# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VFRImporter
                                 A QGIS plugin
 Tool for import RUIAN data
                              -------------------
        begin                : 2015-03-16
        git sha              : $Format:$
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
from __future__ import absolute_import
from builtins import object

# Import the PyQt, QGIS libraries and classes
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from .resources import *
from .MainApp import MainApp

class VFRImporter(object):

    def __init__(self, iface):
        self.iface = iface
        self.actions = []
        self.menu = u'RUIAN Plugin'

    def initGui(self):
        self.action = QAction(
            QIcon(':/icon.png'),
            u'Nástroj pro práci s daty RUIAN',
            self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action)
        self.action.setObjectName(u'spustitRUIANPlugin')
        self.action.setWhatsThis(u'Spustí RUIAN Plugin')
        self.action.setStatusTip(u'Toto spustí RUIAN Plugin')
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu(self.menu,self.action)
        self.actions.append(self.action)
        
    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                u'RUIAN Plugin',
                action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        dlg = MainApp(self.iface)
        dlg.show()
