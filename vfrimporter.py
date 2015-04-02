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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources_rc.py
from resources_rc import *
# Import Main dialog source
from MainApp import MainApp

class VFRImporter:

    def __init__(self, iface):
        # save reference to the QGIS interface
        self.iface = iface


    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(':/icon.png'),'Tool for import RUIAN data', self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        
    
    def unload(self):
        # Remove plugin icon
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        #create and show main dialog
        dlg = MainApp(self.iface)
        dlg.show()
        result = dlg.exec_()
