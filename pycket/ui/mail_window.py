# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# (ɔ) Iván Rincón 2018

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MailDialog(object):
    def setupUi(self, MailDialog):
        MailDialog.setObjectName("MailDialog")
        MailDialog.resize(769, 514)
        MailDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtWidgets.QGridLayout(MailDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.labelFrom = QtWidgets.QLabel(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelFrom.setFont(font)
        self.labelFrom.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelFrom.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFrom.setObjectName("labelFrom")
        self.gridLayout.addWidget(self.labelFrom, 0, 0, 1, 2)
        self.lineEditFrom = QtWidgets.QLineEdit(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditFrom.setFont(font)
        self.lineEditFrom.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditFrom.setClearButtonEnabled(True)
        self.lineEditFrom.setObjectName("lineEditFrom")
        self.gridLayout.addWidget(self.lineEditFrom, 0, 2, 1, 3)
        self.labelAlias = QtWidgets.QLabel(MailDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAlias.sizePolicy().hasHeightForWidth())
        self.labelAlias.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelAlias.setFont(font)
        self.labelAlias.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelAlias.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAlias.setObjectName("labelAlias")
        self.gridLayout.addWidget(self.labelAlias, 0, 5, 1, 1)
        self.lineEditAlias = QtWidgets.QLineEdit(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditAlias.setFont(font)
        self.lineEditAlias.setClearButtonEnabled(True)
        self.lineEditAlias.setObjectName("lineEditAlias")
        self.gridLayout.addWidget(self.lineEditAlias, 0, 6, 1, 3)
        self.labelServer = QtWidgets.QLabel(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelServer.setFont(font)
        self.labelServer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelServer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelServer.setObjectName("labelServer")
        self.gridLayout.addWidget(self.labelServer, 1, 0, 1, 2)
        self.lineEditServer = QtWidgets.QLineEdit(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditServer.setFont(font)
        self.lineEditServer.setClearButtonEnabled(True)
        self.lineEditServer.setObjectName("lineEditServer")
        self.gridLayout.addWidget(self.lineEditServer, 1, 2, 1, 1)
        self.labelServer_2 = QtWidgets.QLabel(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelServer_2.setFont(font)
        self.labelServer_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelServer_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelServer_2.setObjectName("labelServer_2")
        self.gridLayout.addWidget(self.labelServer_2, 1, 3, 1, 1)
        self.lineEditPassword = QtWidgets.QLineEdit(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setClearButtonEnabled(True)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 1, 4, 1, 2)
        self.comboBoxEncrypt = QtWidgets.QComboBox(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBoxEncrypt.setFont(font)
        self.comboBoxEncrypt.setCurrentText("TSL")
        self.comboBoxEncrypt.setObjectName("comboBoxEncrypt")
        self.comboBoxEncrypt.addItem("")
        self.comboBoxEncrypt.setItemText(0, "TSL")
        self.comboBoxEncrypt.addItem("")
        self.comboBoxEncrypt.setItemText(1, "SSL")
        self.comboBoxEncrypt.addItem("")
        self.comboBoxEncrypt.setItemText(2, "NONE")
        self.gridLayout.addWidget(self.comboBoxEncrypt, 1, 6, 1, 1)
        self.labelPort = QtWidgets.QLabel(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelPort.setFont(font)
        self.labelPort.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelPort.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPort.setObjectName("labelPort")
        self.gridLayout.addWidget(self.labelPort, 1, 7, 1, 1)
        self.spinBoxPort = QtWidgets.QSpinBox(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBoxPort.setFont(font)
        self.spinBoxPort.setMaximum(65536)
        self.spinBoxPort.setProperty("value", 587)
        self.spinBoxPort.setObjectName("spinBoxPort")
        self.gridLayout.addWidget(self.spinBoxPort, 1, 8, 1, 1)
        self.lineEditTo = QtWidgets.QLineEdit(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditTo.setFont(font)
        self.lineEditTo.setClearButtonEnabled(True)
        self.lineEditTo.setObjectName("lineEditTo")
        self.gridLayout.addWidget(self.lineEditTo, 2, 2, 1, 7)
        self.labelSubject = QtWidgets.QLabel(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelSubject.setFont(font)
        self.labelSubject.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelSubject.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSubject.setObjectName("labelSubject")
        self.gridLayout.addWidget(self.labelSubject, 3, 0, 1, 2)
        self.lineEditSubject = QtWidgets.QLineEdit(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEditSubject.setFont(font)
        self.lineEditSubject.setClearButtonEnabled(True)
        self.lineEditSubject.setObjectName("lineEditSubject")
        self.gridLayout.addWidget(self.lineEditSubject, 3, 2, 1, 6)
        self.pushButtonAttach = QtWidgets.QPushButton(MailDialog)
        self.pushButtonAttach.setObjectName("pushButtonAttach")
        self.gridLayout.addWidget(self.pushButtonAttach, 3, 8, 1, 1)
        self.labelBody = QtWidgets.QLabel(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelBody.setFont(font)
        self.labelBody.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelBody.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBody.setObjectName("labelBody")
        self.gridLayout.addWidget(self.labelBody, 4, 0, 1, 2)
        self.plainTextEditBody = QtWidgets.QPlainTextEdit(MailDialog)
        self.plainTextEditBody.setObjectName("plainTextEditBody")
        self.gridLayout.addWidget(self.plainTextEditBody, 4, 2, 1, 7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOk = QtWidgets.QPushButton(MailDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOk.sizePolicy().hasHeightForWidth())
        self.pushButtonOk.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonOk.setFont(font)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtWidgets.QPushButton(MailDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCancel.sizePolicy().hasHeightForWidth())
        self.pushButtonCancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonTest = QtWidgets.QPushButton(MailDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonTest.sizePolicy().hasHeightForWidth())
        self.pushButtonTest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonTest.setFont(font)
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.horizontalLayout.addWidget(self.pushButtonTest)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 2, 1, 7)
        self.labelTo = QtWidgets.QLabel(MailDialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelTo.setFont(font)
        self.labelTo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTo.setObjectName("labelTo")
        self.gridLayout.addWidget(self.labelTo, 2, 0, 1, 2)

        self.retranslateUi(MailDialog)
        QtCore.QMetaObject.connectSlotsByName(MailDialog)

    def retranslateUi(self, MailDialog):
        _translate = QtCore.QCoreApplication.translate
        MailDialog.setWindowTitle(_translate("MailDialog", "Pycket - SMPT Mail Settings "))
        self.labelFrom.setText(_translate("MailDialog", "From:"))
        self.labelAlias.setText(_translate("MailDialog", "Alias:"))
        self.labelServer.setText(_translate("MailDialog", "Server:"))
        self.lineEditServer.setText(_translate("MailDialog", "smpt.gmail.com"))
        self.labelServer_2.setText(_translate("MailDialog", "Password:"))
        self.labelPort.setText(_translate("MailDialog", "Port:"))
        self.labelSubject.setText(_translate("MailDialog", "Subject:"))
        self.pushButtonAttach.setText(_translate("MailDialog", "Attach"))
        self.labelBody.setText(_translate("MailDialog", "Body:"))
        self.pushButtonOk.setText(_translate("MailDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("MailDialog", "Cancel"))
        self.pushButtonTest.setText(_translate("MailDialog", "Test"))
        self.labelTo.setText(_translate("MailDialog", "To:"))

