from os.path import join, expanduser
from os import getcwd
from math import pi, e

HOME = expanduser("~")
CONFIG = join(HOME, ".config", "pycket")
# MAIN_CFG = join(CONFIG, "config.cfg")
# MAIL_CFG = join(CONFIG, "mail.cfg")
# NOTIFY_CFG = join(CONFIG, "notify.cfg")

# todo change
MAIN_CFG = join(getcwd(), "cfg", "config.cfg")
MAIL_CFG = join(getcwd(), "cfg", "mail.cfg")
NOTIFY_CFG = join(getcwd(), "cfg", "notify.cfg")

# todo delete
GMAIL_APP_PW = "geuipfkvdhhxtmxi"
CONTROL = "%.15f%s%.14f%s" % (pi, "ck", e, "t")

