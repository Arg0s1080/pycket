from pycket.ui.mail_window import Ui_MailDialog
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QCloseEvent
from os.path import expanduser
from os import remove
from pycket.scripts.aes import AESManaged
from pycket.scripts.sendmail import SendMail, CONTROL
from sys import argv, exit
from pycket.common.common import *
from pycket.common.errors import BadPasswordError

# TODO: Delete
from pycket.misc.paths import MAIL_CFG


class MailForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MailDialog()
        self.ui.setupUi(self)
        self.config = ConfigParser()
        self.control = CONTROL
        self.attempts = 3
        self.cancel = None
        self.aes = None
        self.title = self.tr("Mail Settings Password")
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

    def set_config(self):
        if exists(MAIL_CFG):
            if self.attempts < 1:
                remove(MAIL_CFG)
                msg = self.tr("Bad Password")
                msg_dlg(msg, self.tr("The data has been deleted"), icon=QMessageBox.Critical,
                        details=self.tr("The maximum number of attempts has been exceeded"))
                exit(msg)
            pw = pw_dlg(self.tr("Enter the password"), self.title)
            if pw is not None:
                self.aes = AESManaged(pw)
                self.config.read(MAIL_CFG)
                cntrl = self.aes.decrypt(self.config.get("Encrypted", "control"))
                if cntrl == CONTROL and cntrl != -1:
                    set_geometry(self.config, self.setGeometry)
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
                    msg_dlg(self.tr("Password incorrect"), self.tr("Attempts: %d") % self.attempts)
                    self.set_config()
            else:
                exit(0)

        else:
            make_cfg_folder(MAIL_CFG)
            pw = pw_dlg(self.tr("Enter a new password:\n\nThis password will not be stored.\nIf this is lost "
                                "or forgotten, the data can not be recovered"), self.title)
            if pw is not None:
                if pw == self.pw_dlg(self.tr("Type the password again")):
                    self.aes = AESManaged(pw)
                    make_geometry(self.config, 769, 514)
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
                    write_config(self.config, MAIL_CFG)

                else:
                    msg_dlg(self.tr("Both string do not match"), icon=QMessageBox.Warning)
                    self.set_config()
            else:
                exit(0)

    def closeEvent(self, a0: QCloseEvent):
        save_geometry(self.config, self.geometry())
        close_widget(self, self.config, MAIL_CFG, self.cancel)

    def tr(self, sourceText: str, disambiguation: Optional[str] = ..., n: int = ...):
        return QCoreApplication.translate(name(self), sourceText)

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
        # TODO: to common
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        attachment = self.aes.decrypt(self.config.get("Encrypted", "attachment"))
        directory = dirname(attachment) or expanduser("~")
        filename, _ = QFileDialog.getOpenFileName(self, self.tr("Select a file"), directory,
                                                  self.tr("All Files (*)"), options=options)
        if filename:
            self.config.set("Encrypted", "attachment", self.aes.encrypt(filename))

    def pushbutton_cancel_clicked(self):
        self.cancel = True
        self.close()

    def pushbutton_ok_clicked(self):
        self.close()

    def pushbutton_test_clicked(self):
        if self.send_mail():
            msg_dlg(self.tr("Operation performed"), self.tr("Please, check your mailbox"))

    def send_mail(self):
        pw = pw_dlg(self.tr("Enter the password:"), self.title)
        ok = True
        if pw is not None:
            try:
                mail = SendMail(pw, MAIL_CFG)
                mail.send()
            except BadPasswordError as ex:
                ok = False
                msg_dlg(ex.msg, self.tr("Aborted operation"), icon=QMessageBox.Critical)
            except Exception as ex:
                ok = False
                msg_dlg("Mail error", "An error occurred while sending mail", icon=QMessageBox.Critical,
                        details="\n-".join(list(map(str, ex.args))))
            finally:
                return ok

if __name__ == "__main__":
    app = QApplication(argv)
    translator = QTranslator()
    translator.load(get_loc_file())
    app.installTranslator(translator)
    application = MailForm()
    application.show()
    exit(app.exec_())
