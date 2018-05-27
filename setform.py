#!/usr/bin/python
# -*- coding: utf-8 -*-

#import os
import sys

from os import makedirs, getcwd
from os.path import join, exists
from configparser import ConfigParser
from ui.main_window import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer
from enums import *
from statux.net import get_interfaces
from statux.ram import used_percent, available_percent
from statux.cpu import cpu_load
from statux.thermald import x86_pkg_temp

config_file = join(getcwd(), "config.cfg")


class SetForm(QtWidgets.QMainWindow):
    # <editor-fold desc=" Init and close "
    def __init__(self):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_SetForm()
        self.ui.setupUi(self)

        # Section: Variables
        self.delay = 0
        self.action = Action.Shutdown
        self.condition = Condition.AtTime

        # Section: Declarations
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.config = ConfigParser()
        self.set_config()
        self.set_sys_load()

        # Section: Widgets parameters
        # self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime().addSecs(10))  # TODO Change addSecs
        self.ui.radioButtonExecute.checkStateSet()
        self.ui.comboBoxNetworkAdapter.addItems(get_interfaces())

        # Section: Events
        self.ui.pushButtonStart.clicked.connect(self.pushbutton_start_clicked)
        self.ui.pushButtonPause.clicked.connect(self.pushbutton_pause_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.pushbutton_cancel_clicked)
        self.ui.dateTimeEdit.dateTimeChanged.connect(self.datetime_edit_changed)
        self.ui.spinBoxHours.valueChanged.connect(self.spinbox_hours_value_changed)
        self.ui.spinBoxMinutes.valueChanged.connect(self.spinbox_minutes_value_changed)
        self.ui.spinBoxSeconds.valueChanged.connect(self.spinbox_seconds_value_changed)
        self.ui.buttonGroupActions.buttonClicked.connect(self.button_group_actions_clicked)
        self.ui.buttonGroupSystemLoad.buttonClicked.connect(self.button_group_sys_load_clicked)
        self.ui.tabWidget.currentChanged.connect(self.tab_widget_changed)
        self.ui.comboBoxSystemLoad.currentIndexChanged.connect(self.combo_sl_index_changed)
        self.ui.spinBoxSystemLoadMinutes.valueChanged.connect(self.spinbox_minutes_sl_value_changed)
        self.ui.spinBoxSystemLoadUnit.valueChanged.connect(self.spinbox_unit_sl_value_changed)
        self.timer1.timeout.connect(self.timer1_tick)
        self.timer2.timeout.connect(self.timer_sl_tick)

    # TEST
    def test_event(self):
        print("TEST EVENT")

    def set_config(self):
        if exists(config_file):
            self.config.read(config_file)

            # Section: Main
            self.action = Action[self.config.get("Main", "actions")]
            if self.action == Action.Shutdown:
                self.ui.radioButtonShutdown.setChecked(True)
            elif self.action == Action.Reboot:
                self.ui.radioButtonReboot.setChecked(True)
            elif self.action == Action.CloseSession:
                self.ui.radioButtonCloseSesion.setChecked(True)
            elif self.action == Action.Lock:
                self.ui.radioButtonLock.setChecked(True)
            elif self.action == Action.Suspend:
                self.ui.radioButtonSuspend.setChecked(True)
            elif self.action == Action.Hibernate:
                self.ui.radioButtonHibernate.setChecked(True)
            elif self.action == Action.Notify:
                self.ui.radioButtonNotify.setChecked(True)
            elif self.action == Action.Execute:
                self.ui.radioButtonExecute.setChecked(True)
            else:
                self.ui.radioButtonSendMail.setChecked(True)

            self.condition = Condition[self.config.get("Main", "conditions")]
            if self.condition == Condition.AtTime:
                self.ui.tabWidget.setCurrentIndex(0)
            elif self.condition == Condition.Countdown:
                self.ui.tabWidget.setCurrentIndex(1)
            elif self.condition == Condition.SystemLoad:
                self.ui.tabWidget.setCurrentIndex(2)
            elif self.condition == Condition.Network:
                self.ui.tabWidget.setCurrentIndex(3)
            elif self.condition == Condition.Power:
                self.ui.tabWidget.setCurrentIndex(4)
            elif self.condition == Condition.Drives:
                self.ui.tabWidget.setCurrentIndex(5)

            # Section: SystemLoad
            d = QDateTime.fromString(self.config.get("AtTime", "date_time"), "yyyy/MM/dd hh:mm:ss")
            self.ui.dateTimeEdit.setDateTime(d)

            # Section: CountDown
            self.ui.spinBoxHours.setValue(self.config.getint("CountDown", "hours"))
            self.ui.spinBoxMinutes.setValue(self.config.getint("CountDown", "minutes"))
            self.ui.spinBoxSeconds.setValue(self.config.getint("CountDown", "seconds"))

            # Section SystemLoad
            sli = int(self.config.get("SystemLoad", "group_index"))
            if sli == 0:
                self.ui.radioButtonLoadRAMUsed.setChecked(True)
            elif sli == 1:
                self.ui.radioButtonLoadRAMAvailable.setChecked(True)
            elif sli == 2:
                self.ui.radioButtonLoadCPU.setChecked(True)
            else:
                self.ui.radioButtonCPUTemp.setChecked(True)
            self.ui.comboBoxSystemLoad.setCurrentIndex(self.config.getboolean("SystemLoad", "combo"))
            self.ui.spinBoxSystemLoadMinutes.setValue(self.config.getint("SystemLoad", "spin_min"))
            self.ui.spinBoxSystemLoadUnit.setValue(self.config.getint("SystemLoad", "spin_unit"))
        else:
            folder = config_file.replace("config.cfg", "")
            if not exists(folder):
                makedirs(folder)

            self.config.add_section("Main")
            self.config.set("Main", "actions", "Shutdown")
            self.config.set("Main", "conditions", "AtTime")
            self.config.add_section("AtTime")
            self.config.set("AtTime", "date_time",
                            QDateTime.currentDateTime().addSecs(3600).toString("yyyy/MM/dd hh:mm:ss"))
            self.config.add_section("CountDown")
            self.config.set("CountDown", "hours", "0")
            self.config.set("CountDown", "minutes", "0")
            self.config.set("CountDown", "seconds", "0")
            self.config.add_section("SystemLoad")
            self.config.set("SystemLoad", "group_index", "0")
            self.config.set("SystemLoad", "combo", "False")
            self.config.set("SystemLoad", "spin_min", "0")
            self.config.set("SystemLoad", "spin_unit", "0")

    def set_sys_load(self):
        self.timer2.start(1000)

    def timer_sl_tick(self):
        self.ui.labelRAMUsed.setText("%.2f %%" % used_percent())
        self.ui.labelRAMAvailable.setText("%.2f %%" % available_percent())
        self.ui.labelCPULoad.setText("%.2f %%" % cpu_load())
        self.ui.labelCPUTemp.setText("%.2f °C" % x86_pkg_temp(scale="celsius"))

    def closeEvent(self, a0: QtGui.QCloseEvent):
        try:
            with open(config_file, "w") as file:
                self.config.write(file)

        except Exception as ex:
            err = ""
            for arg in sys.exc_info():
                err += "! " + str(arg) + "\n"
            self.msg_dlg("An unexpected error occurred:", ex.args[1], QMessageBox.Ok,
                         QMessageBox.Warning, err)

        finally:
            application.close()
            print("Goodbye!")
    # </editor-fold>

    # <editor-fold desc= " Controls "
    def button_group_actions_clicked(self):
        if self.ui.radioButtonShutdown.isChecked():
            self.action = Action.Shutdown
        elif self.ui.radioButtonReboot.isChecked():
            self.action = Action.Reboot
        elif self.ui.radioButtonCloseSesion.isChecked():
            self.action = Action.CloseSession
        elif self.ui.radioButtonLock.isChecked():
            self.action = Action.Lock
        elif self.ui.radioButtonSuspend.isChecked():
            self.action = Action.Suspend
        elif self.ui.radioButtonHibernate.isChecked():
            self.action = Action.Hibernate
        elif self.ui.radioButtonNotify.isChecked():
            self.action = Action.Notify
        elif self.ui.radioButtonExecute.isChecked():
            self.action = Action.Execute
        else:
            self.action = Action.Mail
        self.config.set("Main", "actions", str(self.action.name))

    def tab_widget_changed(self):
        if self.ui.tabWidget.currentIndex() == 0:
            self.condition = Condition.AtTime
        elif self.ui.tabWidget.currentIndex() == 1:
            self.condition = Condition.Countdown
        elif self.ui.tabWidget.currentIndex() == 2:
            self.condition = Condition.SystemLoad
        elif self.ui.tabWidget.currentIndex() == 3:
            self.condition = Condition.Network
        elif self.ui.tabWidget.currentIndex() == 4:
            self.condition = Condition.Power
        elif self.ui.tabWidget.currentIndex() == 5:
            self.condition = Condition.Drives
        else:
            # TODO CHANGE
            print("ERROR")
        self.config.set("Main", "conditions", str(self.condition.name))

    def datetime_edit_changed(self):
        self.config.set("AtTime", "date_time", str(self.ui.dateTimeEdit.dateTime().toString("yyyy/MM/dd hh:mm:ss")))

    def button_group_sys_load_clicked(self):
        if self.ui.radioButtonLoadRAMUsed.isChecked():
            index = 0
        elif self.ui.radioButtonLoadRAMAvailable.isChecked():
            index = 1
        elif self.ui.radioButtonLoadCPU.isChecked():
            index = 2
        else:
            index = 3
        self.ui.labelSystemLoadUnitSymbol.setText("%" if not index == 3 else "°C")
        self.config.set("SystemLoad", "group_index", str(index))

    def spinbox_hours_value_changed(self):
        self.config.set("CountDown", "hours", str(self.ui.spinBoxHours.value()))

    def spinbox_minutes_value_changed(self):
        self.config.set("CountDown", "minutes", str(self.ui.spinBoxMinutes.value()))

    def spinbox_seconds_value_changed(self):
        self.config.set("CountDown", "seconds", str(self.ui.spinBoxSeconds.value()))

    def combo_sl_index_changed(self):
        self.config.set("SystemLoad", "combo", str(self.ui.comboBoxSystemLoad.currentIndex()))
        print(bool(self.ui.comboBoxSystemLoad.currentIndex()))

    def spinbox_minutes_sl_value_changed(self):
        self.config.set("SystemLoad", "spin_min", str(self.ui.spinBoxSystemLoadMinutes.value()))

    def spinbox_unit_sl_value_changed(self):
        self.config.set("SystemLoad", "spin_unit", str(self.ui.spinBoxSystemLoadUnit.value()))

    # </editor-fold>

    @staticmethod
    def msg_dlg(body, info="", buttons=QMessageBox.Ok, icon=QMessageBox.Information, details=""):

        msg = QMessageBox()

        msg.setIcon(icon)
        msg.setText(body)
        msg.setInformativeText(info)
        msg.setWindowTitle("Pycket")
        msg.setStandardButtons(buttons)

        if details != "":
            msg.setDetailedText(details)

        return msg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = SetForm()
    application.show()
    sys.exit(app.exec_())
