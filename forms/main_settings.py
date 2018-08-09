from ui.settings_window import *
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtCore import QTranslator
from configparser import ConfigParser
from common.common import *
import sys

# TODO: Move
from provisional import MAIN_CFG


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
        self.ui.lineEditShutdown.textChanged.connect(self.line_edit_shutdown_text_changed)
        self.ui.lineEditReboot.textChanged.connect(self.line_edit_reboot_text_changed)
        self.ui.lineEditCloseSession.textChanged.connect(self.line_edit_close_session_text_changed)
        self.ui.lineEditLockScreen.textChanged.connect(self.line_edit_lock_screen_text_changed)
        self.ui.lineEditSuspend.textChanged.connect(self.line_edit_suspend_text_changed)
        self.ui.lineEditHibernate.textChanged.connect(self.line_edit_hibernate_text_changed)
        self.ui.lineEditExecute.textChanged.connect(self.line_edit_execute_text_changed)
        self.ui.comboBoxStyle.currentIndexChanged.connect(self.combo_style_current_index_changed)
        self.ui.lineEditDateTimeEditFormat.textChanged.connect(self.line_edit_date_time_edit_format)
        self.ui.comboBoxTempScale.currentIndexChanged.connect(self.combo_temp_scale_current_index_changed)
        self.ui.checkBoxProgressbarText.stateChanged.connect(self.checkbox_progressbar_text_state_changed)
        self.ui.checkBoxAlwaysOnTop.stateChanged.connect(self.checkbox_always_on_top_state_changed)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        save_geometry(self.config, self.geometry(), "Geometry_Settings")
        close_widget(self, self.config, MAIN_CFG, self.cancel)

    def canceled(self):
        self.cancel = True
        self.close()

    def get_config(self):
        self.config.read(test_cfg(MAIN_CFG))
        set_geometry(self.config, self.setGeometry, "Geometry_Settings")
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
        self.ui.checkBoxAlwaysOnTop.setChecked(self.config.getboolean("General", "on_top"))

    def line_edit_shutdown_text_changed(self):
        self.config.set("Commands", "shutdown", self.ui.lineEditShutdown.text())

    def line_edit_reboot_text_changed(self):
        self.config.set("Commands", "reboot", self.ui.lineEditReboot.text())

    def line_edit_close_session_text_changed(self):
        self.config.set("Commands", "close_session", self.ui.lineEditCloseSession.text())

    def line_edit_lock_screen_text_changed(self):
        self.config.set("Commands", "lock_screen", self.ui.lineEditLockScreen.text())

    def line_edit_suspend_text_changed(self):
        self.config.set("Commands", "suspend", self.ui.lineEditSuspend.text())

    def line_edit_hibernate_text_changed(self):
        self.config.set("Commands", "hibernate", self.ui.lineEditHibernate.text())

    def line_edit_execute_text_changed(self):
        self.config.set("Commands", "execute", self.ui.lineEditExecute.text())

    def combo_style_current_index_changed(self):
        self.config.set("General", "qstyle", self.ui.comboBoxStyle.currentText())

    def combo_temp_scale_current_index_changed(self):
        self.config.set("General", "temp_scale", self.ui.comboBoxTempScale.currentText())

    def line_edit_date_time_edit_format(self):
        self.config.set("General", "date_time_format", self.ui.lineEditDateTimeEditFormat.text())

    def checkbox_progressbar_text_state_changed(self):
        self.config.set("General", "progressbar_text", str(self.ui.checkBoxProgressbarText.isChecked()))

    def checkbox_always_on_top_state_changed(self):
        self.config.set("General", "on_top", str(self.ui.checkBoxAlwaysOnTop.isChecked()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    translator = QTranslator()
    translator.load(get_loc_file())
    app.installTranslator(translator)
    application = ConfigForm()
    application.show()
    sys.exit(app.exec_())