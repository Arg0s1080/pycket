# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#
# (ɔ) Iván Rincón 2018

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NotifySettingsDialog(object):
    def setupUi(self, NotifySettingsDialog):
        NotifySettingsDialog.setObjectName("NotifySettingsDialog")
        NotifySettingsDialog.resize(475, 600)
        NotifySettingsDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout_4 = QtWidgets.QGridLayout(NotifySettingsDialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonOk = QtWidgets.QPushButton(NotifySettingsDialog)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout_2.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtWidgets.QPushButton(NotifySettingsDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.pushButtonTest = QtWidgets.QPushButton(NotifySettingsDialog)
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.horizontalLayout_2.addWidget(self.pushButtonTest)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.groupBoxText = QtWidgets.QGroupBox(NotifySettingsDialog)
        self.groupBoxText.setObjectName("groupBoxText")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxText)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fontComboBoxHeader = QtWidgets.QFontComboBox(self.groupBoxText)
        self.fontComboBoxHeader.setEditable(False)
        self.fontComboBoxHeader.setObjectName("fontComboBoxHeader")
        self.horizontalLayout_9.addWidget(self.fontComboBoxHeader)
        self.labelSizeFontHeader = QtWidgets.QLabel(self.groupBoxText)
        self.labelSizeFontHeader.setObjectName("labelSizeFontHeader")
        self.horizontalLayout_9.addWidget(self.labelSizeFontHeader)
        self.spinBoxSizeFontHeader = QtWidgets.QSpinBox(self.groupBoxText)
        self.spinBoxSizeFontHeader.setSuffix("")
        self.spinBoxSizeFontHeader.setProperty("value", 10)
        self.spinBoxSizeFontHeader.setObjectName("spinBoxSizeFontHeader")
        self.horizontalLayout_9.addWidget(self.spinBoxSizeFontHeader)
        self.checkBoxBoldHeader = QtWidgets.QCheckBox(self.groupBoxText)
        self.checkBoxBoldHeader.setObjectName("checkBoxBoldHeader")
        self.horizontalLayout_9.addWidget(self.checkBoxBoldHeader)
        self.checkBoxItalicHeader = QtWidgets.QCheckBox(self.groupBoxText)
        self.checkBoxItalicHeader.setObjectName("checkBoxItalicHeader")
        self.horizontalLayout_9.addWidget(self.checkBoxItalicHeader)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.lineEditHeader = QtWidgets.QLineEdit(self.groupBoxText)
        self.lineEditHeader.setObjectName("lineEditHeader")
        self.gridLayout_3.addWidget(self.lineEditHeader, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fontComboBoxBody = QtWidgets.QFontComboBox(self.groupBoxText)
        self.fontComboBoxBody.setEditable(False)
        self.fontComboBoxBody.setObjectName("fontComboBoxBody")
        self.horizontalLayout_6.addWidget(self.fontComboBoxBody)
        self.labelSizeFontBody = QtWidgets.QLabel(self.groupBoxText)
        self.labelSizeFontBody.setObjectName("labelSizeFontBody")
        self.horizontalLayout_6.addWidget(self.labelSizeFontBody)
        self.spinBoxSizeFontBody = QtWidgets.QSpinBox(self.groupBoxText)
        self.spinBoxSizeFontBody.setSuffix("")
        self.spinBoxSizeFontBody.setProperty("value", 14)
        self.spinBoxSizeFontBody.setObjectName("spinBoxSizeFontBody")
        self.horizontalLayout_6.addWidget(self.spinBoxSizeFontBody)
        self.checkBoxBoldBody = QtWidgets.QCheckBox(self.groupBoxText)
        self.checkBoxBoldBody.setObjectName("checkBoxBoldBody")
        self.horizontalLayout_6.addWidget(self.checkBoxBoldBody)
        self.checkBoxItalicBody = QtWidgets.QCheckBox(self.groupBoxText)
        self.checkBoxItalicBody.setObjectName("checkBoxItalicBody")
        self.horizontalLayout_6.addWidget(self.checkBoxItalicBody)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.plainTextEditBody = QtWidgets.QPlainTextEdit(self.groupBoxText)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEditBody.setFont(font)
        self.plainTextEditBody.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.plainTextEditBody.setObjectName("plainTextEditBody")
        self.gridLayout_3.addWidget(self.plainTextEditBody, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxText, 1, 0, 1, 1)
        self.groupBoxGeneral = QtWidgets.QGroupBox(NotifySettingsDialog)
        self.groupBoxGeneral.setObjectName("groupBoxGeneral")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxGeneral)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBoxSecondsClose = QtWidgets.QSpinBox(self.groupBoxGeneral)
        self.spinBoxSecondsClose.setObjectName("spinBoxSecondsClose")
        self.gridLayout.addWidget(self.spinBoxSecondsClose, 2, 2, 1, 1)
        self.checkBoxShowTime = QtWidgets.QCheckBox(self.groupBoxGeneral)
        self.checkBoxShowTime.setObjectName("checkBoxShowTime")
        self.gridLayout.addWidget(self.checkBoxShowTime, 3, 0, 1, 1)
        self.checkBoxAlwaysOnTop = QtWidgets.QCheckBox(self.groupBoxGeneral)
        self.checkBoxAlwaysOnTop.setObjectName("checkBoxAlwaysOnTop")
        self.gridLayout.addWidget(self.checkBoxAlwaysOnTop, 1, 0, 1, 1)
        self.checkBoxCloseAuto = QtWidgets.QCheckBox(self.groupBoxGeneral)
        self.checkBoxCloseAuto.setObjectName("checkBoxCloseAuto")
        self.gridLayout.addWidget(self.checkBoxCloseAuto, 2, 0, 1, 1)
        self.checkBoxPlaySound = QtWidgets.QCheckBox(self.groupBoxGeneral)
        self.checkBoxPlaySound.setObjectName("checkBoxPlaySound")
        self.gridLayout.addWidget(self.checkBoxPlaySound, 4, 0, 1, 1)
        self.comboBoxSounds = QtWidgets.QComboBox(self.groupBoxGeneral)
        self.comboBoxSounds.setObjectName("comboBoxSounds")
        self.gridLayout.addWidget(self.comboBoxSounds, 4, 2, 1, 1)
        self.labelOpacity = QtWidgets.QLabel(self.groupBoxGeneral)
        self.labelOpacity.setObjectName("labelOpacity")
        self.gridLayout.addWidget(self.labelOpacity, 5, 0, 1, 1)
        self.doubleSpinBoxOpacity = QtWidgets.QDoubleSpinBox(self.groupBoxGeneral)
        self.doubleSpinBoxOpacity.setMaximum(100.0)
        self.doubleSpinBoxOpacity.setProperty("value", 100.0)
        self.doubleSpinBoxOpacity.setObjectName("doubleSpinBoxOpacity")
        self.gridLayout.addWidget(self.doubleSpinBoxOpacity, 5, 2, 1, 1)
        self.checkBoxInLoop = QtWidgets.QCheckBox(self.groupBoxGeneral)
        self.checkBoxInLoop.setObjectName("checkBoxInLoop")
        self.gridLayout.addWidget(self.checkBoxInLoop, 4, 4, 1, 1)
        self.pushButtonPlaySound = QtWidgets.QPushButton(self.groupBoxGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonPlaySound.sizePolicy().hasHeightForWidth())
        self.pushButtonPlaySound.setSizePolicy(sizePolicy)
        self.pushButtonPlaySound.setMaximumSize(QtCore.QSize(35, 16777215))
        self.pushButtonPlaySound.setObjectName("pushButtonPlaySound")
        self.gridLayout.addWidget(self.pushButtonPlaySound, 4, 3, 1, 1)
        self.labelPercent = QtWidgets.QLabel(self.groupBoxGeneral)
        self.labelPercent.setObjectName("labelPercent")
        self.gridLayout.addWidget(self.labelPercent, 5, 3, 1, 1)
        self.labelSeconds = QtWidgets.QLabel(self.groupBoxGeneral)
        self.labelSeconds.setObjectName("labelSeconds")
        self.gridLayout.addWidget(self.labelSeconds, 2, 3, 1, 1)
        self.lineEditTimeFormat = QtWidgets.QLineEdit(self.groupBoxGeneral)
        self.lineEditTimeFormat.setObjectName("lineEditTimeFormat")
        self.gridLayout.addWidget(self.lineEditTimeFormat, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBoxGeneral, 0, 0, 1, 1)

        self.retranslateUi(NotifySettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(NotifySettingsDialog)

    def retranslateUi(self, NotifySettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        NotifySettingsDialog.setWindowTitle(_translate("NotifySettingsDialog", "Dialog"))
        self.pushButtonOk.setText(_translate("NotifySettingsDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("NotifySettingsDialog", "Cancel"))
        self.pushButtonTest.setText(_translate("NotifySettingsDialog", "Test"))
        self.groupBoxText.setTitle(_translate("NotifySettingsDialog", "Text"))
        self.labelSizeFontHeader.setText(_translate("NotifySettingsDialog", "Size"))
        self.checkBoxBoldHeader.setText(_translate("NotifySettingsDialog", "Bold"))
        self.checkBoxItalicHeader.setText(_translate("NotifySettingsDialog", "Italic"))
        self.lineEditHeader.setPlaceholderText(_translate("NotifySettingsDialog", "Header"))
        self.labelSizeFontBody.setText(_translate("NotifySettingsDialog", "Size"))
        self.checkBoxBoldBody.setText(_translate("NotifySettingsDialog", "Bold"))
        self.checkBoxItalicBody.setText(_translate("NotifySettingsDialog", "Italic"))
        self.plainTextEditBody.setPlainText(_translate("NotifySettingsDialog", "ALARM"))
        self.plainTextEditBody.setPlaceholderText(_translate("NotifySettingsDialog", "Body"))
        self.groupBoxGeneral.setTitle(_translate("NotifySettingsDialog", "General"))
        self.checkBoxShowTime.setText(_translate("NotifySettingsDialog", "Show time in header"))
        self.checkBoxAlwaysOnTop.setText(_translate("NotifySettingsDialog", "Always on top"))
        self.checkBoxCloseAuto.setText(_translate("NotifySettingsDialog", "Close dialog automatically"))
        self.checkBoxPlaySound.setText(_translate("NotifySettingsDialog", "Play sound"))
        self.labelOpacity.setText(_translate("NotifySettingsDialog", "Opacity"))
        self.checkBoxInLoop.setText(_translate("NotifySettingsDialog", "in loop"))
        self.pushButtonPlaySound.setText(_translate("NotifySettingsDialog", "▶"))
        self.labelPercent.setText(_translate("NotifySettingsDialog", "%"))
        self.labelSeconds.setText(_translate("NotifySettingsDialog", "seconds"))
        self.lineEditTimeFormat.setText(_translate("NotifySettingsDialog", "hh:mm:ss"))

