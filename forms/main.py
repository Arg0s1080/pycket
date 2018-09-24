#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from os.path import abspath, curdir, pardir, dirname
#sys.path.append(abspath(curdir))
sys.path.append('/media/ivan/Acer/Users/ivanr/Proyectos/Python/PyCharmProjects/pycket/forms')
sys.path.append('/media/ivan/Acer/Users/ivanr/Proyectos/Python/PyCharmProjects/pycket/')

from forms.setmain import *
from actions import execute
from statux.net import *
from statux.battery import *
from statux.disks import *
from datetime import timedelta
from PyQt5.QtCore import QTranslator


class MainForm(SetMainForm):
    def closeEvent(self, a0: QtGui.QCloseEvent):
        save_geometry(self.config, self.geometry())
        close_widget(self, self.config, MAIN_CFG)

    def pushbutton_start_clicked(self):
        if not self.check_action():
            return
        self.state = State.Activated
        if self.condition == Condition.AtTime: ###############################################
            import datetime
            self.delay = self.ui.dateTimeEditAtTime.dateTime().toTime_t() - QDateTime.currentDateTime().toTime_t()
            print("Debug AtTime:", self.delay)
            if datetime.datetime.now() >= self.ui.dateTimeEditAtTime.dateTime():
                print("Log: error, date after now")
                msg_dlg(self.tr("Pycket cannot start", 1), self.tr("Date before now", 1), icon=QMessageBox.Warning)
                return
            self.ui.progressBar.setMaximum(self.delay)
        elif self.condition == Condition.Countdown:  ###########################################
            self.delay = ((self.ui.spinBoxCountdownHours.value() * 3600) +
                          (self.ui.spinBoxCountdownMinutes.value() * 60) +
                          self.ui.spinBoxCountdownSeconds.value())
            self.ui.progressBar.setMaximum(self.delay)
            # Debug
            print("Debug Countdown:", self.delay)
        elif self.condition == Condition.SystemLoad: ###########################################
            self.cpu_load = cpu.Load()
            self.alarm_count = 0
            self.title = self.ui.labelSystemLoadTitle.text()
            self.index = self.ui.comboBoxSystemLoad.currentIndex()
            self.spin_value = self.ui.spinBoxSystemLoadUnit.value()
            self.minutes = self.ui.spinBoxSystemLoadMinutes.value()
            self.check_for = self.ui.checkBoxSystemLoadFor.isChecked()
        elif self.condition == Condition.Network:  ##############################################
            self.alarm_count = 0
            self.net_interface = self.ui.comboBoxNetworkInterface.currentText()  # WARNING set in event
            if self.ui.radioButtonNetworkIsUpDownloading.isChecked():
                self.index_radio = 1
                self.scale = self.ui.comboBoxNetworkUnit.currentText()
                self.index_combo = self.ui.comboBoxNetworkFinished.currentIndex()
                self.title = self.tr("Downloaded", 1) if self.index_combo == 0 else self.tr("Uploaded", 1)
                self.spin_value = self.ui.spinBoxNetworkUnit.value()
            else:
                self.index_radio = 0
                self.index = self.ui.comboBoxNetworkMoreLess.currentIndex()
                self.scale = self.ui.comboBoxNetworkUnitSpeed.currentText()
                self.index_combo = self.ui.comboBoxNetworkSpeed.currentIndex()
                self.title = self.tr("Download", 1) if self.index_combo == 0 else self.tr("Upload", 1)
                self.spin_value = self.ui.spinBoxNetworkUnitSpeed.value()
                self.minutes = self.ui.spinBoxNetworkMinutes.value()
                self.check_for = self.ui.checkBoxNetworkFor.isChecked()
            self.count_bytes = self.get_net_value()
        elif self.condition == Condition.Power: ####################################################
            if self.ui.radioButtonPowerIs.isChecked():
                self.alarm_count = 0
                self.index_radio = 0
                self.index = self.ui.comboBoxPowerACDC.currentIndex()
                self.title = self.tr("Power", 1)
                self.check_for = self.ui.checkBoxPowerFor.isChecked()
                self.minutes = self.ui.spinBoxPowerMinutes.value()
            else:
                self.index_radio = 1
                self.index = self.ui.comboBoxPowerMoreLess.currentIndex()
                if self.ui.radioButtonPowerBatteryTime.isChecked():
                    self.index_radio2 = 0
                    time_ = self.ui.timeEditPower.time()
                    self.spin_value = time_.hour() * 3600 + time_.minute() * 60
                    self.title = self.tr("Remaining Time", 1)
                    self.scale = ""
                else:
                    self.index_radio2 = 1
                    self.spin_value = self.ui.spinBoxPowerPercent.value()
                    self.title = self.tr("Capacity", 1)
                    self.scale = "%"
        elif self.condition == Condition.Partitions: ###############################################
            if self.check_ptt() == QMessageBox.No:
                return
            self.partition = self.ui.comboBoxPttPartitions.currentText()
            if self.ui.radioButtonPttSpace.isChecked():
                self.index_radio = 0
                self.index = self.ui.comboBoxPttSpaceLessMore.currentIndex()
                self.spin_value = self.ui.spinBoxPttSpace.value()
                self.index_combo = self.ui.comboBoxPttSpace.currentIndex()
                self.scale = self.ui.comboBoxPttSpaceUnit.currentText()
            else:
                self.index_radio = 1
                self.index = self.ui.comboBoxPttIOPSLessMore.currentIndex()
                self.spin_value = self.ui.spinBoxPttIOPS.value()
                self.scale = self.ui.comboBoxPttIOPSUnit.currentText().split("/")[0]
                self.alarm_count = 0
                self.check_for = self.ui.checkBoxPttFor.isChecked()
                self.minutes = self.ui.spinBoxPttMinutes.value()

        self.set_timer(1, self.timer)
        self.set_controls()
        print("start clicked")

    def pushbutton_cancel_clicked(self):
        self.set_finish(False)

    def timer_tick(self):
        if self.condition == Condition.AtTime or self.condition == Condition.Countdown:  ####################
            if self.delay <= 0:
                self.delay = None
                self.set_finish(True)
                return
            self.delay -= 1
            self.ui.progressBar.setValue(self.ui.progressBar.maximum() - self.delay)
            self.ui.labelData.setText(str(timedelta(seconds=self.delay)))
        elif self.condition == Condition.SystemLoad:  #########################################################
            self.scale = "%"
            if self.ui.radioButtonSystemLoadRAMUsed.isChecked():
                value = ram.used_percent()
            elif self.ui.radioButtonSystemLoadCPUFrequency.isChecked():
                value = cpu.frequency_percent(False)
            elif self.ui.radioButtonSystemLoadCPU.isChecked():
                value = self.cpu_load.next_value()
            else:  # Temp
                value = temp.max_val(self.temp_scale)
                self.scale = self.temp_symbol
            self.ui.labelData.setText("%s %.2f %s" % (self.title, value, self.scale))
            if (self.index == 0 and value < self.spin_value) or (self.index == 1 and value > self.spin_value):
                if self.check_for:
                    self.alarm_count += 1
                    self.set_progressbar(self.alarm_count, self.minutes)  # TODO: * 60
                    if self.alarm_count >= self.minutes:  # TODO: Multiply by 60
                        self.set_finish(True)
                else:
                    self.set_finish(True)
            else:
                self.alarm_count = 0
                self.set_progressbar(0, 1)
        elif self.condition == Condition.Network: ############################################################
            value = self.get_net_value() if not self.index_radio else self.get_net_value() - self.count_bytes
            self.ui.labelData.setText("%s: %s %s" % (self.title, value, self.scale))
            if self.index_radio == 0:  # Network speed
                if ((self.index == 0 and value < self.spin_value)
                        or (self.index == 1 and value > self.spin_value)):
                    if self.ui.checkBoxNetworkFor.isChecked():
                        self.alarm_count += 1
                        self.set_progressbar(self.alarm_count, self.minutes)  # TODO * 60
                        if self.alarm_count >= self.minutes:  # TODO: Multiply by 60
                            self.set_finish(True)
                    else:
                        self.set_finish(True)
                else:
                    self.alarm_count = 0  # set 0
                    self.set_progressbar(0, 1)
            else:  # is finished download/upload
                if value >= self.spin_value:
                    self.set_finish(True)
        elif self.condition == Condition.Power:  #################################################################
            if self.index_radio == 0:
                online = ac_adapter_online()
                value = "AC" if online else "DC"
                self.ui.labelData.setText("%s: %s" % (self.title, value))
                if (self.index == 0 and online) or (self.index == 1 and not online):
                    if self.check_for:
                        self.alarm_count += 1
                        self.set_progressbar(self.alarm_count, self.minutes)  # TODO: Multiply by 60
                        if self.alarm_count >= self.minutes:  # TODO: * 60
                            self.set_finish(True)
                    else:
                        self.set_finish(True)
                else:
                    self.alarm_count = 0
                    self.set_progressbar(0, 1)
            else:  # Remaining time
                if self.index_radio2 == 0:
                    value = remaining_time()
                    value_data = remaining_time(True)
                else:
                    value = capacity()
                    value_data = value
                self.ui.labelData.setText("%s: %s%s" % (self.title, value_data, self.scale))
                if (self.index == 0 and value < self.spin_value) or (self.index == 1 and value > self.spin_value):
                    self.set_finish(True)
        elif self.condition == Condition.Partitions:  ###########################################################
            if self.ui.radioButtonPttSpace.isChecked():
                if self.index_combo == 0:
                    value = free_space(self.partition, self.scale)
                    fun = "free"
                elif self.index_combo == 1:
                    value = used_space(self.partition, self.scale)
                    fun = "used"
                else:
                    value = total_size(self.partition, self.scale)
                    fun = "total"
                self.ui.labelData.setText("%s: %s %s %s" % (self.partition, value, self.scale, fun))
                if (value < self.spin_value and self.index == 0) or (value > self.spin_value and self.index == 1):
                    self.set_finish(True)
            else:  # IOPS
                value = bytes_read_write(self.partition, scale=self.scale)[self.index]
                self.ui.labelData.setText("%s: %s %s/sec" % (self.partition, value, self.scale))
                # DEBUG:
                print(value, self.scale)
                if (value < self.spin_value and self.index == 0) or (value > self.spin_value and self.index == 1):
                    if self.ui.checkBoxPttFor.isChecked():
                        self.alarm_count += 1
                        self.set_progressbar(self.alarm_count, self.minutes)  # TODO: Multiply by 60
                        if self.alarm_count >= self.ui.spinBoxPttMinutes.value():  # TODO * 60
                            self.set_finish(True)
                    else:
                        self.set_finish(True)
                else:
                    self.alarm_count = 0
                    self.set_progressbar(0, 1)

    def get_net_value(self):
        if self.ui.radioButtonNetworkUploadDownloadSpeed.isChecked():
            return down_up_speed(self.net_interface, 0, self.scale.split("/")[0])[self.index_combo]
        elif self.ui.radioButtonNetworkIsUpDownloading.isChecked():
            return down_up_bytes(self.net_interface, self.scale)[self.index_combo]

    def set_finish(self, execute_=False):
        self.set_timer(0, self.timer)
        self.delay = None
        self.scale = None
        # self.value = None  # set in timer
        self.index = None
        # self.net_interface = None  # set in event
        self.index_radio = None
        self.index_radio2 = None
        self.check_for = None
        self.title = None
        self.minutes = None
        self.spin_value = None
        self.alarm_count = None

        #xx, yy, zz = (None,) * 3

        self.state = State.Stopped
        self.set_controls()

        if execute_:
            execute(self.action, self.mail_pw)

    def set_time_edit(self, dt: QDateTime, secs: int):
        self.ui.dateTimeEditAtTime.setDateTime(dt.addSecs(secs))

    def pushbutton_at_time_now_clicked(self):
        self.set_time_edit(QDateTime.currentDateTime(), 60)

    def pushbutton_at_time_plus_1h(self):
        self.config.read(MAIN_CFG)
        self.set_time_edit(self.ui.dateTimeEditAtTime.dateTime(), 3600)

    def pushbutton_at_time_minus_1h(self):
        self.set_time_edit(self.ui.dateTimeEditAtTime.dateTime(), -3600)

    def action_settings_triggered(self):
        from forms.main_settings import ConfigForm
        if ConfigForm().exec_() == 0:
            self.set_config()

    @staticmethod
    def action_notify_triggered():
        from forms.notify_settings import NotifySettingsForm
        NotifySettingsForm().exec_()

    @staticmethod
    def action_send_mail_triggered():
        from forms.mail import MailForm
        MailForm().exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    translator = QTranslator()
    translator.load(get_loc_file())
    app.installTranslator(translator)
    application = MainForm()
    application.show()
    sys.exit(app.exec_())
