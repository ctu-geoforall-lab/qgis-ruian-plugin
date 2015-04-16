# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VFRImporter_dialog
                                 A QGIS plugin
 Tool for import RUIAN data
                             -------------------
        begin                : 2015-03-16
        git sha              : $Format:%
        copyright            : (C) 2015 by Jan Klima
        email                : honzi.klima@gmail.com
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
#import subprocess
from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import QgsMessageBar
from osgeo import ogr, gdal
from Connection import Connection
from ui_MainApp import Ui_MainApp


class MainApp(QtGui.QDialog):

    def __init__(self, iface, parent=None):
        QtGui.QDialog.__init__(self)
        self.iface = iface
        self.driverTypes = {'PostgreSQL':'PG','MSSQLSpatial':'MSSQL','SQLite':'sqlite','GPKG':'gpkg','Nepodporuje':0}
        self.driverNames = ['PostgreSQL','MSSQLSpatial','SQLite','GPKG', 'Nepodporuje']
        self.missDrivers = []
        self.option = {'driver':None, 'datasource':None}


        version = gdal.__version__.split('.', 2)
        if not (int(version[0]) > 1 or int(version[1]) >= 11):
            self.iface.messageBar().pushMessage(u"GDAL/OGR: požadována verze 1.11 nebo vyšší (nainstalována {}.{})".format(version[0],version[1]), level=QgsMessageBar.CRITICAL, duration=5)


        # Set up the user interface from Designer.
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)

        # set up widget
        self.ui.driverBox.setToolTip(u'Zvolte typ výstupního souboru/databáze')
        self.ui.driverBox.addItem('--Vybrat--')
        self.set_comboDrivers(self.driverNames) 
        self.ui.driverBox.insertSeparator(3)  
        self.ui.search.addItems(['Obec', 'ORP', 'Okres', 'Kraj'])
        self.ui.search.setEditable(True)
        self.ui.search.clearEditText()
        self.ui.advanced.hide()
        self.ui.import_btn.setEnabled(False)

        # Set up the table view
        path = os.path.join(os.path.dirname(__file__), 'files','obce_cr.csv')
        self.model, self.proxy = self.create_model(path)
        self.ui.view.setModel(self.proxy)
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
        self.ui.driverBox.activated['QString'].connect(self.set_datasource)              # set datasource
        self.ui.driverBox.currentIndexChanged['QString'].connect(self.enable_import)     # enable import button
        self.ui.search.activated.connect(self.set_searchColumn)         # set column for searching
        self.ui.search.editTextChanged.connect(self.start_searching)       # start filtering view
        self.ui.check.clicked.connect(lambda: self.set_checkstate(0))   # set checkstate
        self.ui.uncheck.clicked.connect(lambda: self.set_checkstate(1)) # set checkstate
        self.ui.advanced_btn.clicked.connect(self.show_advanced)        # show advanced widget
        self.ui.import_btn.clicked.connect(self.start_import)           # start importing RUIAN data
        self.ui.buttonBox.rejected.connect(self.close)                  # close program

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
        if driverName in self.missDrivers:
            self.ui.driverBox.setCurrentIndex(0)
            self.iface.messageBar().pushMessage(u"Nainstalovaná verze GDAL nepodporuje ovladač {}".format(driverName), level=QgsMessageBar.CRITICAL, duration=5)
            return

        elif driverName in ['SQLite', 'GPKG']:
            connString = QtGui.QFileDialog.getSaveFileName(self,u'Vybrat/vytvořit soubor','output.{}'.format(self.driverTypes[driverName]),'{} (*.{})'.format(driverName, self.driverTypes[driverName]),QtGui.QFileDialog.DontConfirmOverwrite)   
            if not connString:
                self.ui.driverBox.setCurrentIndex(0)
                return

            driver = ogr.GetDriverByName(str(driverName))
            capability = driver.TestCapability(ogr._ogr.ODrCCreateDataSource)
                
            if capability:
            	self.ui.driverBox.setToolTip(connString)
                self.option['driver'] = driverName
                self.option['datasource'] = connString
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
    def set_searchColumn(self, column):
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
    def start_import(self):
        print self.option['driver'], self.option['datasource']
        for row in xrange(0,self.model.rowCount()):
            item = self.model.item(row,0)
            if item.checkState() == QtCore.Qt.Checked:
                code = self.model.item(row,1).text()
                city = self.model.item(row,2).text()
                district = self.model.item(row,4).text()
                print (u'Obec {} ({})'.format(city,district))
     
    # close application
    def close(self):
        self.hide()