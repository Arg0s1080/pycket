from ui.mail_window import *
from PyQt5.QtWidgets import QDialog
from configparser import ConfigParser
from os.path import join, exists
from os import getcwd, makedirs
import sys

config_file = join(getcwd(), "mail.cfg")


class MailForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MailDialog()
        self.ui.setupUi(self)
        self.config = ConfigParser()
        self.set_config()

    def set_config(self):
        if exists(config_file):
            self.config.read(config_file)
            self.ui.lineEditFrom.setText(self.config.get("Encrypted", "from"))
            self.ui.lineEditAlias.setText(self.config.get("Encrypted", "alias"))
            self.ui.lineEditServer.setText(self.config.get("General", "server"))
            self.ui.lineEditPassword.setText(self.config.get("Encrypted", "password"))
            self.ui.comboBoxEncrypt.setCurrentText(self.config.get("General", "encryption"))
            self.ui.spinBoxPort.setValue(self.config.getint("General", "port"))
            self.ui.lineEditTo.setText(self.config.get("Encrypted", "to"))
            self.ui.lineEditSubject.setText(self.config.get("Encrypted", "subject"))
            self.ui.plainTextEditBody.setPlainText(self.config.get("Encrypted", "body"))
        else:
            folder = config_file.split("/")[-1]
            if not exists(folder):
                makedirs(folder)
            self.config.add_section("General")
            self.config.set("General", "server", "smtp.gmail.com")
            self.config.set("General", "encryption", "TSL")
            self.config.set("General", "port", "587")
            self.config.add_section("Encrypted")
            self.config.set("Encrypted", "from", "")
            self.config.set("Encrypted", "alias", "")
            self.config.set("Encrypted", "password", "")
            self.config.set("Encrypted", "to", "")
            self.config.set("Encrypted", "subject", "")
            self.config.set("Encrypted", "body", "")
            self.config.set("Encrypted", "attachment", "")






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = MailForm()
    application.show()

    sys.exit(app.exec_())

