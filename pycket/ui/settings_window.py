# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# (ɔ) Iván Rincón 2019

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(350, 430)
        SettingsDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.gridLayout_3 = QtWidgets.QGridLayout(SettingsDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOk = QtWidgets.QPushButton(SettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOk.sizePolicy().hasHeightForWidth())
        self.pushButtonOk.setSizePolicy(sizePolicy)
        self.pushButtonOk.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtWidgets.QPushButton(SettingsDialog)
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(SettingsDialog)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tabActions = QtWidgets.QWidget()
        self.tabActions.setObjectName("tabActions")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabActions)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tabActions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelShutdown = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShutdown.sizePolicy().hasHeightForWidth())
        self.labelShutdown.setSizePolicy(sizePolicy)
        self.labelShutdown.setMinimumSize(QtCore.QSize(100, 0))
        self.labelShutdown.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelShutdown.setObjectName("labelShutdown")
        self.verticalLayout_5.addWidget(self.labelShutdown)
        self.labelReboot = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelReboot.sizePolicy().hasHeightForWidth())
        self.labelReboot.setSizePolicy(sizePolicy)
        self.labelReboot.setMinimumSize(QtCore.QSize(100, 0))
        self.labelReboot.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelReboot.setObjectName("labelReboot")
        self.verticalLayout_5.addWidget(self.labelReboot)
        self.labelCloseSession = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCloseSession.sizePolicy().hasHeightForWidth())
        self.labelCloseSession.setSizePolicy(sizePolicy)
        self.labelCloseSession.setMinimumSize(QtCore.QSize(100, 0))
        self.labelCloseSession.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelCloseSession.setObjectName("labelCloseSession")
        self.verticalLayout_5.addWidget(self.labelCloseSession)
        self.LockScreen = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LockScreen.sizePolicy().hasHeightForWidth())
        self.LockScreen.setSizePolicy(sizePolicy)
        self.LockScreen.setMinimumSize(QtCore.QSize(100, 0))
        self.LockScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.LockScreen.setObjectName("LockScreen")
        self.verticalLayout_5.addWidget(self.LockScreen)
        self.labelSuspend = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSuspend.sizePolicy().hasHeightForWidth())
        self.labelSuspend.setSizePolicy(sizePolicy)
        self.labelSuspend.setMinimumSize(QtCore.QSize(100, 0))
        self.labelSuspend.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelSuspend.setObjectName("labelSuspend")
        self.verticalLayout_5.addWidget(self.labelSuspend)
        self.labelHibernate = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHibernate.sizePolicy().hasHeightForWidth())
        self.labelHibernate.setSizePolicy(sizePolicy)
        self.labelHibernate.setMinimumSize(QtCore.QSize(100, 0))
        self.labelHibernate.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelHibernate.setObjectName("labelHibernate")
        self.verticalLayout_5.addWidget(self.labelHibernate)
        self.labelExecute = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelExecute.sizePolicy().hasHeightForWidth())
        self.labelExecute.setSizePolicy(sizePolicy)
        self.labelExecute.setMinimumSize(QtCore.QSize(100, 0))
        self.labelExecute.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.labelExecute.setObjectName("labelExecute")
        self.verticalLayout_5.addWidget(self.labelExecute)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEditShutdown = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditShutdown.sizePolicy().hasHeightForWidth())
        self.lineEditShutdown.setSizePolicy(sizePolicy)
        self.lineEditShutdown.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditShutdown.setText("")
        self.lineEditShutdown.setObjectName("lineEditShutdown")
        self.verticalLayout_6.addWidget(self.lineEditShutdown)
        self.lineEditReboot = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditReboot.sizePolicy().hasHeightForWidth())
        self.lineEditReboot.setSizePolicy(sizePolicy)
        self.lineEditReboot.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditReboot.setText("")
        self.lineEditReboot.setObjectName("lineEditReboot")
        self.verticalLayout_6.addWidget(self.lineEditReboot)
        self.lineEditCloseSession = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditCloseSession.sizePolicy().hasHeightForWidth())
        self.lineEditCloseSession.setSizePolicy(sizePolicy)
        self.lineEditCloseSession.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditCloseSession.setText("")
        self.lineEditCloseSession.setObjectName("lineEditCloseSession")
        self.verticalLayout_6.addWidget(self.lineEditCloseSession)
        self.lineEditLockScreen = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditLockScreen.sizePolicy().hasHeightForWidth())
        self.lineEditLockScreen.setSizePolicy(sizePolicy)
        self.lineEditLockScreen.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditLockScreen.setText("")
        self.lineEditLockScreen.setObjectName("lineEditLockScreen")
        self.verticalLayout_6.addWidget(self.lineEditLockScreen)
        self.lineEditSuspend = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSuspend.sizePolicy().hasHeightForWidth())
        self.lineEditSuspend.setSizePolicy(sizePolicy)
        self.lineEditSuspend.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditSuspend.setText("")
        self.lineEditSuspend.setObjectName("lineEditSuspend")
        self.verticalLayout_6.addWidget(self.lineEditSuspend)
        self.lineEditHibernate = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHibernate.sizePolicy().hasHeightForWidth())
        self.lineEditHibernate.setSizePolicy(sizePolicy)
        self.lineEditHibernate.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditHibernate.setText("")
        self.lineEditHibernate.setObjectName("lineEditHibernate")
        self.verticalLayout_6.addWidget(self.lineEditHibernate)
        self.lineEditExecute = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditExecute.sizePolicy().hasHeightForWidth())
        self.lineEditExecute.setSizePolicy(sizePolicy)
        self.lineEditExecute.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditExecute.setText("")
        self.lineEditExecute.setObjectName("lineEditExecute")
        self.verticalLayout_6.addWidget(self.lineEditExecute)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabActions, "")
        self.tabMiscellaneous = QtWidgets.QWidget()
        self.tabMiscellaneous.setObjectName("tabMiscellaneous")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabMiscellaneous)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelQtStyle = QtWidgets.QLabel(self.tabMiscellaneous)
        self.labelQtStyle.setObjectName("labelQtStyle")
        self.horizontalLayout_8.addWidget(self.labelQtStyle)
        self.comboBoxStyle = QtWidgets.QComboBox(self.tabMiscellaneous)
        self.comboBoxStyle.setObjectName("comboBoxStyle")
        self.horizontalLayout_8.addWidget(self.comboBoxStyle)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelDateTimeEditFormat = QtWidgets.QLabel(self.tabMiscellaneous)
        self.labelDateTimeEditFormat.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelDateTimeEditFormat.setObjectName("labelDateTimeEditFormat")
        self.horizontalLayout_9.addWidget(self.labelDateTimeEditFormat)
        self.lineEditDateTimeEditFormat = QtWidgets.QLineEdit(self.tabMiscellaneous)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDateTimeEditFormat.sizePolicy().hasHeightForWidth())
        self.lineEditDateTimeEditFormat.setSizePolicy(sizePolicy)
        self.lineEditDateTimeEditFormat.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditDateTimeEditFormat.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEditDateTimeEditFormat.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEditDateTimeEditFormat.setText("")
        self.lineEditDateTimeEditFormat.setObjectName("lineEditDateTimeEditFormat")
        self.horizontalLayout_9.addWidget(self.lineEditDateTimeEditFormat)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelTempScale = QtWidgets.QLabel(self.tabMiscellaneous)
        self.labelTempScale.setObjectName("labelTempScale")
        self.horizontalLayout_10.addWidget(self.labelTempScale)
        self.comboBoxTempScale = QtWidgets.QComboBox(self.tabMiscellaneous)
        self.comboBoxTempScale.setCurrentText("Celsius")
        self.comboBoxTempScale.setObjectName("comboBoxTempScale")
        self.comboBoxTempScale.addItem("")
        self.comboBoxTempScale.setItemText(0, "Celsius")
        self.comboBoxTempScale.addItem("")
        self.comboBoxTempScale.setItemText(1, "Fahrenheit")
        self.comboBoxTempScale.addItem("")
        self.comboBoxTempScale.setItemText(2, "Kelvin")
        self.comboBoxTempScale.addItem("")
        self.comboBoxTempScale.setItemText(3, "Rankine")
        self.horizontalLayout_10.addWidget(self.comboBoxTempScale)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 0, 1, 2)
        self.checkBoxProgressbarText = QtWidgets.QCheckBox(self.tabMiscellaneous)
        self.checkBoxProgressbarText.setObjectName("checkBoxProgressbarText")
        self.gridLayout_2.addWidget(self.checkBoxProgressbarText, 1, 0, 1, 2)
        self.checkBoxAlwaysOnTop = QtWidgets.QCheckBox(self.tabMiscellaneous)
        self.checkBoxAlwaysOnTop.setObjectName("checkBoxAlwaysOnTop")
        self.gridLayout_2.addWidget(self.checkBoxAlwaysOnTop, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonNotify = QtWidgets.QPushButton(self.tabMiscellaneous)
        self.pushButtonNotify.setObjectName("pushButtonNotify")
        self.horizontalLayout_2.addWidget(self.pushButtonNotify)
        self.pushButtonSendMail = QtWidgets.QPushButton(self.tabMiscellaneous)
        self.pushButtonSendMail.setObjectName("pushButtonSendMail")
        self.horizontalLayout_2.addWidget(self.pushButtonSendMail)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tabMiscellaneous, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Pycket Settings"))
        self.pushButtonOk.setText(_translate("SettingsDialog", "Ok"))
        self.pushButtonCancel.setText(_translate("SettingsDialog", "Cancel"))
        self.groupBox.setTitle(_translate("SettingsDialog", "Commands"))
        self.labelShutdown.setText(_translate("SettingsDialog", "Shutdown"))
        self.labelReboot.setText(_translate("SettingsDialog", "Reboot"))
        self.labelCloseSession.setText(_translate("SettingsDialog", "Close Session"))
        self.LockScreen.setText(_translate("SettingsDialog", "Lock Screen"))
        self.labelSuspend.setText(_translate("SettingsDialog", "Suspend"))
        self.labelHibernate.setText(_translate("SettingsDialog", "Hibernate"))
        self.labelExecute.setText(_translate("SettingsDialog", "Execute"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabActions), _translate("SettingsDialog", "Actions"))
        self.labelQtStyle.setText(_translate("SettingsDialog", "Qt Style"))
        self.labelDateTimeEditFormat.setText(_translate("SettingsDialog", "DateTimeEdit format"))
        self.labelTempScale.setText(_translate("SettingsDialog", "Temperature scale"))
        self.checkBoxProgressbarText.setText(_translate("SettingsDialog", "Text visible in progressbar"))
        self.checkBoxAlwaysOnTop.setText(_translate("SettingsDialog", "Always on top"))
        self.pushButtonNotify.setText(_translate("SettingsDialog", "Notify"))
        self.pushButtonSendMail.setText(_translate("SettingsDialog", "Send Mail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMiscellaneous), _translate("SettingsDialog", "Misc."))

