# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_Actor_Regizor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEAR(object):
    def setupUi(self, DialogEAR):
        DialogEAR.setObjectName("DialogEAR")
        DialogEAR.resize(450, 350)
        DialogEAR.setMinimumSize(QtCore.QSize(450, 350))
        DialogEAR.setMaximumSize(QtCore.QSize(450, 350))
        DialogEAR.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogEAR)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_nume = QtWidgets.QLabel(DialogEAR)
        self.label_nume.setMinimumSize(QtCore.QSize(0, 40))
        self.label_nume.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_nume.setStyleSheet("color: rgb(170, 85, 255);\n"
"font: 375 14pt \"Segoe UI\";")
        self.label_nume.setObjectName("label_nume")
        self.verticalLayout.addWidget(self.label_nume)
        self.LE_nume = QtWidgets.QLineEdit(DialogEAR)
        self.LE_nume.setMinimumSize(QtCore.QSize(0, 30))
        self.LE_nume.setMaximumSize(QtCore.QSize(16777215, 30))
        self.LE_nume.setStyleSheet("color: white;")
        self.LE_nume.setText("")
        self.LE_nume.setObjectName("LE_nume")
        self.verticalLayout.addWidget(self.LE_nume)
        self.label_prenume = QtWidgets.QLabel(DialogEAR)
        self.label_prenume.setMinimumSize(QtCore.QSize(0, 40))
        self.label_prenume.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_prenume.setStyleSheet("color: rgb(170, 85, 255);\n"
"font: 375 14pt \"Segoe UI\";")
        self.label_prenume.setObjectName("label_prenume")
        self.verticalLayout.addWidget(self.label_prenume)
        self.LE_prenume = QtWidgets.QLineEdit(DialogEAR)
        self.LE_prenume.setMinimumSize(QtCore.QSize(0, 30))
        self.LE_prenume.setMaximumSize(QtCore.QSize(16777215, 30))
        self.LE_prenume.setStyleSheet("color: white;")
        self.LE_prenume.setObjectName("LE_prenume")
        self.verticalLayout.addWidget(self.LE_prenume)
        self.checkBoxDN = QtWidgets.QCheckBox(DialogEAR)
        self.checkBoxDN.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBoxDN.setObjectName("checkBoxDN")
        self.verticalLayout.addWidget(self.checkBoxDN)
        self.label_dataNasterii = QtWidgets.QLabel(DialogEAR)
        self.label_dataNasterii.setMinimumSize(QtCore.QSize(0, 40))
        self.label_dataNasterii.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_dataNasterii.setStyleSheet("color: rgb(170, 85, 255);\n"
"font: 375 14pt \"Segoe UI\";")
        self.label_dataNasterii.setObjectName("label_dataNasterii")
        self.verticalLayout.addWidget(self.label_dataNasterii)
        self.HLayoutCB = QtWidgets.QHBoxLayout()
        self.HLayoutCB.setObjectName("HLayoutCB")
        self.comboBoxDA_an = QtWidgets.QComboBox(DialogEAR)
        self.comboBoxDA_an.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBoxDA_an.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBoxDA_an.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.comboBoxDA_an.setObjectName("comboBoxDA_an")
        self.HLayoutCB.addWidget(self.comboBoxDA_an)
        self.comboBoxDA_luna = QtWidgets.QComboBox(DialogEAR)
        self.comboBoxDA_luna.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBoxDA_luna.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBoxDA_luna.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.comboBoxDA_luna.setObjectName("comboBoxDA_luna")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.comboBoxDA_luna.addItem("")
        self.HLayoutCB.addWidget(self.comboBoxDA_luna)
        self.comboBoxDA_zi = QtWidgets.QComboBox(DialogEAR)
        self.comboBoxDA_zi.setMinimumSize(QtCore.QSize(0, 25))
        self.comboBoxDA_zi.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBoxDA_zi.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.comboBoxDA_zi.setObjectName("comboBoxDA_zi")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.comboBoxDA_zi.addItem("")
        self.HLayoutCB.addWidget(self.comboBoxDA_zi)
        self.verticalLayout.addLayout(self.HLayoutCB)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.CBD_OK = QtWidgets.QPushButton(DialogEAR)
        self.CBD_OK.setMinimumSize(QtCore.QSize(100, 30))
        self.CBD_OK.setMaximumSize(QtCore.QSize(100, 30))
        self.CBD_OK.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.CBD_OK.setObjectName("CBD_OK")
        self.horizontalLayout.addWidget(self.CBD_OK)
        self.CBD_Cancel = QtWidgets.QPushButton(DialogEAR)
        self.CBD_Cancel.setMinimumSize(QtCore.QSize(100, 30))
        self.CBD_Cancel.setMaximumSize(QtCore.QSize(100, 30))
        self.CBD_Cancel.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.CBD_Cancel.setObjectName("CBD_Cancel")
        self.horizontalLayout.addWidget(self.CBD_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogEAR)
        QtCore.QMetaObject.connectSlotsByName(DialogEAR)

    def retranslateUi(self, DialogEAR):
        _translate = QtCore.QCoreApplication.translate
        DialogEAR.setWindowTitle(_translate("DialogEAR", "Edit"))
        self.label_nume.setText(_translate("DialogEAR", "Nume"))
        self.label_prenume.setText(_translate("DialogEAR", "Prenume"))
        self.checkBoxDN.setText(_translate("DialogEAR", "Modificare data nastere"))
        self.label_dataNasterii.setText(_translate("DialogEAR", "Data nasterii"))
        self.comboBoxDA_luna.setItemText(0, _translate("DialogEAR", "(01) Ianuarie"))
        self.comboBoxDA_luna.setItemText(1, _translate("DialogEAR", "(02) Februarie"))
        self.comboBoxDA_luna.setItemText(2, _translate("DialogEAR", "(03) Martie"))
        self.comboBoxDA_luna.setItemText(3, _translate("DialogEAR", "(04) Aprilie"))
        self.comboBoxDA_luna.setItemText(4, _translate("DialogEAR", "(05) Mai"))
        self.comboBoxDA_luna.setItemText(5, _translate("DialogEAR", "(06) Iunie"))
        self.comboBoxDA_luna.setItemText(6, _translate("DialogEAR", "(07) Iulie"))
        self.comboBoxDA_luna.setItemText(7, _translate("DialogEAR", "(08) August"))
        self.comboBoxDA_luna.setItemText(8, _translate("DialogEAR", "(09) Septembrie"))
        self.comboBoxDA_luna.setItemText(9, _translate("DialogEAR", "(10) Octombrie"))
        self.comboBoxDA_luna.setItemText(10, _translate("DialogEAR", "(11) Noiembrie"))
        self.comboBoxDA_luna.setItemText(11, _translate("DialogEAR", "(12) Decembrie"))
        self.comboBoxDA_zi.setItemText(0, _translate("DialogEAR", "01"))
        self.comboBoxDA_zi.setItemText(1, _translate("DialogEAR", "02"))
        self.comboBoxDA_zi.setItemText(2, _translate("DialogEAR", "03"))
        self.comboBoxDA_zi.setItemText(3, _translate("DialogEAR", "04"))
        self.comboBoxDA_zi.setItemText(4, _translate("DialogEAR", "05"))
        self.comboBoxDA_zi.setItemText(5, _translate("DialogEAR", "06"))
        self.comboBoxDA_zi.setItemText(6, _translate("DialogEAR", "07"))
        self.comboBoxDA_zi.setItemText(7, _translate("DialogEAR", "08"))
        self.comboBoxDA_zi.setItemText(8, _translate("DialogEAR", "09"))
        self.comboBoxDA_zi.setItemText(9, _translate("DialogEAR", "10"))
        self.comboBoxDA_zi.setItemText(10, _translate("DialogEAR", "11"))
        self.comboBoxDA_zi.setItemText(11, _translate("DialogEAR", "12"))
        self.comboBoxDA_zi.setItemText(12, _translate("DialogEAR", "13"))
        self.comboBoxDA_zi.setItemText(13, _translate("DialogEAR", "14"))
        self.comboBoxDA_zi.setItemText(14, _translate("DialogEAR", "15"))
        self.comboBoxDA_zi.setItemText(15, _translate("DialogEAR", "16"))
        self.comboBoxDA_zi.setItemText(16, _translate("DialogEAR", "17"))
        self.comboBoxDA_zi.setItemText(17, _translate("DialogEAR", "18"))
        self.comboBoxDA_zi.setItemText(18, _translate("DialogEAR", "19"))
        self.comboBoxDA_zi.setItemText(19, _translate("DialogEAR", "20"))
        self.comboBoxDA_zi.setItemText(20, _translate("DialogEAR", "21"))
        self.comboBoxDA_zi.setItemText(21, _translate("DialogEAR", "22"))
        self.comboBoxDA_zi.setItemText(22, _translate("DialogEAR", "23"))
        self.comboBoxDA_zi.setItemText(23, _translate("DialogEAR", "24"))
        self.comboBoxDA_zi.setItemText(24, _translate("DialogEAR", "25"))
        self.comboBoxDA_zi.setItemText(25, _translate("DialogEAR", "26"))
        self.comboBoxDA_zi.setItemText(26, _translate("DialogEAR", "27"))
        self.comboBoxDA_zi.setItemText(27, _translate("DialogEAR", "28"))
        self.comboBoxDA_zi.setItemText(28, _translate("DialogEAR", "29"))
        self.comboBoxDA_zi.setItemText(29, _translate("DialogEAR", "30"))
        self.comboBoxDA_zi.setItemText(30, _translate("DialogEAR", "31"))
        self.CBD_OK.setText(_translate("DialogEAR", "OK"))
        self.CBD_Cancel.setText(_translate("DialogEAR", "Cancel"))
