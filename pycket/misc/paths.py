from os.path import join, expanduser, realpath, dirname, pardir
from os import getcwd
from math import pi, e

provisional = True

HOME = expanduser("~")
PARENT = realpath(join(dirname(__file__), pardir))
CONFIG = join(HOME, ".config", "pycket")
SHARE = join("/", "usr", "share")
LOCALE_PTH = join(SHARE, "locale")

if not provisional:
    MAIN_CFG = join(CONFIG, "config.cfg")
    MAIL_CFG = join(CONFIG, "mail.cfg")
    NOTIFY_CFG = join(CONFIG, "notify.cfg")
    LAUNCHERS = join(SHARE, "applications")
    SOUNDS_PTH = join(SHARE, "sounds", "pycket")
    TRANSLATION_PTH = join(LOCALE_PTH, "%s", "LC_MESSAGES")
else:
    MAIN_CFG = join(getcwd(), "cfg", "config.cfg")
    MAIL_CFG = join(getcwd(), "cfg", "mail.cfg")
    NOTIFY_CFG = join(getcwd(), "cfg", "notify.cfg")
    SOUNDS_PTH = join(PARENT, "resources", "sounds")
    PARENT = realpath(join(PARENT, pardir))
    TRANSLATION_PTH = realpath(join(PARENT, "translate", "%s"))

# todo delete
GMAIL_APP_PW = "geuipfkvdhhxtmxi"
CONTROL = "%.15f%s%.14f%s" % (pi, "ck", e, "t")

