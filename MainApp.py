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
import os
# Import the PyQt and QGIS libraries
from PyQt4 import QtCore, QtGui
from qgis.core import *
#Import python GUI
from ui_MainApp import Ui_MainApp



class MainApp(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)

        # Set up the table view
        self.ui.view.setSortingEnabled(True)
        self.ui.view.setVisible(True)
        self.ui.view.setCornerButtonEnabled(False)
        path = os.path.join(os.path.dirname(__file__), 'files','obce_cr.csv')
        self.model, self.proxy = self.create_model(path)
        self.ui.view.setModel(self.proxy)
        self.ui.view.horizontalHeader().setStretchLastSection(True)

        # set up widgets
        self.ui.search.addItems(["Obec", "ORP", "Okres", "Kraj"])
        self.ui.search.setEditable(True)
        self.ui.search.clearEditText()
        self.ui.advanced.hide()

        # SIGNAL/SLOTS CONNECTION
        self.ui.search.activated.connect(self.search_column)
        self.ui.search.editTextChanged.connect(self.search)
        self.ui.check.clicked.connect(lambda: self.check(0))
        self.ui.uncheck.clicked.connect(lambda: self.check(1))
        self.ui.more.clicked.connect(self.advanced)
        self.ui.buttonBox.accepted.connect(self.start_import)



    # create model-view
    def create_model(self, file_path):
        model = QtGui.QStandardItemModel(self)
        firts_line = True
        header = []

        with open(file_path, 'r') as f:
            for line in f:
                line = line.replace('\n','')
                items = []
                if firts_line:
                    for word in line.split(','):
                        word = u'{}'.format(word.decode('utf-8'))
                        header.append(word)
                    firts_line = False
                else:
                    for word in line.split(','):
                        word = u'{}'.format(word.decode('utf-8'))
                        item = QtGui.QStandardItem(word)
                        item.setEnabled(True)
                        item.setSelectable(True)
                        item.setEditable(False)
                        items.append(item)
                    items[0].setCheckable(True)
                    model.appendRow(items)        
                
        model.setHorizontalHeaderLabels(header)
        proxy = QtGui.QSortFilterProxyModel()
        proxy.setFilterKeyColumn(1)
        proxy.setSourceModel(model)
        return model, proxy


    # filtering tableview
    def search_column(self, column):
        self.ui.search.clearEditText()
        self.proxy.setFilterKeyColumn(column+1)

    def search(self, text):
        self.proxy.setFilterRegExp(QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive))


    #check or uncheck items in qtableview
    def check(self, state):
        rows = self.proxy.rowCount()
        for row in xrange(0,rows):
            proxy_idx = self.proxy.index(row,0)
            model_idx = self.proxy.mapToSource(proxy_idx)
            item = self.model.itemFromIndex(model_idx)
            if item.isCheckable():
                if state == 0:
                    item.setCheckState(QtCore.Qt.Checked)
                elif state == 1:
                    item.setCheckState(QtCore.Qt.Unchecked)

    #show advance option
    def advanced(self):
        if self.ui.more.arrowType() == 4:
            self.ui.more.setArrowType(QtCore.Qt.DownArrow)
            self.ui.advanced.show()
        elif self.ui.more.arrowType() == 2:
            self.ui.more.setArrowType(QtCore.Qt.RightArrow)
            self.ui.advanced.hide()
                

    # run importing data
    def start_import(self):
        rows = self.model.rowCount()
        for row in xrange(0,rows):
            code = self.model.item(row,0)
            if code.checkState() == 2:
                print code.text()











