from pycket.ui.notify_window import Ui_NotifyDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QCloseEvent, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime
from sys import argv, exit
from pycket.common.common import *
from pycket.scripts.sound import Sound

# TODO: Move
from pycket.misc.paths import NOTIFY_CFG


class NotifyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NotifyDialog()
        self.ui.setupUi(self)
        self.config = ConfigParser()
        self.ui.pushButtonClose.clicked.connect(self.pushbutton_close_clicked)
        self.timer_ac = QTimer()
        self.timer_st = QTimer()
        self.timer_sl = QTimer()
        self.timer_ac.timeout.connect(self.timer_ac_tick)  # AutoClose
        self.timer_st.timeout.connect(self.timer_st_tick)  # ShowTime
        self.timer_sl.timeout.connect(self.timer_sl_tick)  # SoundLoop
        self.delay = None
        self.time_format = None
        self.sound = None
        self.play = None
        self.set_config()

    def set_config(self):
        self.config.read(test_cfg(NOTIFY_CFG))
        set_geometry(self.config, self.setGeometry)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, self.config.getboolean("General", "on_top"))
        self.delay = self.config.getint("General", "seconds")
        self.config.getboolean("General", "auto_close") and self.timer_ac.start(1000)
        self.setWindowOpacity(self.config.getfloat("General", "opacity") / 100)
        self.time_format = self.config.get("General", "time_format")
        self.config.getboolean("General", "show_time") and self.timer_st.start(1000)
        header_font = QFont(self.config.get("Header", "font"),
                            self.config.getint("Header", "size"),
                            italic=self.config.getboolean("Header", "italic"))
        header_font.setBold(self.config.getboolean("Header", "bold"))
        self.ui.labelHeader.setFont(header_font)
        self.ui.labelHeader.setText(self.config.get("Header", "txt"))
        body_font = QFont(self.config.get("Body", "font"),
                          self.config.getint("Body", "size"),
                          italic=self.config.getboolean("Body", "italic"))
        body_font.setBold(self.config.getboolean("Body", "bold"))
        self.ui.labelBody.setFont(body_font)
        self.ui.labelBody.setText(self.config.get("Body", "txt"))
        play_sound = self.config.getboolean("General", "play_sound")
        if play_sound:
            self.sound = Sound(self.config.get("General", "sound"))
            self.play = self.sound.play_wav()
            if self.config.getboolean("General", "in_loop"):
                self.timer_sl.start(self.sound.duration())

    def closeEvent(self, a0: QCloseEvent):
        save_geometry(self.config, self.geometry())
        close_widget(self, self.config, NOTIFY_CFG)
        if self.play is not None:
            self.play.terminate()

    def timer_sl_tick(self):
        self.play = self.sound.play_wav()

    def timer_ac_tick(self):
        if self.delay <= 0:
            self.close()
        self.delay -= 1

    def timer_st_tick(self):
        self.ui.labelHeader.setText(QDateTime.currentDateTime().toString(self.time_format))

    def pushbutton_close_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(argv)
    translator = QTranslator()
    translator.load(get_loc_file())
    app.installTranslator(translator)
    dialog = NotifyForm()
    dialog.show()
    exit(app.exec_())
