import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from enum import Enum
from os.path import isfile
from re import match


class Encrypt(Enum):
    ANY = 0,
    TSL = 1,
    SSL = 2


class SMPTMail:
    def __init__(self, server: str, port: int, from_address: str, password: str, to: str, from_alias="",
                 subject="", body="", attachment=None, encrypt=Encrypt.TSL, debug_level=False):
        self.server = server
        self.port = port
        self.from_ = from_address
        self.password = password
        self.to = to
        self.from_alias = from_alias
        self.subject = subject
        self.body = body
        self.attachment = attachment
        self.encrypt = encrypt
        self.debug_level = debug_level

    def send(self):
        msg = MIMEMultipart()
        msg["From"] = self.from_alias
        msg["To"] = self._verify(self.to)
        msg["Subject"] = self.subject
        msg.attach(MIMEText(self.body, "plain"))

        if self.attachment is not None:
            if isfile(self.attachment):
                with open(self.attachment, "rb") as file:
                    piece = MIMEBase("application", "octet-stream")
                    piece.set_payload(file.read())
                    encoders.encode_base64(piece)
                    piece.add_header('Content-Disposition', "attachment; filename= %s" % self.attachment.split("/")[-1])
                    msg.attach(piece)
            else:
                raise FileNotFoundError("The attachment doesn't exist or is not a valid file", self.attachment)

        if self.encrypt == Encrypt.SSL:
            server = smtplib.SMTP_SSL(self.server, self.port)
            server.ehlo()
        else:
            server = smtplib.SMTP(self.server, self.port)
            if self.encrypt == Encrypt.TSL:
                server.ehlo()
                server.starttls()
            else:
                server.ehlo_or_helo_if_needed()
        server.set_debuglevel(self.debug_level)
        server.login(self.from_, self.password)
        mail = msg.as_string()
        server.sendmail(self._verify(self.from_), self.to, mail)
        server.quit()

    @staticmethod
    def _verify(address: str):
        if match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", address):
            return address
        else:
            raise ValueError("Bad email address syntax", address)

"""
# TODO: Delete
from provisional import GMAIL_APP_PW
mail_ = SMPTMail(server="smtp.gmail.com", port=587,
                 from_address="ivan.rincon76@gmail.com",
                 password=GMAIL_APP_PW,  # GMAIL App password
                 to="ivan.rincon@ymail.com",
                 subject="Mensaje de prueba III a a yahoo 2",
                 body="únó dòŝ trêŝ",
                 attachment="/home/ivan/Escritorio/tabla.ods",
                 encrypt=Encrypt.TSL,
                 debug_level=True)
mail_.send()
"""
# TSL 587
# SSL 465
# ANY 25
