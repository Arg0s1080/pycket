from configparser import ConfigParser
from os.path import exists

DE = "Desktop Entry"

config = ConfigParser()

config.optionxform = lambda option: option

config.add_section(DE)
config.set(DE, "Encoding", "UTF-8")
config.set(DE, "Name", "pycket")
config.set(DE, "Comment", "Action launcher based on system activity")
config.set(DE, "Exec", "/usr/bin/pycket")
config.set(DE, "Icon", "/usr/local/share/icons/flameshot.png")
config.set(DE, "Type", "Application")
config.set(DE, "Categories", "Utility;System;Monitor;Qt")

with open()