#!/usr/bin/python
# -*- coding: utf-8 -*-

#import os
import sys
import statux.ram as ram
import statux.cpu2 as cpu
import statux.temp as temp

from os import makedirs, getcwd
from os.path import join, exists
from configparser import ConfigParser
from ui.main_window import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime, QTimer
from enums import *
from statux.net import get_interfaces


config_file = join(getcwd(), "config.cfg")


class SetForm(QtWidgets.QMainWindow):
    # <editor-fold desc=" Init and close "
    def __init__(self):
        QtWidgets.QWidget.__init__(self, None)
        self.ui = Ui_SetForm()
        self.ui.setupUi(self)

        # Section: Widgets parameters
        # self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime().addSecs(10))  # TODO Change addSecs
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.comboBoxNetworkInterface.addItems(get_interfaces())

        # Section: Variables
        self.delay = 0
        self.action = Action.Shutdown
        self.condition = Condition.AtTime
        self.state = State.Stopped
        self.cpu_load1 = None
        self.cpu_load2 = None
        self.alarm_count_sl = None
        self.alarm_count_net = None
        self.count_bytes = None

        # Section: Declarations
        self.timer_mon = QTimer()   # SysLoad TabWidget monitoring
        self.timer_temp = QTimer()  # Countdown and AtTime
        self.timer_sl = QTimer()    # System Load
        self.timer_net = QTimer()   # Network
        self.timer_pow = QTimer()   # Power

        self.config = ConfigParser()
        self.set_config()
        self.set_sys_load()

        # Section: Events
        self.ui.pushButtonStart.clicked.connect(self.pushbutton_start_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.pushbutton_cancel_clicked)
        self.ui.dateTimeEditAtTime.dateTimeChanged.connect(self.datetime_edit_at_time_changed)
        self.ui.spinBoxCountdownHours.valueChanged.connect(self.spinbox_cd_hours_value_changed)
        self.ui.spinBoxCountdownMinutes.valueChanged.connect(self.spinbox_cd_minutes_value_changed)
        self.ui.spinBoxCountdownSeconds.valueChanged.connect(self.spinbox_cd_seconds_value_changed)
        self.ui.buttonGroupActions.buttonClicked.connect(self.button_group_actions_clicked)
        self.ui.buttonGroupSystemLoad.buttonClicked.connect(self.button_group_sl_clicked)
        self.ui.tabWidget.currentChanged.connect(self.tab_widget_changed)
        self.ui.comboBoxSystemLoad.currentIndexChanged.connect(self.combo_sl_index_changed)
        self.ui.spinBoxSystemLoadMinutes.valueChanged.connect(self.spinbox_minutes_sl_value_changed)
        self.ui.spinBoxSystemLoadUnit.valueChanged.connect(self.spinbox_unit_sl_value_changed)
        self.ui.checkBoxSystemLoadFor.stateChanged.connect(self.check_sl_for_state_changed)
        self.ui.buttonGroupNetwork.buttonClicked.connect(self.button_group_network_clicked)
        self.ui.comboBoxNetworkInterface.currentIndexChanged.connect(self.combo_net_interface_index_changed)
        self.ui.comboBoxNetworkSpeed.currentIndexChanged.connect(self.combo_net_speed_index_changed)
        self.ui.comboBoxNetworkMoreLess.currentIndexChanged.connect(self.combo_net_more_less_index_changed)
        self.ui.comboBoxNetworkUnitSpeed.currentIndexChanged.connect(self.combo_net_unit_speed_index_changed)
        self.ui.comboBoxNetworkFinished.currentIndexChanged.connect(self.combo_net_finished_index_changed)
        self.ui.comboBoxNetworkUnit.currentIndexChanged.connect(self.combo_net_unit_index_changed)
        self.ui.spinBoxNetworkUnitSpeed.valueChanged.connect(self.spin_net_unit_speed_value_changed)
        self.ui.spinBoxNetworkMinutes.valueChanged.connect(self.spin_net_minutes_value_changed)
        self.ui.spinBoxNetworkUnit.valueChanged.connect(self.spin_net_unit_value_changed)
        self.ui.checkBoxNetworkFor.stateChanged.connect(self.check_net_for_state_changed)
        self.ui.buttonGroupPowerMain.buttonClicked.connect(self.button_group_pow_main)
        self.ui.buttonGroupPowerSnd.buttonClicked.connect(self.button_group_pow_snd) #
        self.ui.comboBoxPowerACDC.currentIndexChanged.connect(self.combo_pow_acdc_index_changed) #
        self.ui.comboBoxPowerMoreLess.currentIndexChanged.connect(self.combo_pow_more_less_index_changed) #
        self.ui.spinBoxPowerMinutes.valueChanged.connect(self.spin_pow_minutes_value_changed) #
        self.ui.spinBoxPowerPercent.valueChanged.connect(self.spin_pow_percent_value_changed) #
        self.ui.checkBoxPowerFor.stateChanged.connect(self.check_pow_for_state_changed) #
        self.ui.timeEditPower.timeChanged.connect(self.time_edit_pow_time_changed) #
        self.timer_temp.timeout.connect(self.timer_temp_tick)
        self.timer_mon.timeout.connect(self.timer_mon_tick)
        self.timer_sl.timeout.connect(self.timer_sl_tick)
        self.timer_net.timeout.connect(self.timer_net_tick)
        self.timer_pow.timeout.connect(self.timer_pow_tick)


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
            self.ui.dateTimeEditAtTime.setDateTime(d)

            # Section: CountDown
            self.ui.spinBoxCountdownHours.setValue(self.config.getint("CountDown", "hours"))
            self.ui.spinBoxCountdownMinutes.setValue(self.config.getint("CountDown", "minutes"))
            self.ui.spinBoxCountdownSeconds.setValue(self.config.getint("CountDown", "seconds"))

            # Section SystemLoad
            sli = int(self.config.get("SystemLoad", "group_index"))
            if sli == 0:
                self.ui.radioButtonSystemLoadRAMUsed.setChecked(True)
            elif sli == 1:
                self.ui.radioButtonSystemLoadCPUFrequency.setChecked(True)
            elif sli == 2:
                self.ui.radioButtonSystemLoadCPU.setChecked(True)
            else:
                self.ui.radioButtonSystemLoadCPUTemp.setChecked(True)
            self.ui.comboBoxSystemLoad.setCurrentIndex(self.config.getboolean("SystemLoad", "combo"))
            self.ui.spinBoxSystemLoadMinutes.setValue(self.config.getint("SystemLoad", "spin_min"))
            self.ui.spinBoxSystemLoadUnit.setValue(self.config.getint("SystemLoad", "spin_unit"))
            self.ui.checkBoxSystemLoadFor.setChecked(self.config.getboolean("SystemLoad", "check_for"))
            self.button_group_sl_clicked()

            # Section Network
            if self.config.getboolean("Network", "group_index"):
                self.ui.radioButtonNetworkUploadDownloadSpeed.setChecked(True)
            else:
                self.ui.radioButtonNetworkIsUpDownloading.setChecked(True)
            self.ui.comboBoxNetworkInterface.setCurrentIndex(self.config.getint("Network", "combo_interface"))
            self.ui.comboBoxNetworkSpeed.setCurrentIndex(self.config.getboolean("Network", "combo_speed"))
            self.ui.comboBoxNetworkMoreLess.setCurrentIndex(self.config.getboolean("Network", "combo_more_less"))
            self.ui.comboBoxNetworkUnitSpeed.setCurrentIndex(self.config.getint("Network", "combo_unit_speed"))
            self.ui.comboBoxNetworkFinished.setCurrentIndex(self.config.getboolean("Network", "combo_finished"))
            self.ui.comboBoxNetworkUnit.setCurrentIndex(self.config.getint("Network", "combo_unit"))
            self.ui.checkBoxNetworkFor.setChecked(self.config.getboolean("Network", "check_for"))
            self.ui.spinBoxNetworkUnitSpeed.setValue(self.config.getint("Network", "spin_unit_speed"))
            self.ui.spinBoxNetworkMinutes.setValue(self.config.getint("Network", "spin_minutes"))
            self.ui.spinBoxNetworkUnit.setValue(self.config.getint("Network", "spin_unit"))

            # Section Power
            if self.config.getboolean("Power", "group_index_1"):
                self.ui.radioButtonPowerTheBatteryHas.setChecked(True)
            else:
                self.ui.radioButtonPowerIs.setChecked(True) # TODO Try delete (only 2 options)
            if self.config.getboolean("Power", "group_index_2"):
                self.ui.radioButtonPowerBatteryPercent.setChecked(True)
            else:
                self.ui.radioButtonPowerBatteryTime.setChecked(True)  # TODO Try Delete
            self.ui.comboBoxPowerMoreLess.setCurrentIndex(self.config.getboolean("Power", "combo_more_less"))
            self.ui.comboBoxPowerACDC.setCurrentIndex(self.config.getboolean("Power", "combo_acdc"))
            self.ui.spinBoxPowerMinutes.setValue(self.config.getint("Power", "spin_minutes"))
            self.ui.spinBoxPowerPercent.setValue(self.config.getint("Power", "spin_percent"))
            self.ui.checkBoxPowerFor.setChecked(self.config.getboolean("Power", "check_for"))
            self.ui.timeEditPower.setDateTime(QDateTime.fromString(self.config.get("Power", "time_edit"), "h:mm"))
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
            self.config.set("SystemLoad", "check_for", "False")
            self.config.add_section("Network")
            self.config.set("Network", "group_index", "False")
            self.config.set("Network", "combo_interface", "0")
            self.config.set("Network", "combo_speed", "False")
            self.config.set("Network", "combo_more_less", "False")
            self.config.set("Network", "combo_unit_speed", "0")
            self.config.set("Network", "combo_finished", "False")
            self.config.set("Network", "combo_unit", "0")
            self.config.set("Network", "spin_unit_speed", "0")
            self.config.set("Network", "spin_minutes", "0")
            self.config.set("Network", "spin_unit", "0")
            self.config.set("Network", "check_for", "False")
            self.config.add_section("Power")
            self.config.set("Power", "group_index_1", "False")
            self.config.set("Power", "group_index_2", "False")
            self.config.set("Power", "combo_acdc", "False")
            self.config.set("Power", "combo_more_less", "False")
            self.config.set("Power", "spin_minutes", "0")
            self.config.set("Power", "spin_percent", "0")
            self.config.set("Power", "check_for", "False")
            self.config.set("Power", "time_edit", "0:00")


    def set_sys_load(self):
        self.timer_mon.start(1000)
        self.cpu_load1 = cpu.Load()

    def timer_mon_tick(self):
        self.ui.labelSystemLoadRAMUsed.setText("%.2f %%" % ram.used_percent())
        self.ui.labelSystemLoadCPUFrequency.setText("%.2f %%" % cpu.frequency_percent(False))
        self.ui.labelSystemLoadCPULoad.setText("%.2f %%" % self.cpu_load1.next_value())
        self.ui.labelSystemLoadCPUTemp.setText("%.2f °C" % temp.x86_pkg("celsius"))
        # self.ui.labelCPUTemp.setText("%.2f °C" % temp.x86_pkg(scale="celsius"))

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

    def datetime_edit_at_time_changed(self):
        self.config.set("AtTime", "date_time",
                        str(self.ui.dateTimeEditAtTime.dateTime().toString("yyyy/MM/dd hh:mm:ss")))

    def button_group_sl_clicked(self):
        def get_title(control):
            return control.text().split("(")[0].replace("&", "")
        if self.ui.radioButtonSystemLoadRAMUsed.isChecked():
            index = 0
            title = get_title(self.ui.radioButtonSystemLoadRAMUsed)
        elif self.ui.radioButtonSystemLoadCPUFrequency.isChecked():
            index = 1
            title = get_title(self.ui.radioButtonSystemLoadCPUFrequency)
        elif self.ui.radioButtonSystemLoadCPU.isChecked():
            index = 2
            title = get_title(self.ui.radioButtonSystemLoadCPU)
        else:
            index = 3
            title = get_title(self.ui.radioButtonSystemLoadCPUTemp)
        self.ui.labelSystemLoadUnitSymbol.setText("%" if not index == 3 else "°C")
        self.ui.labelSystemLoadTitle.setText("%s is" % title)
        self.config.set("SystemLoad", "group_index", str(index))

    def spinbox_cd_hours_value_changed(self):
        self.config.set("CountDown", "hours", str(self.ui.spinBoxCountdownHours.value()))

    def spinbox_cd_minutes_value_changed(self):
        self.config.set("CountDown", "minutes", str(self.ui.spinBoxCountdownMinutes.value()))

    def spinbox_cd_seconds_value_changed(self):
        self.config.set("CountDown", "seconds", str(self.ui.spinBoxCountdownSeconds.value()))

    def combo_sl_index_changed(self):
        self.config.set("SystemLoad", "combo", str(self.ui.comboBoxSystemLoad.currentIndex()))
        # print("Debug", bool(self.ui.comboBoxSystemLoad.currentIndex()))

    def spinbox_minutes_sl_value_changed(self):
        self.config.set("SystemLoad", "spin_min", str(self.ui.spinBoxSystemLoadMinutes.value()))

    def spinbox_unit_sl_value_changed(self):
        self.config.set("SystemLoad", "spin_unit", str(self.ui.spinBoxSystemLoadUnit.value()))

    def check_sl_for_state_changed(self):
        self.config.set("SystemLoad", "check_for", str(self.ui.checkBoxSystemLoadFor.isChecked()))

    def button_group_network_clicked(self):
        self.config.set("Network", "group_index",
                        "False" if self.ui.radioButtonNetworkIsUpDownloading.isChecked() else "True")

    def combo_net_interface_index_changed(self):
        self.config.set("Network", "combo_interface", str(self.ui.comboBoxNetworkInterface.currentIndex()))

    def combo_net_speed_index_changed(self):
        self.config.set("Network", "combo_speed", str(bool(self.ui.comboBoxNetworkSpeed.currentIndex())))

    def combo_net_more_less_index_changed(self):
        self.config.set("Network", "combo_more_less", str(bool(self.ui.comboBoxNetworkMoreLess.currentIndex())))

    def combo_net_unit_speed_index_changed(self):
        self.config.set("Network", "combo_unit_speed", str(self.ui.comboBoxNetworkUnitSpeed.currentIndex()))

    def combo_net_finished_index_changed(self):
        self.config.set("Network", "combo_finished", str(bool(self.ui.comboBoxNetworkFinished.currentIndex())))

    def combo_net_unit_index_changed(self):
        self.config.set("Network", "combo_unit", str(self.ui.comboBoxNetworkUnit.currentIndex()))

    def spin_net_unit_speed_value_changed(self):
        self.config.set("Network", "spin_unit_speed", str(self.ui.spinBoxNetworkUnitSpeed.value()))

    def spin_net_minutes_value_changed(self):
        self.config.set("Network", "spin_minutes", str(self.ui.spinBoxNetworkMinutes.value()))

    def spin_net_unit_value_changed(self):
        self.config.set("Network", "spin_unit", str(self.ui.spinBoxNetworkUnit.value()))

    def check_net_for_state_changed(self):
        self.config.set("Network", "check_for", str(self.ui.checkBoxNetworkFor.isChecked()))

    def button_group_pow_main(self):
        self.config.set("Power", "group_index_1", str("False" if self.ui.radioButtonPowerIs.isChecked() else "True"))

    def button_group_pow_snd(self):
        self.config.set("Power", "group_index_2",
                        str("False" if self.ui.radioButtonPowerBatteryTime.isChecked() else "True"))

    def combo_pow_acdc_index_changed(self):
        self.config.set("Power", "combo_acdc", str(bool(self.ui.comboBoxPowerACDC.currentIndex())))

    def combo_pow_more_less_index_changed(self):
        self.config.set("Power", "combo_more_less", str(bool(self.ui.comboBoxPowerMoreLess.currentIndex())))

    def spin_pow_minutes_value_changed(self):
        self.config.set("Power", "spin_minutes", str(self.ui.spinBoxPowerMinutes.value()))

    def spin_pow_percent_value_changed(self):
        self.config.set("Power", "spin_percent", str(self.ui.spinBoxPowerPercent.value()))

    def check_pow_for_state_changed(self):
        self.config.set("Power", "check_for", str(self.ui.checkBoxPowerFor.isChecked()))

    def time_edit_pow_time_changed(self):
        self.config.set("Power", "time_edit", self.ui.timeEditPower.time().toString("h:mm"))

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
