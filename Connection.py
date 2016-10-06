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
from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import QgsMessageBar
from osgeo import ogr
from ui_Connection import Ui_Connection


class Connection(QtGui.QDialog):

	def __init__(self, iface, driverName, parent):
		QtGui.QDialog.__init__(self)
		self.iface = iface
		self.driverName = driverName
		self.parent = parent
		self.setFixedSize(400, 284)

		# Set up the user interface from Designer.
		self.ui = Ui_Connection()
		self.ui.setupUi(self)

		# set up widget
		self.ui.port.setText('5432')
		self.settings = QtCore.QSettings('Import-RUIAN', 'connections')
		self.settings.beginGroup(self.driverName)
		self.ui.conn.addItem('')
		self.ui.conn.addItems(self.settings.allKeys())

		# SIGNAL/SLOTS CONNECTION
		self.ui.buttonBox.button(QtGui.QDialogButtonBox.Apply).clicked.connect(self.set_connection)    # set connection and (save)
		self.ui.remove.clicked.connect(self.remove_connection)				# remove connection - save
		self.ui.conn.activated['QString'].connect(self.load_connection)		# load connection parametres - save
		

	# create connection and optionally save
	def set_connection(self):
		db = self.parent.driverTypes[self.driverName]
		name = self.ui.name.text()
		host = self.ui.host.text()
		port = self.ui.port.text()
		dbname = self.ui.dbname.text()
		user = self.ui.user.text()
		password = self.ui.password.text()
		passwordh = self.ui.password.displayText()

		self.setCursor(QtCore.Qt.WaitCursor)
		connString = '{}:host={} port={} dbname={} user={} password={}'.format(db,host,port,dbname,user,password)
		connList = [host,port,dbname,user,password]
		driver = ogr.GetDriverByName(str(self.driverName))
		capability = driver.Open(connString)

		if capability is None:
			self.iface.messageBar().pushMessage(u"K databázi {} se nepodařilo připojit".format(dbname), level=QgsMessageBar.CRITICAL, duration=5)
			self.setCursor(QtCore.Qt.ArrowCursor)
			return
		if self.ui.save.isChecked():
			if name =='': name = dbname
			reply = QtGui.QMessageBox.question(self, u'Uložení hesla', u"Opravdu chcete uložit heslo? To bude uloženo ve formě prostého textu. Pokud heslo nechcete z bezpečnostních důvodů ukládat, opusťtě tuto nabídku a změňte nastavení",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
			if reply == QtGui.QMessageBox.Yes:
				self.save_connection(name,connList)
				self.iface.messageBar().pushMessage(u'Připojení k databázi {} bylo úspěšné (uloženo)'.format(dbname), level=QgsMessageBar.INFO, duration=5)
				self.parent.ui.driverBox.setToolTip('{}:host={} port={} dbname={} user={} password={}'.format(db,host,port,dbname,user,passwordh))
				self.parent.option['driver'] = self.driverName
				self.parent.option['datasource'] = connString
			else: return
		else:
			self.iface.messageBar().pushMessage(u'Připojení k databázi {} bylo úspěšné'.format(dbname), level=QgsMessageBar.INFO, duration=5)
			self.parent.ui.driverBox.setToolTip('{}:host={} port={} dbname={} user={} password={}'.format(db,host,port,dbname,user,passwordh))
			self.parent.option['driver'] = self.driverName
			self.parent.option['datasource'] = connString

		self.hide()


	# save QSettings connection
	def save_connection(self, name, connList):
		self.settings.setValue(name, connList)


	# load QSettings to lineedits
	def load_connection(self, name):
		if name:
			connList = self.settings.value(name)
			self.ui.name.setText(name)
			self.ui.host.setText(connList[0])
			self.ui.port.setText(connList[1])
			self.ui.dbname.setText(connList[2])
			self.ui.user.setText(connList[3])
			self.ui.password.setText(connList[4])
			

	# remove connections from QSettings
	def remove_connection(self):
		name = self.ui.conn.currentText()
		reply = QtGui.QMessageBox.question(self, u'Potvrdit smazání', u"Opravdu chcete odstranit připojení {}?".format(name), 
				QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
		if reply == QtGui.QMessageBox.Yes:
			self.settings.remove(name)
			self.ui.conn.clear()
			self.ui.conn.addItem('')
			self.ui.conn.addItems(self.settings.allKeys())
			self.ui.name.clear()
			self.ui.host.clear()
			self.ui.dbname.clear()
			self.ui.user.clear()
			self.ui.password.clear()

	# exit dialog
	def reject(self):
		self.parent.ui.driverBox.setCurrentIndex(0)
		self.hide()
