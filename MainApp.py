# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                 A QGIS plugin
                           Tool for importing RUIAN data
                             -------------------
        begin                : 2015-03-16
        git sha              : $Format:%
        copyright            : (C) 2015-2016 by Jan Klima, Dennis Dvořák,
                               and Martin Landa
        email                : honzi.klima@gmail.com; dennis.dvorak@email.cz;
                               martin.landa@fsv.cvut.cz
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
import tempfile
import time

from PyQt4 import QtCore, QtGui

from qgis.core import *
from qgis.gui import QgsMessageBar

from osgeo import ogr, gdal

from Connection import Connection
from ui_MainApp import Ui_MainApp

try:
    from .gdal_vfr.vfr4ogr import VfrOgr
except:
    # download
    import requests, zipfile, StringIO

    gdal_vfr_version = '2.0.4'
    url = "https://github.com/ctu-geoforall-lab/gdal-vfr/archive/v{}.zip".format(gdal_vfr_version)
    req = requests.get(url, stream=True)
    zipf = zipfile.ZipFile(StringIO.StringIO(req.content))
    zipf.extractall(os.path.join(os.path.dirname(__file__)))
    os.rename(os.path.join(os.path.dirname(__file__), 'gdal-vfr-{}'.format(gdal_vfr_version)),
              os.path.join(os.path.dirname(__file__), 'gdal_vfr'))
    zipf.close()

    from .gdal_vfr.vfr4ogr import VfrOgr

class TextOutputSignal(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))

class MainApp(QtGui.QDialog):

    def __init__(self, iface, parent=None):
        QtGui.QDialog.__init__(self)

        self.settings = QtCore.QSettings()

        # sys.stdout = TextOutputSignal(textWritten=self.normalOutputWritten)
        sys.stderr = TextOutputSignal(textWritten=self.errorOutputWritten)

        self.iface = iface
        self.driverTypes = {
#            'PostgreSQL'    :'PG',
#            'MSSQLSpatial'  :'MSSQL',
            'SQLite': { 'alias': 'SQLite',     'ext': 'sqlite'},
            'GPKG'  : { 'alias': 'GeoPackage', 'ext': 'gpkg'  },
            'ESRI Shapefile': { 'alias': 'Esri Shapefile', 'ext': 'shp'  },
        }

        self.missDrivers = [] # list of missing drivers

        # internal settings
        self.option = {'driver'     : None,
                       'datasource' : None,
                       'layers'     : [],
                       'layers_name': []
        }

        # set up the user interface from designed
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)

        # test GDAL version
        version = gdal.__version__.split('.', 2)
        if not (int(version[0]) > 1 or int(version[1]) >= 11):
            self.iface.messageBar().pushMessage(u"GDAL/OGR: požadována verze 1.11 nebo vyšší (nainstalována {}.{})".format(
                version[0],version[1]), level=QgsMessageBar.CRITICAL, duration=5
            )

        # set up widgets
        self.ui.driverBox.setToolTip(u'Zvolte typ výstupního souboru/databáze')
        self.ui.driverBox.addItem('--Vybrat--')
        self.set_comboDrivers(self.driverTypes)
        self.ui.driverBox.insertSeparator(4)  
        self.ui.searchComboBox.addItems(['Obec', 'ORP', 'Okres', 'Kraj'])
        self.ui.searchComboBox.setEditable(True)
        self.ui.searchComboBox.clearEditText()
        self.ui.advancedSettings.hide()

        # set up the table view
        path = os.path.join(os.path.dirname(__file__), 'files','obce_cr.csv')
        self.model, self.proxy = self.create_model(path)
        self.ui.dataView.setModel(self.proxy)
        self.ui.dataView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ui.dataView.setCornerButtonEnabled(False)
        self.ui.dataView.setSortingEnabled(True)
        self.ui.dataView.sortByColumn(2,0)
        self.ui.dataView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.ui.dataView.horizontalHeader().setResizeMode(0,2)
        self.ui.dataView.horizontalHeader().resizeSection(0,28)
        self.ui.dataView.horizontalHeader().setStretchLastSection(True)
        self.ui.dataView.verticalHeader().setResizeMode(2)
        self.ui.dataView.verticalHeader().setDefaultSectionSize(23)
        self.ui.dataView.verticalHeader().hide()

        # signal/slots connections
        self.ui.driverBox.activated['QString'].connect(self.set_datasource)              
        self.ui.driverBox.currentIndexChanged['QString'].connect(self.enable_import)     
        self.ui.searchComboBox.activated.connect(self.set_searching)
        self.ui.searchComboBox.editTextChanged.connect(self.start_searching)
        self.ui.checkButton.clicked.connect(lambda: self.set_checkstate(0))
        self.ui.uncheckButton.clicked.connect(lambda: self.set_checkstate(1))
        self.ui.advancedButton.clicked.connect(self.show_advanced)
        self.ui.importButton.clicked.connect(self.get_options)
        self.ui.buttonBox.rejected.connect(self.close)

    def errorOutputWritten(self, text):
        # self.iface.messageBar().pushMessage(u"Chyba: {}".format(text),
        #                                     level=QgsMessageBar.CRITICAL)
        # QgsMessageLog.logMessage('Ruian plugin: {}'.format(text), level=QgsMessageLog.WARNING)
        pass

    def set_comboDrivers(self, drivers):
        """Set GDAL drivers combo box.

        :param driverNames list of supported drivers
        """
        model = self.ui.driverBox.model()
        for driver in drivers.iteritems():
            item = QtGui.QStandardItem(str(driver[1]['alias']))
            ogrdriver = ogr.GetDriverByName(str(driver[0]))
            if ogrdriver is None:
                self.missDrivers.append(str(driver[1]['alias']))
                item.setForeground(QtGui.QColor(180,180,180,100))
                model.appendRow(item)
            else:
                model.appendRow(item)


    def create_model(self, file_path):
        """Create model-view from file.

        :param file_path: path to the file

        :return model, proxy
        """
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

    def set_datasource(self, driverName):
        """Set GDAL driver and datasource.

        :param driverName: GDAL driver
        """
        if self.ui.importButton.isEnabled():
            self.ui.importButton.setEnabled(False)

        for driverItem in self.driverTypes.iteritems():
            if driverItem[1]['alias'] == driverName:
                driverName = driverItem[0]
                driverAlias = driverItem[1]['alias']
                driverExtension = driverItem[1]['ext']

        if driverName in self.missDrivers:
            # selected driver is not supported by installed GDAL
            self.ui.driverBox.setCurrentIndex(0)
            self.iface.messageBar().pushMessage(u"Nainstalovaná verze GDAL nepodporuje ovladač {}".format(driverAlias),
                                                level=QgsMessageBar.CRITICAL, duration=5)
            return

        connString = None
        if driverName in ['SQLite', 'GPKG', 'ESRI Shapefile']:
            sender = '{}-lastUserFilePath'.format(self.sender().objectName())
            lastUsedFilePath = self.settings.value(sender, '')

            if driverName == 'ESRI Shapefile':
                connString = QtGui.QFileDialog.getExistingDirectory(self,
                                                                    u'Vybrat/vytvořit výstupní adresář',
                                                                    lastUsedFilePath)
            else:
                connString = QtGui.QFileDialog.getSaveFileName(self,
                                                               u'Vybrat/vytvořit výstupní soubor',
                                                               '{}{}ruian.{}'.format(lastUsedFilePath, os.path.sep, driverExtension),
                                                               '{} (*.{})'.format(driverAlias, driverExtension),
                                                               QtGui.QFileDialog.DontConfirmOverwrite)
            if not connString:
                self.ui.driverBox.setCurrentIndex(0)
                return

            self.settings.setValue(sender, os.path.dirname(connString))

            driver = ogr.GetDriverByName(str(driverName))
            capability = driver.TestCapability(ogr._ogr.ODrCCreateDataSource)
                
            if capability:
                self.ui.driverBox.setToolTip(connString)
                self.option['driver'] = str(driverName)
                self.option['datasource'] = connString
                if not self.ui.importButton.isEnabled():
                    self.ui.importButton.setEnabled(True)
            else:
                self.iface.messageBar().pushMessage(u"Soubor {} nelze vybrat/vytvořit".format(connString),
                                                    level=QgsMessageBar.CRITICAL, duration=5)
                self.ui.driverBox.setCurrentIndex(0)

        # elif driverName in ['PostgreSQL','MSSQLSpatial']:
        #     self.connection = Connection(self.iface, driverName, self)
        #     self.connection.setModal(True)
        #     self.connection.show()
        #     self.connection.setWindowTitle(u'Připojení k databázi {}'.format(driverName))

        if connString:
            self.ui.outputPath.setText(connString)

    def enable_import(self, driverName):
        """Enable/disable import widgets.

        :param driverName: selected GDAL driver
        """
        if driverName == '--Vybrat--':
            self.ui.driverBox.setToolTip(u'Zvolte typ výstupního souboru/databáze')
            self.ui.importButton.setEnabled(False)
        else:
            self.ui.importButton.setEnabled(True)

    def data_select(self, data_box):
        """Enable/disable data selection widgets.

        :param data_box: group box
        """
        if self.ui.datasetComboBox.currentIndex() == 1:
            self.ui.selectionComboBox.setEnabled(False)
        else:
            self.ui.selectionComboBox.setEnabled(True)

    def set_searching(self, column):
        """Set filtering.

        :param column: selected column for filtering
        """
        self.proxy.setFilterKeyColumn(column + 2)
        self.ui.searchComboBox.clearEditText()

    def start_searching(self, searchName):
        """Start searching.

        :param searchName: name to be searched
        """
        if searchName not in ['Obec', 'ORP', 'Okres', 'Kraj']:
            self.proxy.setFilterRegExp(QtCore.QRegExp(searchName, QtCore.Qt.CaseInsensitive))

    def set_checkstate(self, state):
        """Check or uncheck items in qtableview.

        :param state: state (true/false)
        """
        rows = self.proxy.rowCount()
        for row in xrange(0,rows):
            proxyIdx = self.proxy.index(row,0)
            modelIdx = self.proxy.mapToSource(proxyIdx)
            item = self.model.itemFromIndex(modelIdx)
            if state == 0:
                item.setCheckState(QtCore.Qt.Checked)
            elif state == 1:
                item.setCheckState(QtCore.Qt.Unchecked)

    def show_advanced(self):
        """Show advanced options.
        """
        if self.ui.advancedButton.arrowType() == 4:
            self.ui.advancedButton.setArrowType(QtCore.Qt.DownArrow)
            self.ui.advancedSettings.show()
        elif self.ui.advancedButton.arrowType() == 2:
            self.ui.advancedButton.setArrowType(QtCore.Qt.RightArrow)
            self.ui.advancedSettings.hide()

    def get_options(self):
        """Start importing data.
        """
        self.option['layers'] = []
        self.option['layers_name'] = []
        for row in xrange(0,self.model.rowCount()):
            item = self.model.item(row,0)
            if item.checkState() == QtCore.Qt.Checked:
                code = self.model.item(row,1).text()
                name = self.model.item(row,2).text()
                self.option['layers'].append(code)
                self.option['layers_name'].append(name)

        # build RUIAN type
        vfr_type = { 'up'  : 'U',
                     'zk'  : 'K',
                     'sh'  : 'S',
                     'zgho': 'H'
        }
        # not supported yet
        # selectionIndex = self.ui.selectionComboBox.currentIndex()
        # if selectionIndex == 1:
        #     vfr_type['zgho'] = 'G'
        # elif selectionIndex == 2:
        #     vfr_type['zgho'] = 'Z'
        # elif selectionIndex == 3:
        #     vfr_type['zgho'] = 'O'

        # not supported yet
        # if self.ui.timeComboBox.currentIndex() == 1:
        #     vfr_type['up'] = 'Z'
        if self.ui.datasetComboBox.currentIndex() == 1:
            vfr_type['zk'] = 'Z'
            vfr_type['zgho'] = 'Z'
        # not supported yet (allows only 'Z' dataset)
        # if self.ui.validityComboBox.currentIndex() == 1:
        #     vfr_type['sh'] = 'H'
        self.option['file_type'] = u'{0}{1}{2}{3}'.format(vfr_type['up'], vfr_type['zk'], vfr_type['sh'], vfr_type['zgho'])

        if not self.option['driver'] or not self.option['datasource']:
            self.iface.messageBar().pushMessage(u"Není vybrán žádný výstup.",
                                                level=QgsMessageBar.CRITICAL, duration=5)
            return

        if not self.option['layers']:
            self.iface.messageBar().pushMessage(u"Nejsou vybrána žádná data pro import.",
                                                level=QgsMessageBar.CRITICAL, duration=5)
            return

        # create progress dialog
        self.progress = QtGui.QProgressDialog(u'Probíhá import ...', u'Ukončit',
                                              0, 0, self)
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
    
    def set_status(self, num, tot, text, operation):
        """Update progress status.
        """
        self.progress.setLabelText(u'{0} {1} z {2} ({3})'.format(operation, num, tot, text))

    def import_close(self):
        """Terminate import.
        """
        reply = QtGui.QMessageBox.question(self, u'Ukončit', u"Opravdu chcete ukončit import dat?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            self.importThread.terminate()
        else:
            self.progress.resize(400, 50)
            self.progress.show()

    def import_end(self):
        """Inform about successfull import.
        """
        self.progress.cancel()
        if self.importThread.aborted:
            return

        reply  = QtGui.QMessageBox.question(self, u'Import', u"Import dat proběhl úspěšně. "
                                            u"Přejete si vytvořené vrtsvy do mapového okna?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            self.add_layers()

    def close(self):
        """Close application."""
        self.hide()

    def add_layers(self):
        """Add created layers to map display.
        """
        def add_layer(group, layer):
            if layer.GetFeatureCount() < 1:
                # skip empty layers
                return False

            # TODO: use uri instead of hardcoded datasource for SQLite
            # uri = QgsDataSourceURI()
            # uri.setDatabase(self.option['datasource'])
            # schema = ''
            # geom_column = 'GEOMETRY'
            #uri.setDataSource(schema, layer_name, geom_column)

            vlayer = QgsVectorLayer('{0}|layername={1}'.format(self.option['datasource'], layer_name), layer_name, 'ogr')
            layer_style = os.path.join(style_path, layer_name + '.qml')
            if os.path.exists(layer_style):
                vlayer.loadNamedStyle(layer_style)

            QgsMapLayerRegistry.instance().addMapLayer(vlayer, addToLegend=False)
            group.addLayer(vlayer)

            return True

        driver = ogr.GetDriverByName(str(self.option['driver']))
        datasource = driver.Open(self.option['datasource'], False)
        if not datasource:
            self.iface.messageBar().pushMessage(u"Soubor {} nelze načíst".format(self.option['datasource']),
                                                level=QgsMessageBar.CRITICAL, duration=5)
            return

        style_path = os.path.join(os.path.dirname(__file__), "styles")

        # new layers will added into this group
        root = QgsProject.instance().layerTreeRoot()
        try:
            groupName = os.path.splitext(
                os.path.basename(self.option['datasource'])
            )[0]
        except:
            groupName = 'ruian'
        layerGroup = root.addGroup(groupName)

        # first add well-known layers
        layers_added = []
        for layer_name, layer_alias in [('obce', u'Obce'),
                                        ('spravniobvody', u'Správní obvody'),
                                        ('mop', u'Městské obvody v Praze'),
                                        ('momc', u'Městský obvod/část'),
                                        ('castiobci', u'Části obcí'),
                                        ('katastralniuzemi', u'Katastrální území'),
                                        ('zsj', u'Základní sídelní jednotky'),
                                        ('ulice', u'Ulice'),
                                        ('parcely', u'Parcely'),
                                        ('stavebniobjekty', u'Stavební objekty'),
                                        ('adresnimista', u'Adresní místa')]:
            layer = datasource.GetLayerByName(layer_name)
            if layer:
                if add_layer(layerGroup, layer):
                    layers_added.append(layer_name)

        for idx in range(datasource.GetLayerCount()):
            layer = datasource.GetLayerByIndex(idx)
            layer_name = layer.GetName()
            if layer_name in layers_added:
                # skip already added layers
                continue
            layers_added.append(layer_name)

        del datasource # close datasource

class ImportThread(QtCore.QThread):
    importEnd = QtCore.pyqtSignal()
    importStat = QtCore.pyqtSignal(int,int,str,str)

    def __init__(self, option):
        QtCore.QThread.__init__(self)
        self.driver = option['driver']
        self.datasource = option['datasource']
        self.layers = option['layers']
        self.file_type = option['file_type']

    def run(self):
        """Run download/import thread.
        """
        # define temporary directory for downloading VFR data
        data_dir = os.path.join(tempfile.gettempdir(),
                                'ruian_plugin_{}'.format(os.getpid()))
        QtCore.qDebug('\n (VFR) data dir: {}'.format(data_dir))
        os.environ['DATA_DIR'] = data_dir
        if not os.path.exists(data_dir):
            ### TODO (#3): osetrit pripad, kdy uzivatel nema pravo zapisu
            os.makedirs(data_dir)

        # logs will be stored also in data directory
        os.environ['LOG_DIR'] = data_dir
        self.aborted = False

        try:
            # create convertor
            ogr = VfrOgr(frmt=self.driver, dsn=self.datasource, overwrite=True, geom_name='OriginalniHranice')

            n = len(self.layers)
            i = 1
            for l in self.layers:
                filename = 'OB_{}_{}'.format(l, self.file_type)
                QtCore.qDebug('\n (VFR) Processing file: {}'.format(filename))
                # download
                ogr.reset()
                self.importStat.emit(i, n, l, "Download")
                ogr.download([filename])
                # import
                self.importStat.emit(i, n, l, "Import")
                ogr.run(True if i > 1 else False)
                i += 1

            ogr.__del__()
            del os.environ['DATA_DIR']
        except:
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)
            sys.stderr.write('{}'.format(value))
            self.aborted = True
            self.terminate()

        self.importEnd.emit()
