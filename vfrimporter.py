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
# Import the PyQt, QGIS libraries and classes
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from resources_rc import *
from MainApp import MainApp


class VFRImporter:

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(QIcon(':/icon.png'),u'Nástroj pro práci s daty RUIAN', self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action)
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        
    def unload(self):
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        dlg = MainApp(self.iface)
        dlg.show()
