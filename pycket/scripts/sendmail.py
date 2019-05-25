#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# GNU General Public License v3.0
#
# Permissions of this strong copyleft license are conditioned on making available
# complete source code of licensed works and modifications, which include larger works
# using a licensed work, under the same license. Copyright and license notices must be
# preserved. Contributors provide an express grant of patent rights.
#
# For more information on this, and how to apply and follow theGNU GPL, see:
# http://www.gnu.org/licenses
#
# (ɔ) Iván Rincón 2019

from configparser import ConfigParser
from pycket.scripts.aes import AESManaged
from pycket.common.errors import BadPasswordError
from pycket.common.common import test_cfg
from pycket.scripts.smtp import SMPTMail, Encrypt
from math import pi, e


# TODO: Delete

CONTROL = "%.15f%s%.14f%s" % (pi, "ck", e, "t")


class SendMail:
    def __init__(self, password: str, mail_cfg: str):
        self.aes = AESManaged(password)
        self.config = ConfigParser()
        self.config.read(test_cfg(mail_cfg))
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

