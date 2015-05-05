# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Connection.ui'
#
# Created: Tue May  5 18:19:40 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Connection(object):
    def setupUi(self, Connection):
        Connection.setObjectName(_fromUtf8("Connection"))
        Connection.resize(420, 284)
        Connection.setMinimumSize(QtCore.QSize(420, 284))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Connection)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.layout = QtGui.QHBoxLayout()
        self.layout.setObjectName(_fromUtf8("layout"))
        self.labels = QtGui.QVBoxLayout()
        self.labels.setObjectName(_fromUtf8("labels"))
        self.conn_lbl = QtGui.QLabel(Connection)
        self.conn_lbl.setObjectName(_fromUtf8("conn_lbl"))
        self.labels.addWidget(self.conn_lbl)
        self.name_lbl = QtGui.QLabel(Connection)
        self.name_lbl.setObjectName(_fromUtf8("name_lbl"))
        self.labels.addWidget(self.name_lbl)
        self.host_lbl = QtGui.QLabel(Connection)
        self.host_lbl.setObjectName(_fromUtf8("host_lbl"))
        self.labels.addWidget(self.host_lbl)
        self.port_lbl = QtGui.QLabel(Connection)
        self.port_lbl.setObjectName(_fromUtf8("port_lbl"))
        self.labels.addWidget(self.port_lbl)
        self.dbname_lbl = QtGui.QLabel(Connection)
        self.dbname_lbl.setObjectName(_fromUtf8("dbname_lbl"))
        self.labels.addWidget(self.dbname_lbl)
        self.user_lbl = QtGui.QLabel(Connection)
        self.user_lbl.setObjectName(_fromUtf8("user_lbl"))
        self.labels.addWidget(self.user_lbl)
        self.passwd_lbl = QtGui.QLabel(Connection)
        self.passwd_lbl.setObjectName(_fromUtf8("passwd_lbl"))
        self.labels.addWidget(self.passwd_lbl)
        self.layout.addLayout(self.labels)
        self.edits = QtGui.QVBoxLayout()
        self.edits.setObjectName(_fromUtf8("edits"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.conn = QtGui.QComboBox(Connection)
        self.conn.setMinimumSize(QtCore.QSize(0, 0))
        self.conn.setObjectName(_fromUtf8("conn"))
        self.horizontalLayout.addWidget(self.conn)
        self.remove = QtGui.QToolButton(Connection)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon)
        self.remove.setIconSize(QtCore.QSize(12, 12))
        self.remove.setAutoRaise(True)
        self.remove.setObjectName(_fromUtf8("remove"))
        self.horizontalLayout.addWidget(self.remove)
        self.edits.addLayout(self.horizontalLayout)
        self.name = QtGui.QLineEdit(Connection)
        self.name.setMinimumSize(QtCore.QSize(0, 0))
        self.name.setObjectName(_fromUtf8("name"))
        self.edits.addWidget(self.name)
        self.host = QtGui.QLineEdit(Connection)
        self.host.setObjectName(_fromUtf8("host"))
        self.edits.addWidget(self.host)
        self.port = QtGui.QLineEdit(Connection)
        self.port.setObjectName(_fromUtf8("port"))
        self.edits.addWidget(self.port)
        self.dbname = QtGui.QLineEdit(Connection)
        self.dbname.setObjectName(_fromUtf8("dbname"))
        self.edits.addWidget(self.dbname)
        self.user = QtGui.QLineEdit(Connection)
        self.user.setObjectName(_fromUtf8("user"))
        self.edits.addWidget(self.user)
        self.password = QtGui.QLineEdit(Connection)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.edits.addWidget(self.password)
        self.layout.addLayout(self.edits)
        self.verticalLayout_2.addLayout(self.layout)
        self.buttons = QtGui.QHBoxLayout()
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.save = QtGui.QCheckBox(Connection)
        self.save.setObjectName(_fromUtf8("save"))
        self.buttons.addWidget(self.save)
        self.buttonBox = QtGui.QDialogButtonBox(Connection)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.buttons.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.buttons)

        self.retranslateUi(Connection)
        QtCore.QMetaObject.connectSlotsByName(Connection)

    def retranslateUi(self, Connection):
        Connection.setWindowTitle(_translate("Connection", "Dialog", None))
        self.conn_lbl.setText(_translate("Connection", "Připojení", None))
        self.name_lbl.setText(_translate("Connection", "Název", None))
        self.host_lbl.setText(_translate("Connection", "Hostitel", None))
        self.port_lbl.setText(_translate("Connection", "Port", None))
        self.dbname_lbl.setText(_translate("Connection", "Databáze", None))
        self.user_lbl.setText(_translate("Connection", "Jméno", None))
        self.passwd_lbl.setText(_translate("Connection", "Heslo", None))
        self.remove.setText(_translate("Connection", "...", None))
        self.save.setText(_translate("Connection", "Uložit", None))

import resources_rc
