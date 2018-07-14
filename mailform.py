from ui.mail_window import Ui_MailDialog
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog, QMessageBox, QLineEdit, QFileDialog
from PyQt5.QtGui import QCloseEvent
from configparser import ConfigParser
from os.path import join, exists, dirname, expanduser
from os import getcwd, makedirs, remove
from scripts.aes import AESManaged, sha3_256
from math import pi, e
import sys


config_file = join(getcwd(), "mail.cfg")


class MailForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MailDialog()
        self.ui.setupUi(self)
        self.config = ConfigParser()
        self.control = "%.15f%s%.14f%s" % (pi, "ck", e, "t")
        self.attempts = 3
        self.cancel = None
        self.aes = None
        self.set_config()
        self.ui.lineEditFrom.textChanged.connect(self.line_edit_from_text_changed)
        self.ui.lineEditAlias.textChanged.connect(self.line_edit_alias_text_changed)
        self.ui.lineEditServer.textChanged.connect(self.line_edit_server_text_changed)
        self.ui.lineEditPassword.textChanged.connect(self.line_edit_password_text_changed)
        self.ui.lineEditTo.textChanged.connect(self.line_edit_to_text_changed)
        self.ui.lineEditSubject.textChanged.connect(self.line_edit_subject_text_changed)
        self.ui.plainTextEditBody.textChanged.connect(self.plain_text_edit_body_text_changed)
        self.ui.comboBoxEncrypt.currentIndexChanged.connect(self.combobox_encrypt_current_index_changed)
        self.ui.spinBoxPort.valueChanged.connect(self.spinbox_port_value_changed)
        self.ui.pushButtonAttach.clicked.connect(self.pushbutton_attach_clicked)
        self.ui.pushButtonCancel.clicked.connect(self.pushbutton_cancel_clicked)
        self.ui.pushButtonOk.clicked.connect(self.pushbutton_ok_clicked)
        self.ui.pushButtonTest.clicked.connect(self.pushbutton_test_clicked)

        print(self.geometry())

    def set_config(self):
        if exists(config_file):
            if self.attempts < 1:
                remove(config_file)
                msg = "Bad Password"
                self.msg_dlg(msg, "The data has been deleted", icon=QMessageBox.Critical,
                             details="The maximum number of attempts has been exceeded")
                exit(msg)
            pw = self.pw_dlg("Enter the password")
            if pw is not None:
                self.aes = AESManaged(pw)
                self.config.read(config_file)
                control = self.aes.decrypt(self.config.get("Encrypted", "control"))
                if control == self.control and control != -1:
                    x = self.config.getint("Geometry", "x")
                    y = self.config.getint("Geometry", "y")
                    width = self.config.getint("Geometry", "width")
                    height = self.config.getint("Geometry", "height")
                    self.setGeometry(x, y, width, height)
                    self.ui.lineEditFrom.setText(self.aes.decrypt(self.config.get("Encrypted", "from")))
                    self.ui.lineEditAlias.setText(self.aes.decrypt(self.config.get("Encrypted", "alias")))
                    self.ui.lineEditServer.setText(self.config.get("General", "server"))
                    self.ui.lineEditPassword.setText(self.aes.decrypt(self.config.get("Encrypted", "password")))
                    self.ui.comboBoxEncrypt.setCurrentText(self.config.get("General", "encryption"))
                    self.ui.spinBoxPort.setValue(self.config.getint("General", "port"))
                    self.ui.lineEditTo.setText(self.aes.decrypt(self.config.get("Encrypted", "to")))
                    self.ui.lineEditSubject.setText(self.aes.decrypt(self.config.get("Encrypted", "subject")))
                    self.ui.plainTextEditBody.setPlainText(self.aes.decrypt(self.config.get("Encrypted", "body")))

                else:
                    self.attempts -= 1
                    self.msg_dlg("Password incorrect", "Attempts: %d" % self.attempts)
                    self.set_config()
            else:
                exit(0)

        else:
            folder = dirname(config_file)
            if not exists(folder):
                makedirs(folder)
            pw = self.pw_dlg("Enter a new password:\n\nThis password will not be stored.\n"
                             "If this is lost or forgotten, the data can not be recovered")
            if pw is not None:
                if pw == self.pw_dlg("Type the password again"):
                    self.aes = AESManaged(pw)
                    self.config.add_section("Geometry")
                    self.config.set("Geometry", "x", "0")
                    self.config.set("Geometry", "y", "0")
                    self.config.set("Geometry", "width", "769")
                    self.config.set("Geometry", "height", "514")
                    self.config.add_section("General")
                    self.config.set("General", "server", "smtp.gmail.com")
                    self.config.set("General", "encryption", "TSL")
                    self.config.set("General", "port", "587")
                    self.config.add_section("Encrypted")
                    empty = self.aes.encrypt("")
                    self.config.set("Encrypted", "control", self.aes.encrypt(self.control))
                    self.config.set("Encrypted", "from", empty)
                    self.config.set("Encrypted", "alias", empty)
                    self.config.set("Encrypted", "password", empty)
                    self.config.set("Encrypted", "to", empty)
                    self.config.set("Encrypted", "subject", empty)
                    self.config.set("Encrypted", "body", empty)
                    self.config.set("Encrypted", "attachment", empty)

                    with open(config_file, "w") as file:
                        self.config.write(file)
                else:
                    self.msg_dlg("Both string do not match", icon=QMessageBox.Warning)
                    self.set_config()
            else:
                exit(0)

    def closeEvent(self, a0: QCloseEvent):
        geometry = self.geometry()
        self.config.set("Geometry", "x", str(geometry.x()))
        self.config.set("Geometry", "y", str(geometry.y()))
        self.config.set("Geometry", "width", str(geometry.width()))
        self.config.set("Geometry", "height", str(geometry.height()))
        if not self.cancel:
            with open(config_file, "w") as file:
                self.config.write(file)
        application.close()
        print("Goodbye!")

    def line_edit_from_text_changed(self):
        self.config.set("Encrypted", "from", self.aes.encrypt(self.ui.lineEditFrom.text()))

    def line_edit_alias_text_changed(self):
        self.config.set("Encrypted", "alias", self.aes.encrypt(self.ui.lineEditAlias.text()))

    def line_edit_server_text_changed(self):
        self.config.set("General", "server", self.ui.lineEditServer.text())

    def line_edit_password_text_changed(self):
        self.config.set("Encrypted", "password", self.aes.encrypt(self.ui.lineEditPassword.text()))

    def line_edit_to_text_changed(self):
        self.config.set("Encrypted", "to", self.aes.encrypt(self.ui.lineEditTo.text()))

    def line_edit_subject_text_changed(self):
        self.config.set("Encrypted", "subject", self.aes.encrypt(self.ui.lineEditSubject.text()))

    def plain_text_edit_body_text_changed(self):
        self.config.set("Encrypted", "body", self.aes.encrypt(self.ui.plainTextEditBody.toPlainText()))

    def combobox_encrypt_current_index_changed(self):
        encrypt = self.ui.comboBoxEncrypt.currentText()
        if encrypt == "TSL":
            port = 587
        elif encrypt == "SSL":
            port = 465
        else:
            port = 25
        self.ui.spinBoxPort.setValue(port)
        self.config.set("General", "encryption", self.ui.comboBoxEncrypt.currentText())

    def spinbox_port_value_changed(self):
        self.config.set("General", "port", str(self.ui.spinBoxPort.value()))

    def pushbutton_attach_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        attachment = self.aes.decrypt(self.config.get("Encrypted", "attachment"))
        directory = dirname(attachment) or expanduser("~")
        filename, _ = QFileDialog.getOpenFileName(self, "Select a file", directory, "All Files (*)", options=options)
        if filename:
            self.config.set("Encrypted", "attachment", self.aes.encrypt(filename))

    def pushbutton_cancel_clicked(self):
        self.cancel = True
        application.close()

    @staticmethod
    def pushbutton_ok_clicked():
        application.close()

    def pushbutton_test_clicked(self):
        print(self.geometry())
        print(self.geometry().x())
        print(self.geometry().y())
        print(self.geometry().width())
        print(self.geometry().center())

    @staticmethod
    def pw_dlg(msg):
        dlg = QInputDialog()
        txt, ok = dlg.getText(None, "Mail Settings Password", msg, QLineEdit.Password)
        if ok:
            return txt
        return

    @staticmethod
    def msg_dlg(body, info="", buttons=QMessageBox.Ok, icon=QMessageBox.Information, details=""):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(body)
        msg.setInformativeText(info)
        msg.setWindowTitle("Pycket")
        msg.setStandardButtons(buttons)

        if details != "":
            msg.setDetailedText(details)

        return msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = MailForm()
    application.show()

    sys.exit(app.exec_())

