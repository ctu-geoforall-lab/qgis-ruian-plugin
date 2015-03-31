# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VFRImporter
                                 A QGIS plugin
 Tool for import RUIAN data
                             -------------------
        begin                : 2015-03-16
        copyright            : (C) 2015 by Jan Klima
        email                : honzi.klima@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

def name():
    return "VFRImporter"


def description():
    return "Tool for import RUIAN data"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Jan Klima"

"""This is called when the plugin gets loaded to QGIS"""
def classFactory(iface):
    # Import VFRImporter class from vfrimporter file
    from vfrimporter import VFRImporter
    return VFRImporter(iface)