import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from enum import Enum
from os.path import isfile


class Encrypt(Enum):
    ANY = 0,
    STARTTSL = 1,
    SSL = 2


class SendMail:
    def __init__(self, smpt_server: str, port: int, from_address: str, password: str, to: str,
                 from_alias="", subject="", body="", attachment=None, encrypt=Encrypt.STARTTSL):
        self.smpt_server = smpt_server
        self.port = port
        self.from_ = from_address
        self.password = password
        self.to = to
        self.from_alias = from_alias
        self.subject = subject
        self.body = body
        self.attachment = attachment
        self.encrypt = encrypt

    def send(self):
        msg = MIMEMultipart()
        msg["From"] = self.from_alias
        msg["To"] = self.to
        msg["Subject"] = self.subject
        msg.attach(MIMEText(self.body, "plain"))

        if self.attachment is not None:
            if isfile(self.attachment):
                with open(self.attachment, "rb") as file:
                    piece = MIMEBase('application', 'octet-stream')
                    piece.set_payload(file.read())
                    encoders.encode_base64(piece)
                    piece.add_header('Content-Disposition', "attachment; filename= %s" % self.attachment.split("/")[-1])
                    msg.attach(piece)
            else:
                raise FileNotFoundError("The attachment doesn't exist or is not a valid file", self.attachment)

        if self.encrypt == Encrypt.SSL:
            server = smtplib.SMTP_SSL(self.smpt_server, self.port)
            server.ehlo()
        else:
            server = smtplib.SMTP(self.smpt_server, self.port)
            if self.encrypt == Encrypt.STARTTSL:
                server.ehlo()
                server.starttls()
            else:
                server.ehlo_or_helo_if_needed()

        server.login(self.from_, self.password)
        mail = msg.as_string()
        server.sendmail(self.from_, self.to, mail)
        server.quit()


mail_ = SendMail(smpt_server="smtp.gmail.com", port=587,
                 from_address="ivan.rincon76@gmail.com",
                 password="ofocabanisphhbbx",  # GMAIL App password
                 to="ivan.rincon@ymail.com",
                 subject="prueba a yahoo 2",
                 body="únó dòŝ trêŝ",
                 attachment="/home/ivan/Escritorio/tabla.ods",
                 encrypt=Encrypt.STARTTSL)
mail_.send()
