# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_Film.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEM(object):
    def setupUi(self, DialogEM):
        DialogEM.setObjectName("DialogEM")
        DialogEM.resize(400, 300)
        DialogEM.setMinimumSize(QtCore.QSize(0, 300))
        DialogEM.setMaximumSize(QtCore.QSize(16777215, 300))
        DialogEM.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEM)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_titlu = QtWidgets.QLabel(DialogEM)
        self.label_titlu.setMinimumSize(QtCore.QSize(0, 40))
        self.label_titlu.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_titlu.setStyleSheet("color: rgb(170, 85, 255);\n"
"font: 375 14pt \"Segoe UI\";")
        self.label_titlu.setObjectName("label_titlu")
        self.verticalLayout.addWidget(self.label_titlu)
        self.LE_titlu = QtWidgets.QLineEdit(DialogEM)
        self.LE_titlu.setMinimumSize(QtCore.QSize(0, 30))
        self.LE_titlu.setMaximumSize(QtCore.QSize(16777215, 30))
        self.LE_titlu.setStyleSheet("color: white;")
        self.LE_titlu.setText("")
        self.LE_titlu.setObjectName("LE_titlu")
        self.verticalLayout.addWidget(self.LE_titlu)
        self.label_anAp = QtWidgets.QLabel(DialogEM)
        self.label_anAp.setMinimumSize(QtCore.QSize(0, 40))
        self.label_anAp.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_anAp.setStyleSheet("color: rgb(170, 85, 255);\n"
"font: 375 14pt \"Segoe UI\";")
        self.label_anAp.setObjectName("label_anAp")
        self.verticalLayout.addWidget(self.label_anAp)
        self.LE_anAp = QtWidgets.QLineEdit(DialogEM)
        self.LE_anAp.setMinimumSize(QtCore.QSize(0, 30))
        self.LE_anAp.setMaximumSize(QtCore.QSize(16777215, 30))
        self.LE_anAp.setStyleSheet("color: white;")
        self.LE_anAp.setObjectName("LE_anAp")
        self.verticalLayout.addWidget(self.LE_anAp)
        self.label = QtWidgets.QLabel(DialogEM)
        self.label.setStyleSheet("color: rgb(170, 85, 255);\n"
"font: 375 14pt \"Segoe UI\";\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(DialogEM)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CBD_OK = QtWidgets.QPushButton(DialogEM)
        self.CBD_OK.setMinimumSize(QtCore.QSize(100, 30))
        self.CBD_OK.setMaximumSize(QtCore.QSize(100, 30))
        self.CBD_OK.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.CBD_OK.setObjectName("CBD_OK")
        self.horizontalLayout.addWidget(self.CBD_OK)
        self.CBD_Cancel = QtWidgets.QPushButton(DialogEM)
        self.CBD_Cancel.setMinimumSize(QtCore.QSize(100, 30))
        self.CBD_Cancel.setMaximumSize(QtCore.QSize(100, 30))
        self.CBD_Cancel.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.CBD_Cancel.setObjectName("CBD_Cancel")
        self.horizontalLayout.addWidget(self.CBD_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogEM)
        QtCore.QMetaObject.connectSlotsByName(DialogEM)

    def retranslateUi(self, DialogEM):
        _translate = QtCore.QCoreApplication.translate
        DialogEM.setWindowTitle(_translate("DialogEM", "Edit Movie"))
        self.label_titlu.setText(_translate("DialogEM", "Titlu"))
        self.label_anAp.setText(_translate("DialogEM", "An aparitie"))
        self.label.setText(_translate("DialogEM", "Gen"))
        self.comboBox.setItemText(0, _translate("DialogEM", "Action"))
        self.comboBox.setItemText(1, _translate("DialogEM", "Adventure"))
        self.comboBox.setItemText(2, _translate("DialogEM", "Animated"))
        self.comboBox.setItemText(3, _translate("DialogEM", "Comedy"))
        self.comboBox.setItemText(4, _translate("DialogEM", "Drama"))
        self.comboBox.setItemText(5, _translate("DialogEM", "Fantasy"))
        self.comboBox.setItemText(6, _translate("DialogEM", "Horror"))
        self.comboBox.setItemText(7, _translate("DialogEM", "Musical"))
        self.comboBox.setItemText(8, _translate("DialogEM", "Mystery"))
        self.comboBox.setItemText(9, _translate("DialogEM", "Romance"))
        self.comboBox.setItemText(10, _translate("DialogEM", "Thriller"))
        self.comboBox.setItemText(11, _translate("DialogEM", "SuperHero"))
        self.CBD_OK.setText(_translate("DialogEM", "OK"))
        self.CBD_Cancel.setText(_translate("DialogEM", "Cancel"))
