from configparser import ConfigParser
from scripts.aes import AESManaged
from scripts.smtp import SMPTMail, Encrypt
from os.path import join
from os import getcwd

config_file = join(getcwd(), "mail.cfg")


class SendMail:
    def __init__(self, password: str, mail_cfg: str):
        self.aes = AESManaged(password)
        self.config = ConfigParser()
        self.config.read(mail_cfg)
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
        self.attachment = self.attachment or None
        mail = SMPTMail(self.server, self.port, self.from_, self.pw, self.to, self.alias,
                        self.subject, self.body, self.attachment, self.encrypt)
        mail.send()

