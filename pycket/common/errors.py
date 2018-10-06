import errno


class BadPasswordError(ValueError):
    def __init__(self, msg="", cause=""):
        self.cause = cause
        self.msg = msg or "Bad password"
        self.args = (self.msg, self.cause)
        super(BadPasswordError, self).__init__(self.msg, self.cause)

    def __str__(self):
        return str(self.args)


class ConfigFileNotFoundError(FileNotFoundError):
    def __init__(self, filename):
        self.filename = filename
        self.strerror = "No such config file"
        super(FileNotFoundError, self).__init__(errno.ENOENT, self.strerror, self.filename)
