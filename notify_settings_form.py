from ui.notify_settings_window import Ui_NotifySettingsDialog
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QCloseEvent
from os.path import dirname
from os import makedirs, listdir
from sys import argv, exit
from common.common import *

# TODO: Delete:
from provisional import NOTIFY_CFG


class NotifySettingsForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NotifySettingsDialog()
        self.ui.setupUi(self)
        self.set_combo_sound()
        self.config = ConfigParser()
        self.cancel = None
        self.set_config()
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

    def set_config(self):
        if exists(NOTIFY_CFG):
            self.config.read(NOTIFY_CFG)
            set_geometry(self.config, self.setGeometry)
            self.ui.checkBoxAlwaysOnTop.setChecked(self.config.getboolean("General", "on_top"))
            self.ui.checkBoxCloseAuto.setChecked(self.config.getboolean("General", "auto_close"))
            self.ui.spinBoxSecondsClose.setValue(self.config.getint("General", "seconds"))
            self.ui.checkBoxShowTime.setChecked(self.config.getboolean("General", "show_time"))
            self.ui.lineEditHeader.setEnabled(not self.ui.checkBoxShowTime.isChecked())
            self.ui.checkBoxPlaySound.setChecked(self.config.getboolean("General", "play_sound"))
            self.ui.comboBoxSounds.setCurrentText(self.config.get("General", "sound"))
            self.ui.checkBoxInLoop.setChecked(self.config.getboolean("General", "in_loop"))
            self.ui.doubleSpinBoxOpacity.setValue(self.config.getfloat("General", "opacity"))
            self.ui.fontComboBoxHeader.setCurrentText(self.config.get("Header", "font"))
            self.ui.spinBoxSizeFontHeader.setValue(self.config.getint("Header", "size"))
            self.ui.checkBoxBoldHeader.setChecked(self.config.getboolean("Header", "bold"))
            self.ui.checkBoxItalicHeader.setChecked(self.config.getboolean("Header", "italic"))
            self.ui.lineEditHeader.setText(self.config.get("Header", "txt"))
            self.ui.fontComboBoxBody.setCurrentText(self.config.get("Body", "font"))
            self.ui.spinBoxSizeFontBody.setValue(self.config.getint("Body", "size"))
            self.ui.checkBoxBoldBody.setChecked(self.config.getboolean("Body", "bold"))
            self.ui.checkBoxItalicBody.setChecked(self.config.getboolean("Body", "italic"))
            self.ui.plainTextEditBody.setPlainText(self.config.get("Body", "txt"))
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
            self.config.set("Body", "txt", "ALARM")

            with open(NOTIFY_CFG, "w") as file:
                self.config.write(file)

    def set_combo_sound(self):
        def rn(filename):
            return filename.replace("-", " ")[:-4].title()
        for file in listdir(join(getcwd(), "sounds")):
            if file.endswith(".wav"):
                self.ui.comboBoxSounds.addItem(rn(file))

    def closeEvent(self, a0: QCloseEvent):
        save_geometry(self.config, self.geometry())
        close_widget(self, self.config, NOTIFY_CFG, self.cancel)

    def checkbox_always_on_top_state_changed(self):
        self.config.set("General", "on_top", str(self.ui.checkBoxAlwaysOnTop.isChecked()))

    def checkbox_close_auto_state_changed(self):
        self.config.set("General", "auto_close", str(self.ui.checkBoxCloseAuto.isChecked()))

    def spinbox_seconds_value_changed(self):
        self.config.set("General", "seconds", str(self.ui.spinBoxSecondsClose.value()))

    def checkbox_show_time_state_changed(self):
        self.config.set("General", "show_time", str(self.ui.checkBoxShowTime.isChecked()))
        self.ui.lineEditHeader.setEnabled(not self.ui.checkBoxShowTime.isChecked())

    def checkbox_play_sound_state_changed(self):
        self.config.set("General", "play_sound", str(self.ui.checkBoxPlaySound.isChecked()))

    def combobox_sounds_text_changed(self):
        self.config.set("General", "sound", self.ui.comboBoxSounds.currentText())

    def checkbox_in_loop_state_changed(self):
        self.config.set("General", "in_loop", str(self.ui.checkBoxInLoop.isChecked()))

    def double_spinbox_opacity_value_changed(self):
        self.config.set("General", "opacity", str(self.ui.doubleSpinBoxOpacity.value()))

    def font_combobox_header_text_changed(self):
        self.config.set("Header", "font", self.ui.fontComboBoxHeader.currentText())

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
        self.set_controls()

    def pushbutton_cancel_clicked(self):
        self.cancel = True
        application.close()

    def pushbutton_test_clicked(self):
        self.set_combo_sound()


if __name__ == '__main__':
    app = QApplication(argv)
    application = NotifySettingsForm()
    application.show()

    exit(app.exec_())
