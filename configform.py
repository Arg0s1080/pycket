from ui.settings_window import *
from configparser import ConfigParser
from os.path import join
from os import getcwd
import sys

config_file = join(getcwd(), "config.cfg")


class ConfigForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.config = ConfigParser()
        self.get_config()

    def get_config(self):
        self.config.read(config_file)
        self.ui.lineEditShutdown.setText(self.config.get("Commands", "shutdown"))
        self.ui.lineEditReboot.setText(self.config.get("Commands", "reboot"))
        self.ui.lineEditCloseSession.setText(self.config.get("Commands", "close_session"))
        self.ui.lineEditSuspend.setText(self.config.get("Commands", "suspend"))
        self.ui.lineEditHibernate.setText(self.config.get("Commands", "hibernate"))
        self.ui.lineEditExecute.setText(self.config.get("Commands", "execute"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ConfigForm()
    application.show()

    sys.exit(app.exec_())