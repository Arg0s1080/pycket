from base64 import b64encode, b64decode
from hashlib import sha3_256
from Crypto import Random
from Crypto.Cipher import AES


class AESManaged:
    def __init__(self, key: str):
        self.key = sha3_256(key.encode()).digest()

    def encrypt(self, msg: str) -> str:
        pad = lambda s: s + ((AES.block_size - len(s) % AES.block_size) *
                             chr(AES.block_size - len(s) % AES.block_size)).encode()
        msg = pad(msg.encode())
        iv = Random.new().read(16)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(msg)).decode()

    def decrypt(self, encrypted_msg: str):
        encrypted_msg = b64decode(encrypted_msg.encode())
        iv = encrypted_msg[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        unpad = lambda s: s[:-ord(s[len(s) - 1:])]
        try:
            return unpad(cipher.decrypt(encrypted_msg[AES.block_size:])).decode()
        except UnicodeDecodeError:
            # Debug
            print("UnicodeDecodeError from decrypt")
            return -1


class BadPasswordError(ValueError):
    # TODO: Move class to other file.
    def __init__(self, msg="", cause=""):
        self.cause = cause
        self.msg = msg or "Bad password"
        self.args = (self.msg, self.cause)
        super(BadPasswordError, self).__init__(self.msg, self.cause)

    def __str__(self):
        return str(self.args)