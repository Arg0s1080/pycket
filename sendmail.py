from configparser import ConfigParser
from scripts.aes import AESManaged, BadPasswordError
from scripts.smtp import SMPTMail, Encrypt
from os.path import join
from os import getcwd
from math import pi, e

config_file = join(getcwd(), "mail.cfg")
CONTROL = "%.15f%s%.14f%s" % (pi, "ck", e, "t")


class SendMail:
    def __init__(self, password: str, mail_cfg: str):
        self.aes = AESManaged(password)
        self.config = ConfigParser()
        self.config.read(mail_cfg)
        self._verify(password)
        self.server = self.config.get("General", "server")
        self.port = self.config.getint("General", "port")
        self.from_ = self.aes.decrypt(self.config.get("Encrypted", "from"))
        self.pw = self.aes.decrypt(self.config.get("Encrypted", "password"))
        self.to = self.aes.decrypt(self.config.get("Encrypted", "to"))
        self.alias = self.aes.decrypt(self.config.get("Encrypted", "alias"))
        self.subject = self.aes.decrypt(self.config.get("Encrypted", "subject"))
        self.body = self.aes.decrypt(self.config.get("Encrypted", "body"))
        self.attachment = self.aes.decrypt(self.config.get("Encrypted", "attachment"))
        self.encrypt = Encrypt[self.config.get("General", "encryption")]

    def send(self):
        mail = SMPTMail(self.server, self.port, self.from_, self.pw, self.to, self.alias,
                        self.subject, self.body, self.attachment or None, self.encrypt)
        mail.send()

    def _verify(self, pw):
        if CONTROL != self.aes.decrypt(self.config.get("Encrypted", "control")):
            raise BadPasswordError(cause=pw)
