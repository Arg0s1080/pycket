from setform import *
from actions import execute
from statux.net import *
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
            self.set_temp1(1)
        elif self.condition == Condition.Countdown:
            self.delay = (self.ui.spinBoxHours.value() * 3600) + \
                         (self.ui.spinBoxMinutes.value() * 60) + self.ui.spinBoxSeconds.value()
            self.set_temp1(1)
            # Debug
            print("Debug Countdown:", self.delay)
        elif self.condition == Condition.SystemLoad:
            self.cpu_load2 = cpu.Load()
            self.alarm_count_sl = 0
            self.timer_sl.start(1000)
        elif self.condition == Condition.Network:
            self.alarm_count_net = 0
            self.count_bytes = self.get_net_value()
            self.timer_net.start(1000)

        self.set_controls()
        print("start clicked")

    def pushbutton_cancel_clicked(self):
        self.ui.labelData.setText("88 days, 87:88:06")

    def timer_temp_tick(self):
        print("Debug", "delay", self.delay)
        if self.delay <= 0:
            self.set_temp1(0)
            execute(self.action)
            return

        self.delay -= 1
        self.ui.progressBar.setValue(self.ui.progressBar.maximum() - self.delay)
        self.ui.labelData.setText(str(timedelta(seconds=self.delay)))
        print("Debug. Delay:", self.delay)

    def set_temp1(self, on):
        if on:
            self.ui.progressBar.setMaximum(self.delay)
            self.ui.progressBar.setValue(0)
            self.timer_temp.start(1000)
        else:
            self.ui.progressBar.setValue(0)
            self.timer_temp.stop()
            # TODO Below to Quarantine
            self.timer_temp.killTimer(0)

    def timer_sl_tick(self):
        value = None
        if self.ui.radioButtonLoadRAMUsed.isChecked():
            value = ram.used_percent()
        elif self.ui.radioButtonCPUFrequency.isChecked():
            value = cpu.frequency_percent(False)
        elif self.ui.radioButtonLoadCPU.isChecked():
            value = self.cpu_load2.next_value()
        elif self.ui.radioButtonCPUTemp.isChecked():
            value = temp.x86_pkg("celsius")
        # DEBUG:
        print("timer sl", "Value", value)
        index = self.ui.comboBoxSystemLoad.currentIndex()
        spin_value = self.ui.spinBoxSystemLoadUnit.value()

        if (index == 0 and value < spin_value) or (index == 1 and value > spin_value):
            if self.ui.checkBoxSystemLoadFor.isChecked():
                self.alarm_count_sl += 1
                if self.alarm_count_sl >= self.ui.spinBoxSystemLoadMinutes.value():  # TODO: Multiply by 60
                    self.timer_sl.stop()
                    self.alarm_count_sl = 0  # TODO: Delete
                    execute(self.action)
            else:
                self.timer_sl.stop()
                self.alarm_count_sl = 0  # TODO: Delete
                execute(self.action)
        else:
            self.alarm_count_sl = 0
        # DEBUG:
        print("timer_sl", "alarm_count", self.alarm_count_sl)

    def timer_net_tick(self):
        value = self.get_net_value()  # - self.count_bytes
        if self.ui.radioButtonNetworkUploadDownloadSpeed.isChecked():
            index = self.ui.comboBoxNetworkMoreLess.currentIndex()
            spin_value = self.ui.spinBoxNetworkUnitSpeed.value()
            if (index == 0 and value < spin_value) or (index == 1 and value > spin_value):
                if self.ui.checkBoxNetworkFor.isChecked():
                    self.alarm_count_net += 1
                    if self.alarm_count_net >= self.ui.spinBoxNetworkMinutes.value():  # TODO: Multiply by 60
                        self.timer_net.stop()
                        self.alarm_count_net = 0  # TODO Delete
                        execute(self.action)
                else:
                    self.timer_net.stop()
                    self.alarm_count_net = 0  # TODO: Delete
                    execute(self.action)
            else:
                self.alarm_count_net = 0  # set 0
        else:  # is finished download/upload
            value -= self.count_bytes
            if value >= self.ui.spinBoxNetworkUnit.value():
                self.timer_net.stop()
                execute(self.action)

    def timer_pow_tick(self):
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

    def set_controls(self):
        if self.state == State.Activated:
            pass
        elif self.state == State.Stopped:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = MainForm()
    application.show()
    sys.exit(app.exec_())
