from ui.notify_settings_window import Ui_NotifySettingsDialog
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QMessageBox, QLineEdit, QFileDialog
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import QTimer
from configparser import ConfigParser
from os.path import join, exists, dirname, expanduser
from os import getcwd, makedirs, remove
from sys import argv, exit
from common import *

# TODO: Delete:
from provisional import NOTIFY_CFG


class NotifySettingsForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NotifySettingsDialog()
        self.ui.setupUi(self)
        self.config = ConfigParser()
        self.set_config()
        self.timer = QTimer()
        self.ui.checkBoxAlwaysOnTop.stateChanged.connect(self.checkbox_always_on_top_state_changed)
        self.ui.checkBoxCloseAuto.stateChanged.connect(self.checkbox_close_auto_state_changed)
        self.ui.spinBoxSecondsClose.valueChanged.connect(self.spinbox_seconds_value_changed)
        self.ui.checkBoxShowTime.stateChanged.connect(self.checkbox_show_time_state_changed)
        self.ui.checkBoxPlaySound.stateChanged.connect(self.checkbox_play_sound_state_changed)
        self.ui.comboBoxSounds.currentTextChanged.connect(self.combobox_sounds_text_changed)
        self.ui.checkBoxInLoop.stateChanged.connect(self.checkbox_in_loop_state_changed)
        self.ui.doubleSpinBoxOpacity.valueChanged.connect(self.double_spinbox_opacity_value_changed)

        self.ui.fontComboBoxHeader.currentTextChanged.connect(self.font_combobox_header_text_changed)
        self.ui.spinBoxSizeFontHeader.valueChanged.connect(self.spinbox_font_size_header_value_changed)
        self.ui.checkBoxBoldHeader.stateChanged.connect(self.checkbox_bold_header_state_changed)
        self.ui.checkBoxItalicHeader.stateChanged.connect(self.checkbox_italic_header_state_changed)

        self.ui.lineEditHeader.textChanged.connect(self.line_edit_header_text_changed)
        self.ui.plainTextEditBody.textChanged.connect(self.plain_text_edit_body_text_changed)
        self.ui.fontComboBoxBody.currentTextChanged.connect(self.font_combobox_body_text_changed)
        self.ui.spinBoxSizeFontBody.valueChanged.connect(self.spinbox_font_size_body_value_changed)
        self.ui.checkBoxBoldBody.stateChanged.connect(self.checkbox_bold_body_state_changed)
        self.ui.checkBoxItalicBody.stateChanged.connect(self.checkbox_italic_body_state_changed)
        self.ui.pushButtonOk.clicked.connect(self.pushbutton_ok_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.pushbutton_cancel_clicked)
        self.ui.pushButtonTest.clicked.connect(self.pushbutton_test_clicked)
        self.timer.timeout.connect(self.timer_tick)

    def set_config(self):
        if exists(NOTIFY_CFG):
            self.config.read(NOTIFY_CFG)
            set_geometry(self.config, self.setGeometry)
        else:
            folder = dirname(NOTIFY_CFG)
            if not exists(folder):
                makedirs(folder)
            make_geometry(self.config, 400, 600)
            self.config.add_section("General")
            self.config.set("General", "on_top", "False")
            self.config.set("General", "auto_close", "False")
            self.config.set("General", "seconds", "0")
            self.config.set("General", "show_time", "False")
            self.config.set("General", "play_sound", "False")
            self.config.set("General", "in_loop", "False")
            self.config.set("General", "sound", "?")  # TODO set a sound
            self.config.set("General", "opacity", "0")
            self.config.add_section("Header")
            self.config.set("Header", "font", "Noto Sans")
            self.config.set("Header", "size", "10")
            self.config.set("Header", "bold", "False")
            self.config.set("Header", "italic", "False")
            self.config.set("Header", "txt", "")
            self.config.add_section("Body")
            self.config.set("Body", "font", "Noto Sans")
            self.config.set("Body", "size", "14")
            self.config.set("Body", "bold", "False")
            self.config.set("Body", "italic", "False")
            self.config.set("Body", "body", "ALARM")

            with open(NOTIFY_CFG, "w") as file:
                self.config.write(file)

    def closeEvent(self, a0: QCloseEvent):
        save_geometry(self.config, self.geometry())
        close_widget(self, self.config, NOTIFY_CFG)

    def checkbox_always_on_top_state_changed(self):
        self.config.set("General", "on_top", "False")

    def checkbox_close_auto_state_changed(self):
        self.config.set("General", "auto_close", str(self.ui.checkBoxCloseAuto.isChecked()))

    def spinbox_seconds_value_changed(self):
        self.config.set("General", "seconds", str(self.ui.spinBoxSecondsClose.value()))

    def checkbox_show_time_state_changed(self):
        self.config.set("General", "show_time", str(self.ui.checkBoxShowTime.isChecked()))

    def checkbox_play_sound_state_changed(self):
        self.config.save_geometry, set_geometry, make_geometryset("General", "play_sound", str(self.ui.checkBoxPlaySound.isChecked()))

    def combobox_sounds_text_changed(self):
        self.config.set("General", "sound", self.ui.comboBoxSounds.currentText())

    def checkbox_in_loop_state_changed(self):
        self.config.set("General", "in_loop", str(self.ui.checkBoxInLoop.isChecked()))

    def double_spinbox_opacity_value_changed(self):
        self.config.set("General", "opacity", str(self.ui.doubleSpinBoxOpacity.value()))

    def font_combobox_header_text_changed(self):
        self.config.set("Header", "font", self.ui.fontComboBoxBody.currentText())

    def spinbox_font_size_header_value_changed(self):
        self.config.set("Header", "size", str(self.ui.spinBoxSizeFontHeader.value()))

    def checkbox_bold_header_state_changed(self):
        self.config.set("Header", "bold", str(self.ui.checkBoxBoldHeader.isChecked()))

    def checkbox_italic_header_state_changed(self):
        self.config.set("Header", "italic", str(self.ui.checkBoxItalicHeader.isChecked()))

    def line_edit_header_text_changed(self):
        self.config.set("Header", "txt", self.ui.lineEditHeader.text())

    def font_combobox_body_text_changed(self):
        self.config.set("Body", "font", self.ui.fontComboBoxBody.currentText())

    def spinbox_font_size_body_value_changed(self):
        self.config.set("Body", "size", str(self.ui.spinBoxSizeFontBody.value()))

    def checkbox_bold_body_state_changed(self):
        self.config.set("Body", "bold", str(self.ui.checkBoxBoldBody.isChecked()))

    def checkbox_italic_body_state_changed(self):
        self.config.set("Body", "italic", str(self.ui.checkBoxItalicBody.isChecked()))

    def plain_text_edit_body_text_changed(self):
        self.config.set("Body", "txt", self.ui.plainTextEditBody.toPlainText())

    def pushbutton_ok_clicked(self):
        from common import msg_dlg
        msg_dlg("Body", "info", QMessageBox.Ok | QMessageBox.No, QMessageBox.Warning, "details")

    def pushbutton_cancel_clicked(self):
        pass

    def pushbutton_test_clicked(self):
        pass

    def timer_tick(self):
        print("Beep")
        pass


if __name__ == '__main__':
    app = QApplication(argv)
    application = NotifySettingsForm()
    application.show()

    exit(app.exec_())