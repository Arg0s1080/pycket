#!/usr/bin/python
# -*- coding: utf-8 -*-

#import os
import sys
import statux.ram as ram
import statux.cpu2 as cpu
import statux.temp as temp

from os import makedirs
from os.path import dirname
from ui.main_window import *
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtCore import QDateTime, QTimer
from forms.configform import ConfigForm
from common.enums import *
from statux.net import get_interfaces
from statux.disks import mounted_partitions
from statux.system import session_id
from common.common import *

# TODO: Move
from provisional import MAIN_CFG


class SetMainForm(QtWidgets.QMainWindow):
    # <editor-fold desc=" Init and close "
    def __init__(self):
        #QtWidgets.QWidget.__init__(self, None)
        super().__init__()
        self.ui = Ui_SetMainForm()
        self.ui.setupUi(self)

        # Section: Widgets parameters
        # self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime().addSecs(10))  # TODO Change addSecs
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.comboBoxNetworkInterface.addItems(sorted(get_interfaces()))
        self.ui.comboBoxPttPartitions.addItems(list(mounted_partitions()))

        # Section: Variables
        self.delay = 0
        self.action = Action.Shutdown
        self.condition = Condition.AtTime
        self.state = State.Stopped
        self.delay = None
        self.value = None
        self.scale = None
        self.index = None
        self.net_interface = None
        self.partition = None
        self.index_radio = None
        self.index_radio2 = None
        self.index_combo = None
        self.title = None
        self.minutes = None
        self.spin_value = None
        self.check_for = None
        self.cpu_mon = None
        self.cpu_load = None
        self.alarm_count = None   # to use only one alarm
        self.alarm_count_ptt = None  # to use only one alarm
        self.count_bytes = None
        self.unit_panel = None
        self.temp_symbol = None
        self.temp_scale = None

        # Section: Declarations
        self.timer_mon = QTimer()   # SysLoad TabWidget monitoring
        self.timer = QTimer()       # ALL

        self.config = ConfigParser()
        self.set_config()
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
        self.set_sys_load()

        # Section: Events
        self.ui.pushButtonStart.clicked.connect(self.pushbutton_start_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.pushbutton_cancel_clicked)
        self.ui.dateTimeEditAtTime.dateTimeChanged.connect(self.datetime_edit_at_time_changed)
        self.ui.pushButtonAtTimeNow.clicked.connect(self.pushbutton_at_time_now_clicked)
        self.ui.pushButtonAtTimePlus1H.clicked.connect(self.pushbutton_at_time_plus_1h)
        self.ui.pushButtonAtTimeMinus1H.clicked.connect(self.pushbutton_at_time_minus_1h)
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
        self.ui.buttonGroupPartitions.buttonClicked.connect(self.button_group_ptt_clicked)
        self.ui.comboBoxPttPartitions.focusOutEvent = self.combo_ptt_partitions_focus_out
        #self.ui.comboBoxPttPartitions.currentIndexChanged.connect(self.combo_ptt_partitions_index_changed)
        self.ui.comboBoxPttSpace.currentIndexChanged.connect(self.combo_ptt_space_index_changed)
        self.ui.comboBoxPttSpaceLessMore.currentIndexChanged.connect(self.combo_ptt_spc_less_more_index_changed)
        self.ui.comboBoxPttSpaceUnit.currentIndexChanged.connect(self.combo_ptt_spc_unit_index_changed)
        self.ui.comboBoxPttIOPS.currentIndexChanged.connect(self.combo_ptt_iops_index_changed)
        self.ui.comboBoxPttIOPSLessMore.currentIndexChanged.connect(self.combo_ptt_iops_less_more_index_changed)
        self.ui.comboBoxPttIOPSUnit.currentIndexChanged.connect(self.combo_ptt_iops_unit_index_changed)
        self.ui.spinBoxPttSpace.valueChanged.connect(self.spin_ptt_space_value_changed)
        self.ui.spinBoxPttIOPS.valueChanged.connect(self.spin_ptt_iops_value_changed)
        self.ui.spinBoxPttMinutes.valueChanged.connect(self.spin_ptt_minutes_value_changed)
        self.ui.checkBoxPttFor.stateChanged.connect(self.check_ptt_for_state_changed)
        self.ui.actionSettings.triggered.connect(self.action_settings_triggered)
        self.timer_mon.timeout.connect(self.timer_mon_tick)
        self.timer.timeout.connect(self.timer_tick)
        
        self.settings = ConfigForm()

    # TEST
    def test_event(self, event):
        print("TEST EVENT")
        print(type(QtCore.Qt.WindowStaysOnTopHint))
        application.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)

    def set_config(self):
        if exists(MAIN_CFG):
            self.config.read(MAIN_CFG)

            # Section: Geometry
            set_geometry(self.config, self.setGeometry)

            # Section: General
            # self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, self.config.getboolean("General", "on_top"))
            self.setStyle(QtWidgets.QApplication.setStyle(self.config.get("General", "qstyle")))
            self.ui.dateTimeEditAtTime.setDisplayFormat(self.config.get("General", "date_time_format"))
            scale = self.config.get("General", "temp_scale")
            self.temp_scale = scale.lower()
            self.temp_symbol = "%s%s" % (u"\u00B0", scale[0])
            self.ui.progressBar.setTextVisible(self.config.getboolean("General", "progressbar_text"))

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
            elif self.condition == Condition.Partitions:
                self.ui.tabWidget.setCurrentIndex(5)

            # Section: AtTime
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

            # Section Partitions
            if self.config.getboolean("Partitions", "group_index"):
                self.ui.radioButtonPttIOPS.setChecked(True)
            else:
                self.ui.radioButtonPttSpace.setChecked(True)
            self.ui.comboBoxPttPartitions.setCurrentText(self.config.get("Partitions", "combo_partitions"))
            self.ui.comboBoxPttSpace.setCurrentIndex(self.config.getint("Partitions", "combo_space"))
            self.ui.comboBoxPttSpaceLessMore.setCurrentIndex(self.config.getboolean("Partitions", "combo_spc_less_more"))
            self.ui.comboBoxPttSpaceUnit.setCurrentIndex(self.config.getint("Partitions", "combo_spc_unit"))
            self.ui.comboBoxPttIOPS.setCurrentIndex(self.config.getboolean("Partitions", "combo_iops"))
            self.ui.comboBoxPttIOPSLessMore.setCurrentIndex(self.config.getboolean("Partitions", "combo_iops_less_more"))
            self.ui.comboBoxPttIOPSUnit.setCurrentIndex(self.config.getint("Partitions", "combo_iops_unit"))
            self.ui.spinBoxPttSpace.setValue(self.config.getint("Partitions", "spin_space_unit"))
            self.ui.spinBoxPttIOPS.setValue(self.config.getint("Partitions", "spin_iops_unit"))
            self.ui.spinBoxPttMinutes.setValue(self.config.getint("Partitions", "spin_minutes"))
            self.ui.checkBoxPttFor.setChecked(self.config.getboolean("Partitions", "check_for"))

        else:
            folder = dirname(MAIN_CFG)
            if not exists(folder):
                makedirs(folder)
            make_geometry(self.config, 657, 424)
            self.config.add_section("General")
            self.config.set("General", "qstyle", QStyleFactory.keys()[0])
            self.config.set("General", "temp_scale", "Celsius")
            self.config.set("General", "date_time_format", "dd/MM/yyyy - HH:mm:ss")
            self.config.set("General", "progressbar_text", "False")
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
            self.config.add_section("Partitions")
            self.config.set("Partitions", "group_index", "False")
            self.config.set("Partitions", "combo_partitions", list(mounted_partitions().keys())[0])
            self.config.set("Partitions", "combo_space", "0")
            self.config.set("Partitions", "combo_spc_less_more", "False")
            self.config.set("Partitions", "combo_spc_unit", "0")
            self.config.set("Partitions", "combo_iops", "False")
            self.config.set("Partitions", "combo_iops_less_more", "False")
            self.config.set("Partitions", "combo_iops_unit", "0")
            self.config.set("Partitions", "spin_space_unit", "0")
            self.config.set("Partitions", "spin_iops_unit", "0")
            self.config.set("Partitions", "spin_minutes", "0")
            self.config.set("Partitions", "check_for", "False")
            self.config.add_section("Commands")
            self.config.set("Commands", "shutdown", "systemctl poweroff")
            self.config.set("Commands", "reboot", "systemctl reboot")
            self.config.set("Commands", "close_session", "%s %d" % ("loginctl terminate-session", session_id()))
            self.config.set("Commands", "lock_screen", "%s %d" % ("loginctl lock-session", session_id()))
            self.config.set("Commands", "suspend", "systemctl suspend")
            self.config.set("Commands", "hibernate", "systemctl hibernate")
            self.config.set("Commands", "execute", "")

            self.temp_symbol = "°C"
            self.temp_scale = "celsius"
            with open(MAIN_CFG, "w") as file:
                self.config.write(file)

    def set_sys_load(self):
        self.timer_mon.start(1000)
        self.cpu_mon = cpu.Load()

    def timer_mon_tick(self):
        self.ui.labelSystemLoadRAMUsed.setText("%.2f %%" % ram.used_percent())
        self.ui.labelSystemLoadCPUFrequency.setText("%.2f %%" % cpu.frequency_percent(False))
        self.ui.labelSystemLoadCPULoad.setText("%.2f %%" % self.cpu_mon.next_value())
        self.ui.labelSystemLoadCPUTemp.setText("%.2f %s" % (temp.max_val(self.temp_scale), self.temp_symbol))
        # self.ui.labelCPUTemp.setText("%.2f °C" % temp.x86_pkg(scale="celsius"))

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
            self.condition = Condition.Partitions
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
        self.set_spin_sl_unit()
        self.ui.labelSystemLoadUnitSymbol.setText("%" if not index == 3 else self.temp_symbol)
        self.ui.labelSystemLoadTitle.setText(title)
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
        self.net_interface = self.ui.comboBoxNetworkInterface.currentText()

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

    def button_group_ptt_clicked(self):
        self.config.set("Partitions", "group_index", "True" if self.ui.radioButtonPttIOPS.isChecked() else "False")

    def combo_ptt_partitions_focus_out(self, event):
        if self.check_ptt() == QMessageBox.No:
                self.ui.comboBoxPttPartitions.setCurrentText(list(mounted_partitions().keys())[0])
        self.config.set("Partitions", "combo_partitions", self.ui.comboBoxPttPartitions.currentText())

    def combo_ptt_space_index_changed(self):
        self.config.set("Partitions", "combo_space", str(self.ui.comboBoxPttSpace.currentIndex()))

    def combo_ptt_spc_less_more_index_changed(self):
        self.config.set("Partitions", "combo_spc_less_more", str(bool(self.ui.comboBoxPttSpaceLessMore.currentIndex())))

    def combo_ptt_spc_unit_index_changed(self):
        self.config.set("Partitions", "combo_spc_unit", str(self.ui.comboBoxPttSpaceUnit.currentIndex()))

    def combo_ptt_iops_index_changed(self):
        self.config.set("Partitions", "combo_iops", str(bool(self.ui.comboBoxPttIOPS.currentIndex())))

    def combo_ptt_iops_less_more_index_changed(self):
        self.config.set("Partitions", "combo_iops_less_more", str(bool(self.ui.comboBoxPttIOPSLessMore.currentIndex())))

    def combo_ptt_iops_unit_index_changed(self):
        self.config.set("Partitions", "combo_iops_unit", str(self.ui.comboBoxPttIOPSUnit.currentIndex()))

    def spin_ptt_space_value_changed(self):
        self.config.set("Partitions", "spin_space_unit", str(self.ui.spinBoxPttSpace.value()))

    def spin_ptt_iops_value_changed(self):
        self.config.set("Partitions", "spin_iops_unit", str(self.ui.spinBoxPttIOPS.value()))

    def spin_ptt_minutes_value_changed(self):
        self.config.set("Partitions", "spin_minutes", str(self.ui.spinBoxPttMinutes.value()))

    def check_ptt_for_state_changed(self):
        self.config.set("Partitions", "check_for", str(self.ui.checkBoxPttFor.isChecked()))

    # </editor-fold>

    def set_controls(self):
        if self.state == State.Activated:
            self.ui.frame.setStyleSheet("background-color: rgb(0, 85, 0);")
            self.ui.labelState.setText("Activated")
            self.ui.tabWidget.setEnabled(False)
            self.ui.groupBoxActions.setEnabled(False)
            self.ui.pushButtonStart.setEnabled(False)
            self.ui.pushButtonCancel.setEnabled(True)
        elif self.state == State.Stopped:
            self.ui.frame.setStyleSheet("background-color: rgb(170, 0, 0);")
            self.ui.labelData.setText("")
            self.ui.labelState.setText("Stopped")
            self.ui.tabWidget.setEnabled(True)
            self.ui.groupBoxActions.setEnabled(True)
            self.ui.pushButtonStart.setEnabled(True)
            self.ui.pushButtonCancel.setEnabled(False)

        self.ui.labelState.setText(self.state.name)

    def set_progressbar(self, value: int, maximum: int):
        self.ui.progressBar.setMaximum(maximum)
        self.ui.progressBar.setValue(value)

    def set_timer(self, on, timer: QTimer):
        if on:
            timer.start(1000)
        else:
            timer.stop()
        self.ui.progressBar.setValue(0)

    def check_ptt(self):
        ptt = self.ui.comboBoxPttPartitions.currentText()
        mounted = mounted_partitions().keys()
        if ptt not in mounted:
            return msg_dlg("%s is not mounted yet" % ptt, "Do you want continue?",
                           QMessageBox.Yes | QMessageBox.No,
                           details="Current mounted partitions:\n%s" % "\n".join(mounted))

    def set_spin_sl_unit(self):
        if self.ui.radioButtonSystemLoadCPUTemp.isChecked():
            self.ui.labelSystemLoadUnitSymbol.setText(self.temp_symbol)
            if self.temp_scale == "celsius":
                maximum = 100
                minimum = 0
            elif self.temp_scale == "fahrenheit":
                maximum = 212
                minimum = 32
            elif self.temp_scale == "kelvin":
                maximum = 374
                minimum = 273
            else:  # rankine
                maximum = 672
                minimum = 491
        else:
            maximum = 100
            minimum = 0
        self.ui.spinBoxSystemLoadUnit.setMaximum(maximum)
        self.ui.spinBoxSystemLoadUnit.setMinimum(minimum)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = SetMainForm()
    application.show()

    sys.exit(app.exec_())
