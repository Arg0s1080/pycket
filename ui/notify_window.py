# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#
# (ɔ) Iván Rincón 2018

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NotifyDialog(object):
    def setupUi(self, NotifyDialog):
        NotifyDialog.setObjectName("NotifyDialog")
        NotifyDialog.resize(550, 350)
        NotifyDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout = QtWidgets.QGridLayout(NotifyDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelHeader = QtWidgets.QLabel(NotifyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHeader.sizePolicy().hasHeightForWidth())
        self.labelHeader.setSizePolicy(sizePolicy)
        self.labelHeader.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelHeader.setScaledContents(False)
        self.labelHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHeader.setObjectName("labelHeader")
        self.verticalLayout_2.addWidget(self.labelHeader)
        self.labelBody = QtWidgets.QLabel(NotifyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.labelBody.sizePolicy().hasHeightForWidth())
        self.labelBody.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelBody.setFont(font)
        self.labelBody.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBody.setScaledContents(True)
        self.labelBody.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBody.setWordWrap(True)
        self.labelBody.setOpenExternalLinks(True)
        self.labelBody.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.labelBody.setObjectName("labelBody")
        self.verticalLayout_2.addWidget(self.labelBody)
        self.pushButtonClose = QtWidgets.QPushButton(NotifyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonClose.sizePolicy().hasHeightForWidth())
        self.pushButtonClose.setSizePolicy(sizePolicy)
        self.pushButtonClose.setAutoRepeat(True)
        self.pushButtonClose.setObjectName("pushButtonClose")
        self.verticalLayout_2.addWidget(self.pushButtonClose)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(NotifyDialog)
        QtCore.QMetaObject.connectSlotsByName(NotifyDialog)

    def retranslateUi(self, NotifyDialog):
        _translate = QtCore.QCoreApplication.translate
        NotifyDialog.setWindowTitle(_translate("NotifyDialog", "Pycket - Notify"))
        self.labelHeader.setText(_translate("NotifyDialog", "Alarm"))
        self.labelBody.setText(_translate("NotifyDialog", "ALARM"))
        self.pushButtonClose.setText(_translate("NotifyDialog", "Close"))

