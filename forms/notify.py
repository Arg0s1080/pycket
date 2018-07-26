from ui.notify_window import Ui_NotifyDialog
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QCloseEvent, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime
from configparser import ConfigParser
from sys import argv, exit
from os.path import exists, join
from common.common import test_cfg

# TODO: Move
from provisional import NOTIFY_CFG

class NotifyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NotifyDialog()
        self.ui.setupUi(self)
        self.config = ConfigParser()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_tick)
        self.delay = None
        self.set_config()

    def set_config(self):
        self.config.read(test_cfg(NOTIFY_CFG))
        self.setWindowFlag(Qt.WindowStaysOnTopHint, self.config.getboolean("General", "on_top"))
        self.delay = self.config.getint("General", "seconds")
        self.config.getboolean("General", "auto_close") and self.timer.start(1000)
        self.setWindowOpacity(self.config.getfloat("General", "opacity") / 100)
        # TODO:
        show_time = self.config.getboolean("General", "show_time")
        # print(QDateTime.currentDateTime().toString("hh:mm:ss"))

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

    def timer_tick(self):
        if self.delay <= 0:
            self.close()
        self.delay -= 1


if __name__ == '__main__':
    app = QApplication(argv)
    dialog = NotifyForm()
    dialog.show()
    exit(app.exec_())
