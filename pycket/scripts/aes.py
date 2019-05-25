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

from base64 import b64encode, b64decode

from hashlib import sha256
from Crypto import Random
from Crypto.Cipher import AES


class AESManaged:
    def __init__(self, key: str):
        self.key = sha256(key.encode()).digest()

    def encrypt(self, msg: str) -> str:
        pad = lambda s: s + ((AES.block_size - len(s) % AES.block_size) *
                             chr(AES.block_size - len(s) % AES.block_size)).encode()
        msg = pad(msg.encode())
        iv = Random.new().read(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(msg)).decode()

    def decrypt(self, encrypted_msg: str) -> str:
        encrypted_msg = b64decode(encrypted_msg.encode())
        iv = encrypted_msg[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        try:
            return unpad(cipher.decrypt(encrypted_msg[AES.block_size:])).decode()
        except UnicodeDecodeError:
            # Debug
            print("UnicodeDecodeError from decrypt")
            raise

