# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#
# (ɔ) Iván Rincón 2018

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setObjectName("tabWidget")
        self.tabActions = QtWidgets.QWidget()
        self.tabActions.setObjectName("tabActions")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabActions)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
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
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.tabActions)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.tabActions)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tabActions, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelQtStyle = QtWidgets.QLabel(self.tab_4)
        self.labelQtStyle.setObjectName("labelQtStyle")
        self.horizontalLayout_8.addWidget(self.labelQtStyle)
        self.comboBoxStyle = QtWidgets.QComboBox(self.tab_4)
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
        self.labelDateTimeEditFormat = QtWidgets.QLabel(self.tab_4)
        self.labelDateTimeEditFormat.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelDateTimeEditFormat.setObjectName("labelDateTimeEditFormat")
        self.horizontalLayout_9.addWidget(self.labelDateTimeEditFormat)
        self.lineEditDateTimeEditFormat = QtWidgets.QLineEdit(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDateTimeEditFormat.sizePolicy().hasHeightForWidth())
        self.lineEditDateTimeEditFormat.setSizePolicy(sizePolicy)
        self.lineEditDateTimeEditFormat.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEditDateTimeEditFormat.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEditDateTimeEditFormat.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEditDateTimeEditFormat.setObjectName("lineEditDateTimeEditFormat")
        self.horizontalLayout_9.addWidget(self.lineEditDateTimeEditFormat)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelTempScale = QtWidgets.QLabel(self.tab_4)
        self.labelTempScale.setObjectName("labelTempScale")
        self.horizontalLayout_10.addWidget(self.labelTempScale)
        self.comboBoxTempScale = QtWidgets.QComboBox(self.tab_4)
        self.comboBoxTempScale.setObjectName("comboBoxTempScale")
        self.comboBoxTempScale.addItem("")
        self.comboBoxTempScale.addItem("")
        self.comboBoxTempScale.addItem("")
        self.comboBoxTempScale.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBoxTempScale)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.checkBoxTextVisibleProgressbar = QtWidgets.QCheckBox(self.tab_4)
        self.checkBoxTextVisibleProgressbar.setObjectName("checkBoxTextVisibleProgressbar")
        self.gridLayout_2.addWidget(self.checkBoxTextVisibleProgressbar, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOk = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOk.sizePolicy().hasHeightForWidth())
        self.pushButtonOk.setSizePolicy(sizePolicy)
        self.pushButtonOk.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonApply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonApply.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonApply.setObjectName("pushButtonApply")
        self.horizontalLayout.addWidget(self.pushButtonApply)
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Commands"))
        self.labelShutdown.setText(_translate("MainWindow", "Shutdown"))
        self.labelReboot.setText(_translate("MainWindow", "Reboot"))
        self.labelCloseSession.setText(_translate("MainWindow", "Close Session"))
        self.LockScreen.setText(_translate("MainWindow", "Lock Screen"))
        self.labelSuspend.setText(_translate("MainWindow", "Suspend"))
        self.labelHibernate.setText(_translate("MainWindow", "Hibernate"))
        self.labelExecute.setText(_translate("MainWindow", "Execute"))
        self.lineEditLockScreen.setText(_translate("MainWindow", "systemctl hybrid-sleep"))
        self.pushButton.setText(_translate("MainWindow", "Notify"))
        self.pushButton_2.setText(_translate("MainWindow", "Send Mail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabActions), _translate("MainWindow", "Actions"))
        self.labelQtStyle.setText(_translate("MainWindow", "Qt Style"))
        self.labelDateTimeEditFormat.setText(_translate("MainWindow", "DateTimeEdit format"))
        self.lineEditDateTimeEditFormat.setText(_translate("MainWindow", "yyyy/MM/dd hh:mm:ss"))
        self.labelTempScale.setText(_translate("MainWindow", "Temperature scale"))
        self.comboBoxTempScale.setItemText(0, _translate("MainWindow", "Celsius"))
        self.comboBoxTempScale.setItemText(1, _translate("MainWindow", "Fahrenheit"))
        self.comboBoxTempScale.setItemText(2, _translate("MainWindow", "Kelvin"))
        self.comboBoxTempScale.setItemText(3, _translate("MainWindow", "Rankine"))
        self.checkBoxTextVisibleProgressbar.setText(_translate("MainWindow", "Text visible in progressbar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.pushButtonOk.setText(_translate("MainWindow", "Ok"))
        self.pushButtonApply.setText(_translate("MainWindow", "Apply"))
        self.pushButtonCancel.setText(_translate("MainWindow", "Cancel"))

