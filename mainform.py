from setform import *


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
        if self.condition == Condition.AtTime:  # At time
            import datetime
            self.delay = self.ui.dateTimeEdit.dateTime().toTime_t() - QDateTime.currentDateTime().toTime_t()
            # Debug
            print("Debug AtTime:", self.delay)
            self.setTemp1(1)
            if datetime.datetime.now() >= self.ui.dateTimeEdit.dateTime():
                print("Log: error, date after now")
                return
        elif self.condition == Condition.Countdown:  # Countdown:
            self.delay = (self.ui.spinBoxHours.value() * 3600) + \
                         (self.ui.spinBoxMinutes.value() * 60) + self.ui.spinBoxSeconds.value()
            self.setTemp1(1)
            # Debug
            print("Debug Countdown:", self.delay)
        elif self.condition == Condition.SystemLoad:
            pass


        print("start clicked")

    def pushbutton_cancel_clicked(self):
        print(QDateTime.currentDateTime().addSecs(3600).toString("yyyy/MM/dd hh:mm:ss"))

    def pushbutton_pause_clicked(self):
        print(self.config.get("AtTime", "date_time"))

    def timer1_tick(self):
        if self.delay <= 0:
            self.setTemp1(0)
            self.execute_actions()
            return

        self.delay -= 1
        self.ui.progressBar.setValue(self.ui.progressBar.maximum() - self.delay)
        print("Debug. Delay:", self.delay)

    def setTemp1(self, on):
        if on:
            self.ui.progressBar.setMaximum(self.delay)
            self.ui.progressBar.setValue(0)
            self.timer1.start(1000)
        else:
            self.ui.progressBar.setValue(0)
            self.timer1.stop()
            # TODO Below to Quarantine
            self.timer1.killTimer(0)

    def execute_actions(self):
        if self.action is Action.Shutdown:
            print("Shutdown!!")
        elif self.action is Action.Reboot:
            print("Reboot!!")
        elif self.action is Action.Lock:
            print("Lock screen!!")
        elif self.action is Action.Suspend:
            print("Suspend!!")
        elif self.action is Action.Hibernate:
            print("Hibernate!!")
        elif self.action is Action.Notify:
            print("Notify!!")
        elif self.action is Action.Execute:
            print("Execute!!")
        elif self.action is Action.Mail:
            print("Send Mail!!")


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    application = MainForm()
    application.show()
    sys.exit(app.exec_())