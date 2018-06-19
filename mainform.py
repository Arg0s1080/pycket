from setform import *
from actions import execute
from statux.net import *
from statux.battery import *
from datetime import timedelta


class MainForm(SetForm):
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

    def pushbutton_start_clicked(self):
        print(self.condition)
        self.state = State.Activated
        if self.condition == Condition.AtTime:
            import datetime
            self.delay = self.ui.dateTimeEditAtTime.dateTime().toTime_t() - QDateTime.currentDateTime().toTime_t()
            print("Debug AtTime:", self.delay)
            if datetime.datetime.now() >= self.ui.dateTimeEditAtTime.dateTime():
                print("Log: error, date after now")
                self.msg_dlg("Pycket cannot start", "Date before now", icon=QMessageBox.Warning)
                return
            self.set_timer(1, self.timer_temp)
            self.ui.progressBar.setMaximum(self.delay)
        elif self.condition == Condition.Countdown:
            self.delay = ((self.ui.spinBoxCountdownHours.value() * 3600) +
                          (self.ui.spinBoxCountdownMinutes.value() * 60) +
                          self.ui.spinBoxCountdownSeconds.value())
            self.set_timer(1, self.timer_temp)
            self.ui.progressBar.setMaximum(self.delay)
            # Debug
            print("Debug Countdown:", self.delay)
        elif self.condition == Condition.SystemLoad:
            self.cpu_load2 = cpu.Load()
            self.alarm_count_sl = 0
            self.set_timer(1, self.timer_sl)
        elif self.condition == Condition.Network:
            self.alarm_count_net = 0
            self.count_bytes = self.get_net_value()
            self.set_timer(1, self.timer_net)
        elif self.condition == Condition.Power:
            self.alarm_count_pow = 0
            self.set_timer(1, self.timer_pow)
        elif self.condition == Condition.Partitions:
            self.alarm_count_ptt = 0
            self.set_timer(1, self.timer_ptt)

        self.set_controls()
        print("start clicked")

    def pushbutton_cancel_clicked(self):
        if self.condition == Condition.AtTime or self.condition == Condition.Countdown:
            self.set_timer(0, self.timer_temp)
            self.delay = 0
        elif self.condition == Condition.SystemLoad:
            self.set_timer(0, self.timer_sl)
            self.alarm_count_sl = 0
        elif self.condition == Condition.Network:
            self.set_timer(0, self.timer_net)
            self.alarm_count_net = 0
        elif self.condition == Condition.Power:
            self.set_timer(0, self.timer_pow)
            self.alarm_count_pow = 0
        self.state = State.Stopped
        self.set_controls()

    def timer_temp_tick(self):
        if self.delay <= 0:
            self.pushbutton_cancel_clicked()
            execute(self.action)
            return

        self.delay -= 1
        self.ui.progressBar.setValue(self.ui.progressBar.maximum() - self.delay)
        self.ui.labelData.setText(str(timedelta(seconds=self.delay)))
        print("Debug.", "Delay:", self.delay)

    def timer_sl_tick(self):
        value = None
        unit = "%"
        if self.ui.radioButtonSystemLoadRAMUsed.isChecked():
            value = ram.used_percent()
        elif self.ui.radioButtonSystemLoadCPUFrequency.isChecked():
            value = cpu.frequency_percent(False)
        elif self.ui.radioButtonSystemLoadCPU.isChecked():
            value = self.cpu_load2.next_value()
        elif self.ui.radioButtonSystemLoadCPUTemp.isChecked():
            value = temp.cpu("celsius")
            unit = "°C"
        index = self.ui.comboBoxSystemLoad.currentIndex()
        spin_value = self.ui.spinBoxSystemLoadUnit.value()
        self.ui.labelData.setText("%s %.2f %s" % (self.ui.labelSystemLoadTitle.text(), value, unit))

        if (index == 0 and value < spin_value) or (index == 1 and value > spin_value):
            if self.ui.checkBoxSystemLoadFor.isChecked():
                self.alarm_count_sl += 1
                self.set_progressbar(self.alarm_count_sl, self.ui.spinBoxSystemLoadMinutes.value())  # TODO: * 60
                if self.alarm_count_sl >= self.ui.spinBoxSystemLoadMinutes.value():  # TODO: Multiply by 60
                    self.pushbutton_cancel_clicked()
                    execute(self.action)
            else:
                self.pushbutton_cancel_clicked()
                execute(self.action)
        else:
            self.alarm_count_sl = 0
        self.set_controls()

    def timer_net_tick(self):
        # TODO: To get better: tatty
        is_speed = self.ui.radioButtonNetworkUploadDownloadSpeed.isChecked()
        value = self.get_net_value() if is_speed else self.get_net_value() - self.count_bytes
        unit = (self.ui.comboBoxNetworkUnit.currentText() if self.ui.radioButtonNetworkIsUpDownloading.isChecked()
                else self.ui.comboBoxNetworkUnitSpeed.currentText())
        title = (("Download" if self.ui.comboBoxNetworkSpeed.currentIndex() == 0 else "Upload") if is_speed
                 else ("Downloaded" if self.ui.comboBoxNetworkFinished.currentIndex() == 0 else "Uploaded"))
        self.ui.labelData.setText("%s: %.2f %s" % (title, value, unit))
        if is_speed:
            index = self.ui.comboBoxNetworkMoreLess.currentIndex()
            spin_value = self.ui.spinBoxNetworkUnitSpeed.value()
            if (index == 0 and value < spin_value) or (index == 1 and value > spin_value):
                if self.ui.checkBoxNetworkFor.isChecked():
                    self.alarm_count_net += 1
                    self.set_progressbar(self.alarm_count_net, self.ui.spinBoxNetworkMinutes.value())  # TODO * 60
                    if self.alarm_count_net >= self.ui.spinBoxNetworkMinutes.value():  # TODO: Multiply by 60
                        self.pushbutton_cancel_clicked()
                        execute(self.action)
                else:
                    self.pushbutton_cancel_clicked()
                    execute(self.action)
            else:
                self.alarm_count_net = 0  # set 0
        else:  # is finished download/upload
            if value >= self.ui.spinBoxNetworkUnit.value():
                self.pushbutton_cancel_clicked()
                execute(self.action)

    def timer_pow_tick(self):
        if self.ui.radioButtonPowerIs.isChecked():
            online = ac_adapter_online()
            index = self.ui.comboBoxPowerACDC.currentIndex()
            value = "AC" if online else "DC"
            title = "Power"
            self.ui.labelData.setText("%s: %s" % (title, value))
            if (index == 0 and online) or (index == 1 and not online):
                if self.ui.checkBoxPowerFor.isChecked():
                    spin_value = self.ui.spinBoxPowerMinutes.value()
                    self.alarm_count_pow += 1
                    self.set_progressbar(self.alarm_count_pow, spin_value)  # TODO: Multiply by 60
                    if self.alarm_count_pow >= spin_value:
                        self.pushbutton_cancel_clicked()
                        execute(self.action)
                else:
                    self.pushbutton_cancel_clicked()
                    execute(self.action)
            else:
                self.alarm_count_pow = 0
        else:  # Remaining time
            index = self.ui.comboBoxPowerMoreLess.currentIndex()
            if self.ui.radioButtonPowerBatteryTime.isChecked():
                value = remaining_time()
                # DEBUG:
                print("VALUE", value)
                value_data = remaining_time(True)
                time_ = self.ui.timeEditPower.time()
                spin_value = time_.hour() * 3600 + time_.minute() * 60
                title = "Remaining Time"
                unit = ""
            else:
                value = capacity()
                value_data = value
                spin_value = self.ui.spinBoxPowerPercent.value()
                title = "Capacity"
                unit = "%"
            self.ui.labelData.setText("%s: %s%s" % (title, value_data, unit))
            if (index == 0 and value < spin_value) or (index == 1 and value > spin_value):
                self.pushbutton_cancel_clicked()
                execute(self.action)

    def timer_ptt_tick(self):
        if self.ui.radioButtonPttSpace.isChecked():
            pass



    def get_net_value(self):
        if self.ui.radioButtonNetworkUploadDownloadSpeed.isChecked():
            return down_up_speed(self.ui.comboBoxNetworkInterface.currentText(), 0,
                                 self.ui.comboBoxNetworkUnitSpeed.currentText().split("/")[0])[
                                 self.ui.comboBoxNetworkSpeed.currentIndex()]
        elif self.ui.radioButtonNetworkIsUpDownloading.isChecked():
            return down_up_bytes(self.ui.comboBoxNetworkInterface.currentText(),
                                 self.ui.comboBoxNetworkUnit.currentText())[
                                 self.ui.comboBoxNetworkFinished.currentIndex()]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = MainForm()
    application.show()
    sys.exit(app.exec_())
