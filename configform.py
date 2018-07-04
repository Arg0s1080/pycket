from ui.settings_window import *
from PyQt5.QtWidgets import QStyleFactory
from configparser import ConfigParser
from os.path import join
from os import getcwd
import sys

config_file = join(getcwd(), "config.cfg")


class ConfigForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.cancel = None
        self.config = ConfigParser()
        self.ui.comboBoxStyle.addItems(QStyleFactory.keys())
        self.get_config()
        self.ui.pushButtonOk.clicked.connect(self.close)
        self.ui.pushButtonCancel.clicked.connect(self.canceled)
        self.ui.lineEditShutdown.focusOutEvent = self.line_edit_shutdown_focus_out
        self.ui.lineEditReboot.focusOutEvent = self.line_edit_reboot_focus_out
        self.ui.lineEditCloseSession.focusOutEvent = self.line_edit_close_session_focus_out
        self.ui.lineEditLockScreen.focusOutEvent = self.line_edit_lock_screen_focus_out
        self.ui.lineEditSuspend.focusOutEvent = self.line_edit_suspend_focus_out
        self.ui.lineEditHibernate.focusOutEvent = self.line_edit_hibernate_focus_out
        self.ui.lineEditExecute.focusOutEvent = self.line_edit_execute_focus_out
        self.ui.comboBoxStyle.currentIndexChanged.connect(self.combo_style_current_index_changed)
        self.ui.lineEditDateTimeEditFormat.focusOutEvent = self.line_edit_date_time_edit_format
        self.ui.comboBoxTempScale.currentIndexChanged.connect(self.combo_temp_scale_current_index_changed)
        self.ui.checkBoxProgressbarText.stateChanged.connect(self.check_progressbar_text_state_changed)



    def closeEvent(self, a0: QtGui.QCloseEvent):
        try:
            if not self.cancel:
                print("BEEEP")
                with open(config_file, "w") as file:
                    self.config.write(file)
        except Exception:
            for arg in sys.exc_info():
                print("! %s" % arg)
        finally:
            self.close()
            print("Close Config Form!")

    def canceled(self):
        self.cancel = True
        self.close()

    def test_event(self, event):
        print("TEST EVENT")

    def get_config(self):
        self.config.read(config_file)
        self.ui.lineEditShutdown.setText(self.config.get("Commands", "shutdown"))
        self.ui.lineEditReboot.setText(self.config.get("Commands", "reboot"))
        self.ui.lineEditCloseSession.setText(self.config.get("Commands", "close_session"))
        self.ui.lineEditLockScreen.setText(self.config.get("Commands", "lock_screen"))
        self.ui.lineEditSuspend.setText(self.config.get("Commands", "suspend"))
        self.ui.lineEditHibernate.setText(self.config.get("Commands", "hibernate"))
        self.ui.lineEditExecute.setText(self.config.get("Commands", "execute"))
        self.ui.comboBoxStyle.setCurrentText(self.config.get("General", "qstyle"))
        self.ui.lineEditDateTimeEditFormat.setText(self.config.get("General", "date_time_format"))
        self.ui.comboBoxTempScale.setCurrentText(self.config.get("General", "temp_scale"))
        self.ui.checkBoxProgressbarText.setChecked(self.config.getboolean("General", "progressbar_text"))

    def line_edit_shutdown_focus_out(self, event):
        self.config.set("Commands", "shutdown", self.ui.lineEditShutdown.text())

    def line_edit_reboot_focus_out(self, event):
        self.config.set("Commands", "reboot", self.ui.lineEditReboot.text())

    def line_edit_close_session_focus_out(self, event):
        self.config.set("Commands", "close_session", self.ui.lineEditCloseSession.text())

    def line_edit_lock_screen_focus_out(self, event):
        self.config.set("Commands", "lock_screen", self.ui.lineEditLockScreen.text())

    def line_edit_suspend_focus_out(self, event):
        self.config.set("Commands", "suspend", self.ui.lineEditSuspend.text())

    def line_edit_hibernate_focus_out(self, event):
        self.config.set("Commands", "hibernate", self.ui.lineEditHibernate.text())

    def line_edit_execute_focus_out(self, event):
        self.config.set("Commands", "execute", self.ui.lineEditExecute.text())

    def combo_style_current_index_changed(self):
        self.config.set("General", "qstyle", self.ui.comboBoxStyle.currentText())

    def combo_temp_scale_current_index_changed(self):
        self.config.set("General", "temp_scale", self.ui.comboBoxTempScale.currentText())

    def line_edit_date_time_edit_format(self, event):
        self.config.set("General", "date_time_format", self.ui.lineEditDateTimeEditFormat.text())

    def check_progressbar_text_state_changed(self):
        self.config.set("General", "progressbar_text", str(self.ui.checkBoxProgressbarText.isChecked()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ConfigForm()
    application.show()

    sys.exit(app.exec_())