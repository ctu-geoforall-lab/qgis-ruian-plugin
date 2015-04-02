# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_MainApp.ui'
#
# Created: Thu Apr  2 05:15:01 2015
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
        MainApp.resize(601, 471)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainApp.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(MainApp)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.output = QtGui.QLabel(MainApp)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName(_fromUtf8("output"))
        self.verticalLayout.addWidget(self.output)
        self.set = QtGui.QPushButton(MainApp)
        self.set.setObjectName(_fromUtf8("set"))
        self.verticalLayout.addWidget(self.set)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.driver = QtGui.QComboBox(MainApp)
        self.driver.setMinimumSize(QtCore.QSize(150, 0))
        self.driver.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.driver.setObjectName(_fromUtf8("driver"))
        self.driver.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.driver)
        self.datasource = QtGui.QLineEdit(MainApp)
        self.datasource.setMinimumSize(QtCore.QSize(301, 0))
        self.datasource.setObjectName(_fromUtf8("datasource"))
        self.verticalLayout_2.addWidget(self.datasource)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.check = QtGui.QToolButton(MainApp)
        self.check.setMaximumSize(QtCore.QSize(20, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check.setIcon(icon1)
        self.check.setIconSize(QtCore.QSize(20, 20))
        self.check.setAutoExclusive(False)
        self.check.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.check.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.check.setAutoRaise(True)
        self.check.setObjectName(_fromUtf8("check"))
        self.horizontalLayout_3.addWidget(self.check)
        self.uncheck = QtGui.QToolButton(MainApp)
        self.uncheck.setMaximumSize(QtCore.QSize(20, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/uncheck.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uncheck.setIcon(icon2)
        self.uncheck.setIconSize(QtCore.QSize(20, 20))
        self.uncheck.setCheckable(False)
        self.uncheck.setChecked(False)
        self.uncheck.setAutoExclusive(False)
        self.uncheck.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.uncheck.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.uncheck.setAutoRaise(True)
        self.uncheck.setArrowType(QtCore.Qt.NoArrow)
        self.uncheck.setObjectName(_fromUtf8("uncheck"))
        self.horizontalLayout_3.addWidget(self.uncheck)
        self.search = QtGui.QComboBox(MainApp)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.search.setFont(font)
        self.search.setEditable(False)
        self.search.setDuplicatesEnabled(False)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout_3.addWidget(self.search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.view = QtGui.QTableView(MainApp)
        self.view.setMinimumSize(QtCore.QSize(0, 176))
        self.view.setObjectName(_fromUtf8("view"))
        self.verticalLayout_3.addWidget(self.view)
        self.more = QtGui.QToolButton(MainApp)
        self.more.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.more.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.more.setAutoRaise(True)
        self.more.setArrowType(QtCore.Qt.RightArrow)
        self.more.setObjectName(_fromUtf8("more"))
        self.verticalLayout_3.addWidget(self.more)
        self.advanced = QtGui.QWidget(MainApp)
        self.advanced.setMinimumSize(QtCore.QSize(0, 100))
        self.advanced.setObjectName(_fromUtf8("advanced"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.advanced)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.advanced)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.advanced)
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
        self.output.setText(_translate("MainApp", "Výstup:", None))
        self.set.setText(_translate("MainApp", "Spojení", None))
        self.driver.setItemText(0, _translate("MainApp", "--Vybrat--", None))
        self.check.setToolTip(_translate("MainApp", "<html><head/><body><p>Přidat vše</p></body></html>", None))
        self.check.setText(_translate("MainApp", "...", None))
        self.uncheck.setToolTip(_translate("MainApp", "<html><head/><body><p>Odebrat vše</p></body></html>", None))
        self.uncheck.setText(_translate("MainApp", "...", None))
        self.more.setText(_translate("MainApp", "Pokročilé", None))
        self.label.setText(_translate("MainApp", "Zde bude pokročilé nastavení importu", None))

import resources_rc
