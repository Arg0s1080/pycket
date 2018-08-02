from configparser import ConfigParser
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QLocale
from sys import exc_info
from os.path import join, exists, dirname
from os import getcwd, makedirs
from subprocess import run, Popen, PIPE
from common.errors import ConfigFileNotFoundError


def msg_dlg(body, info="", buttons=QMessageBox.Ok, icon=QMessageBox.Information, details=""):
    msg = QMessageBox()

    msg.setIcon(icon)
    msg.setText(body)
    msg.setInformativeText(info)
    msg.setWindowTitle("Pycket")
    msg.setStandardButtons(buttons)

    if details != "":
        msg.setDetailedText(details)

    return msg.exec()


def get_loc_file(context):
    # Ex: if context == "main": loc_file = "./translate/main_es_ES.qm"
    locale = QLocale.system().name()
    path = join(getcwd().replace("forms", ""), "translate")
    loc_file = join(path, "%s_%s.qm" % (context, locale))
    if not exists(loc_file):
        loc_file = join(path, "%s_%s.qm" % (context, locale[:-3]))
    return loc_file


def close_widget(widget: QWidget, config: ConfigParser, file_cfg: str, cancel=False):
    try:
        if not cancel:
            write_config(config, file_cfg)
    except Exception as ex:
        err = ""
        for arg in exc_info():
            err += "! %s\n" % str(arg)
        msg_dlg("An unexpected error occurred:", ex.args[1], QMessageBox.Ok, QMessageBox.Warning, err)
    finally:
        widget.close()
        print("Goodbye!")


def save_geometry(config: ConfigParser, geometry: QWidget.geometry, section="Geometry"):
    config.set(section, "x", str(geometry.x()))
    config.set(section, "y", str(geometry.y()))
    config.set(section, "width", str(geometry.width()))
    config.set(section, "height", str(geometry.height()))


def set_geometry(config: ConfigParser, geometry: QWidget.setGeometry, section="Geometry"):
    x = config.getint(section, "x")
    y = config.getint(section, "y")
    width = config.getint(section, "width")
    height = config.getint(section, "height")
    geometry(x, y, width, height)


def make_geometry(config: ConfigParser, width: int, height: int, section="Geometry", x=0, y=0):
    config.add_section(section)
    config.set(section, "x", str(x))
    config.set(section, "y", str(y))
    config.set(section, "width", str(width))
    config.set(section, "height", str(height))


def execute(*args, **kwargs):
    return run(*args, **kwargs)


def exe_async(*args, **kwargs):
    return Popen(*args, **kwargs)


def test_cfg(cfg_file: str) -> str:
    if not exists(cfg_file):
        raise ConfigFileNotFoundError(cfg_file)
    return cfg_file


def make_cfg_folder(cfg_file: str):
    folder = dirname(cfg_file)
    if not exists(folder):
        makedirs(folder)


def write_config(config: ConfigParser, cfg_file: str):
    with open(cfg_file, "w") as cfg_file:
        config.write(cfg_file)
