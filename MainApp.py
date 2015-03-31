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
# Initialize Qt resources from file resources.py
from resources import *
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
        self.model = self.create_model(path)
        self.ui.view.setModel(self.model)
        self.ui.view.horizontalHeader().setStretchLastSection(True)
        

        # SIGNAL/SLOTS CONNECTION
        self.ui.search_string.textChanged.connect(self.search)
        self.ui.search.clicked.connect(self.check)



    # filtering tableview
    def search(self, text):
        self.model.setFilterRegExp(QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive))


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
                firts_line = False        
                
        model.setHorizontalHeaderLabels(header)
        proxy = QtGui.QSortFilterProxyModel()
        proxy.setFilterKeyColumn(1)
        proxy.setSourceModel(model)
        return proxy


    def check(self):
        rows = self.model.rowCount()
        for row in xrange(0,rows):
            index = self.model.index(row,0)
            data = self.model.data(index)
            print data











