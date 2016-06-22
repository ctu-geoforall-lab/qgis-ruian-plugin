# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VFRImporter_dialog
                                 A QGIS plugin
 Tool for import RUIAN data
                             -------------------
        begin                : 2015-03-16
        git sha              : $Format:%
        copyright            : (C) 2015 by Jan Klima (C) 2016 by Dennis Dvořák
        email                : honzi.klima@gmail.com; dennis.dvorak@email.cz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt, QGIS libraries and classes
import os
import sys

#import subprocess
from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import QgsMessageBar
from osgeo import ogr, gdal
from Connection import Connection
from ui_MainApp import Ui_MainApp
import time
from gdal_vfr.vfr4ogr import VfrOgr

debug=True

class MainApp(QtGui.QDialog):

    def __init__(self, iface, parent=None):
        QtGui.QDialog.__init__(self)
        self.iface = iface
        self.driverTypes = {'PostgreSQL':'PG','MSSQLSpatial':'MSSQL','SQLite':'sqlite','ESRI Shapefile':'shp','GPKG':'gpkg','Nepodporuje':0}
        self.driverNames = ['SQLite']
        #'PostgreSQL','MSSQLSpatial','SQLite','GPKG', 'ESRI Shapefile', 'Nepodporuje'
        self.missDrivers = []
        self.option = {'driver':None, 'datasource':None, 'layers':[], 'layers_name':[]}

        # Set up the user interface from Designer.
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)

        # test GDAL version
        version = gdal.__version__.split('.', 2)
        if not (int(version[0]) > 1 or int(version[1]) >= 11):
            self.iface.messageBar().pushMessage(u"GDAL/OGR: požadována verze 1.11 nebo vyšší (nainstalována {}.{})".format(version[0],version[1]), level=QgsMessageBar.CRITICAL, duration=5)

        # set up widget
        self.ui.driverBox.setToolTip(u'Zvolte typ výstupního souboru/databáze')
        self.ui.driverBox.addItem('--Vybrat--')
        self.set_comboDrivers(self.driverNames) 
        self.ui.driverBox.insertSeparator(4)  
        self.ui.search.addItems(['Obec', 'ORP', 'Okres', 'Kraj'])
        self.ui.search.setEditable(True)
        self.ui.search.clearEditText()
        self.ui.advanced.hide()
        if not debug:
            self.ui.import_btn.setEnabled(False)
        else:
            self.option['driver'] = 'SQLite'
            self.option['datasource'] = '/tmp/ruian.db'

        # Set up the table view
        path = os.path.join(os.path.dirname(__file__), 'files','obce_cr.csv')
        self.model, self.proxy = self.create_model(path)
        self.ui.view.setModel(self.proxy)
        self.ui.view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.view.setCornerButtonEnabled(False)
        self.ui.view.setSortingEnabled(True)
        self.ui.view.sortByColumn(2,0)
        self.ui.view.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.ui.view.horizontalHeader().setResizeMode(0,2)
        self.ui.view.horizontalHeader().resizeSection(0,28)
        self.ui.view.horizontalHeader().setStretchLastSection(True)
        self.ui.view.verticalHeader().setResizeMode(2)
        self.ui.view.verticalHeader().setDefaultSectionSize(23)
        self.ui.view.verticalHeader().hide()

        # SIGNAL/SLOTS CONNECTION
        self.ui.driverBox.activated['QString'].connect(self.set_datasource)              
        self.ui.driverBox.currentIndexChanged['QString'].connect(self.enable_import)     
        self.ui.search.activated.connect(self.set_searching)        
        self.ui.search.editTextChanged.connect(self.start_searching)       
        self.ui.check.clicked.connect(lambda: self.set_checkstate(0))   
        self.ui.uncheck.clicked.connect(lambda: self.set_checkstate(1)) 
        self.ui.advanced_btn.clicked.connect(self.show_advanced)        
        self.ui.import_btn.clicked.connect(self.get_options)          
        self.ui.buttonBox.rejected.connect(self.close)                

    # set combobox drivers
    def set_comboDrivers(self, driverNames):   
        model = self.ui.driverBox.model()
        for driverName in driverNames:
            item = QtGui.QStandardItem(str(driverName))
            driver = ogr.GetDriverByName(str(driverName))
            if driver is None:
                self.missDrivers.append(driverName)
                item.setForeground(QtGui.QColor(180,180,180,100))
                model.appendRow(item)
            else:
                model.appendRow(item)


    # create model-view
    def create_model(self, file_path):
        model = QtGui.QStandardItemModel(self)
        firts_line = True
        header = []
        header.append('')

        with open(file_path, 'r') as f:
            for line in f:
                line = line.replace('\n','')
                if firts_line:
                    for word in line.split(','):
                        word = u'{}'.format(word.decode('utf-8'))
                        header.append(word)
                    firts_line = False
                else:
                    items = []
                    item = QtGui.QStandardItem('')
                    item.setCheckable(True)
                    item.setSelectable(False)
                    items.append(item)
                    for word in line.split(','):
                        word = u'{}'.format(word.decode('utf-8'))
                        item = QtGui.QStandardItem(word)
                        item.setSelectable(False)
                        items.append(item)
                    model.appendRow(items)        
                
        model.setHorizontalHeaderLabels(header)
        proxy = QtGui.QSortFilterProxyModel()
        proxy.setFilterKeyColumn(2)
        proxy.setSourceModel(model)
        return model, proxy


    # set driver and datasource
    def set_datasource(self, driverName):
        if self.ui.import_btn.isEnabled():
            self.ui.import_btn.setEnabled(False)

        if driverName in self.missDrivers:
            self.ui.driverBox.setCurrentIndex(0)
            self.iface.messageBar().pushMessage(u"Nainstalovaná verze GDAL nepodporuje ovladač {}".format(driverName), level=QgsMessageBar.CRITICAL, duration=5)
            return

        if driverName in ['SQLite', 'GPKG', 'ESRI Shapefile']: ### only SQLite currently works
            connString = QtGui.QFileDialog.getSaveFileName(self,
                                                           u'Vybrat/vytvořit soubor','output.{}'.format(
                                                               self.driverTypes[driverName]),
                                                           '{} (*.{})'.format(driverName, self.driverTypes[driverName]),
                                                           QtGui.QFileDialog.DontConfirmOverwrite)
            if not connString:
                self.ui.driverBox.setCurrentIndex(0)
                return

            driver = ogr.GetDriverByName(str(driverName))
            capability = driver.TestCapability(ogr._ogr.ODrCCreateDataSource)
                
            if capability:
            	self.ui.driverBox.setToolTip(connString)
                self.option['driver'] = driverName
                self.option['datasource'] = connString
                if not self.ui.import_btn.isEnabled():
                    self.ui.import_btn.setEnabled(True)
            else:
            	self.iface.messageBar().pushMessage(u"Soubor {} nelze vybrat/vytvořit".format(connString), level=QgsMessageBar.CRITICAL, duration=5)
                self.ui.driverBox.setCurrentIndex(0)

        elif driverName in ['PostgreSQL','MSSQLSpatial']:
            self.connection = Connection(self.iface, driverName, self)
            self.connection.setModal(True)
            self.connection.show()
            self.connection.setWindowTitle(u'Připojení k databázi {}'.format(driverName))

    def enable_import(self, driverName):
        if driverName == '--Vybrat--':
            self.ui.driverBox.setToolTip(u'Zvolte typ výstupního souboru/databáze')
            self.ui.import_btn.setEnabled(False)
        else:
            self.ui.import_btn.setEnabled(True)


    # filtering tableview
    def set_searching(self, column):
        self.proxy.setFilterKeyColumn(column+2)
        self.ui.search.clearEditText()

    def start_searching(self, searchName):
        if searchName not in ['Obec', 'ORP', 'Okres', 'Kraj']:
            self.proxy.setFilterRegExp(QtCore.QRegExp(searchName, QtCore.Qt.CaseInsensitive))


    # check or uncheck items in qtableview
    def set_checkstate(self, state):
        rows = self.proxy.rowCount()
        for row in xrange(0,rows):
            proxyIdx = self.proxy.index(row,0)
            modelIdx = self.proxy.mapToSource(proxyIdx)
            item = self.model.itemFromIndex(modelIdx)
            if state == 0:
                item.setCheckState(QtCore.Qt.Checked)
            elif state == 1:
                item.setCheckState(QtCore.Qt.Unchecked)


    # show advance option
    def show_advanced(self):
        if self.ui.advanced_btn.arrowType() == 4:
            self.ui.advanced_btn.setArrowType(QtCore.Qt.DownArrow)
            self.ui.advanced.show()
        elif self.ui.advanced_btn.arrowType() == 2:
            self.ui.advanced_btn.setArrowType(QtCore.Qt.RightArrow)
            self.ui.advanced.hide()


    # star importing data
    def get_options(self):
    	self.option['layers'] = []
    	self.option['layers_name'] = []
        for row in xrange(0,self.model.rowCount()):
            item = self.model.item(row,0)
            if item.checkState() == QtCore.Qt.Checked:
            	code = self.model.item(row,1).text()
            	name = self.model.item(row,2).text()
            	self.option['layers'].append(code)
            	self.option['layers_name'].append(name)

        if not self.option['layers']:
            self.iface.messageBar().pushMessage(u"Nejsou vybrána žádná data pro import.", level=QgsMessageBar.INFO, duration=5)
            return

        # create progress dialog
        self.progress = QtGui.QProgressDialog(u'Probíhá import ...', u'Ukončit', 0, 0, self, QtCore.Qt.SplashScreen)
        self.progress.setParent(self)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.setWindowTitle(u'Import dat RÚIAN')
        self.progress.canceled.connect(self.import_close)
        self.progress.setAutoClose(False)
        self.progress.resize(400, 50)
        self.progress.show()

        # start import and set signal
        self.importThread = ImportThread(self.option)
        self.importThread.importEnd.connect(self.import_end)
        self.importThread.importStat.connect(self.set_status)
        if not self.importThread.isRunning():
        	self.progress.show()
        	self.importThread.start()
    
    # update progress status
    def set_status(self, num, tot, text, operation):
    	self.progress.setLabelText(u'{0} {1} z {2} ({3})'.format(operation, num, tot, text))

    # terminate import
    def import_close(self):
    	reply = QtGui.QMessageBox.question(self, u'Ukončit', u"Opravdu chcete ukončit import dat?",
    			QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
    	if reply == QtGui.QMessageBox.Yes:
    		self.importThread.terminate()
    	else:
    		self.progress.resize(400, 50)
    		self.progress.show()

    # import was succesful
    def import_end(self):
        self.progress.cancel()
        reply  = QtGui.QMessageBox.question(self, u'Import', u"Import dat proběhl úspěšně. "
                                            u"Přejete si vytvořené vrtsvy do mapového okna?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.add_layers()

    # close application
    def close(self):
        self.hide()

    # add created layers to map display
    def add_layers(self):
        driver = ogr.GetDriverByName(self.option['driver'])
        datasource = driver.Open(self.option['datasource'], False)
        if not datasource:
            self.iface.messageBar().pushMessage(u"Soubor {} nelze načíst".format(self.option['datasource']), level=QgsMessageBar.CRITICAL, duration=5)
            return

        # TODO: use uri instead of hardcoded datasource for SQLite
        # uri = QgsDataSourceURI()
        # uri.setDatabase(self.option['datasource'])
        # schema = ''
        # geom_column = 'GEOMETRY'
        layers = []
        for idx in range(datasource.GetLayerCount()):
            layer = datasource.GetLayerByIndex(idx)
            layer_name = layer.GetName()
            #uri.setDataSource(schema, layer_name, geom_column)
            vlayer = QgsVectorLayer('{0}|layername={1}'.format(self.option['datasource'], layer_name), layer_name, 'ogr')
            QgsMapLayerRegistry.instance().addMapLayer(vlayer)

        del datasource # close datasource

class ImportThread(QtCore.QThread):
    importEnd = QtCore.pyqtSignal()
    importStat = QtCore.pyqtSignal(int,int,str,str)

    def __init__(self, option):
        QtCore.QThread.__init__(self)
        self.layers = option['layers']
        self.datasource = option['datasource']

    def run(self):
        # create convertor
        os.environ['DATA_DIR'] = os.environ['HOMEPATH'] if sys.platform.startswith('win') else os.environ['HOME']
        ogr = VfrOgr(frmt='SQLite', dsn=self.datasource, overwrite=True, geom_name='OriginalniHranice')

        n = len(self.layers)
        i = 1
        for l in self.layers:
            filename = 'OB_{}_UKSH'.format(l)
            QtCore.qDebug('\n (VFR) Processing file: {}'.format(filename))
            # download
            ogr.reset()
            self.importStat.emit(i, n, l, "Download")
            ogr.download([filename])
            # import
            self.importStat.emit(i, n, l, "Import")
            ogr.run(True if i > 1 else False)
            i += 1
        
        self.importEnd.emit()
