# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainApp.ui'
#
# Created: Mon Mar 30 14:43:53 2015
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

class Ui_MainApp(object):
    def setupUi(self, MainApp):
        MainApp.setObjectName(_fromUtf8("MainApp"))
        MainApp.resize(601, 444)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("files/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainApp.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(MainApp)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.driver_lab = QtGui.QLabel(MainApp)
        self.driver_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.driver_lab.setObjectName(_fromUtf8("driver_lab"))
        self.verticalLayout.addWidget(self.driver_lab)
        self.ds = QtGui.QPushButton(MainApp)
        self.ds.setObjectName(_fromUtf8("ds"))
        self.verticalLayout.addWidget(self.ds)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.driver = QtGui.QComboBox(MainApp)
        self.driver.setMinimumSize(QtCore.QSize(150, 0))
        self.driver.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.driver.setObjectName(_fromUtf8("driver"))
        self.driver.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.driver)
        self.ds_string = QtGui.QLineEdit(MainApp)
        self.ds_string.setMinimumSize(QtCore.QSize(301, 0))
        self.ds_string.setObjectName(_fromUtf8("ds_string"))
        self.verticalLayout_2.addWidget(self.ds_string)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.search = QtGui.QToolButton(MainApp)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/VFRImporter/files/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon1)
        self.search.setIconSize(QtCore.QSize(25, 25))
        self.search.setAutoExclusive(False)
        self.search.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.search.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.search.setAutoRaise(True)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout_3.addWidget(self.search)
        self.search_string = QtGui.QLineEdit(MainApp)
        self.search_string.setObjectName(_fromUtf8("search_string"))
        self.horizontalLayout_3.addWidget(self.search_string)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.view = QtGui.QTableView(MainApp)
        self.view.setObjectName(_fromUtf8("view"))
        self.verticalLayout_3.addWidget(self.view)
        self.state = QtGui.QCheckBox(MainApp)
        self.state.setObjectName(_fromUtf8("state"))
        self.verticalLayout_3.addWidget(self.state)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.buttonBox = QtGui.QDialogButtonBox(MainApp)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

    def retranslateUi(self, MainApp):
        MainApp.setWindowTitle(_translate("MainApp", "VFRImporter", None))
        self.driver_lab.setText(_translate("MainApp", "Výstup:", None))
        self.ds.setText(_translate("MainApp", "Spojení", None))
        self.driver.setItemText(0, _translate("MainApp", "--Vybrat--", None))
        self.search.setText(_translate("MainApp", "...", None))
        self.state.setText(_translate("MainApp", "Importovat stát", None))

import resources
