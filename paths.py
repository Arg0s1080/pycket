from os.path import join, expanduser, realpath, dirname, pardir
from os import getcwd
from math import pi, e

HOME = expanduser("~")
PARENT = realpath(join(pardir, dirname(__file__)))
CONFIG = join(HOME, ".config", "pycket")
# MAIN_CFG = join(CONFIG, "config.cfg")
# MAIL_CFG = join(CONFIG, "mail.cfg")
# NOTIFY_CFG = join(CONFIG, "notify.cfg")
SHARE = join("/", "usr", "share")
LAUNCHERS = join(SHARE, "applications")
# SOUNDS_PTH = join(SHARE, "sounds", "pycket")
LOCALE_PTH = join(SHARE, "locale")
# TRANSLATION_PTH = join(LOCALE_PTH, "%s", "LC_MESSAGES")

# Provisional
MAIN_CFG = join(getcwd(), "cfg", "config.cfg")
MAIL_CFG = join(getcwd(), "cfg", "mail.cfg")
NOTIFY_CFG = join(getcwd(), "cfg", "notify.cfg")
SOUNDS_PTH = join(PARENT, "resources", "sounds")
TRANSLATION_PTH = join(PARENT, "translate", "%s")
# todo delete
GMAIL_APP_PW = "geuipfkvdhhxtmxi"
CONTROL = "%.15f%s%.14f%s" % (pi, "ck", e, "t")

