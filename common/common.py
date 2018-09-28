from configparser import ConfigParser
from PyQt5.QtWidgets import QWidget, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtCore import QLocale, QCoreApplication
from sys import exc_info
from os.path import join, exists, dirname, isdir
from os import makedirs, listdir
from subprocess import run, Popen
from misc.paths import LOCALE_PTH, TRANSLATION_PTH, PARENT
from common.errors import ConfigFileNotFoundError
from typing import Optional


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


def pw_dlg(msg, title="Pycket"):
    dlg = QInputDialog()
    txt, ok = dlg.getText(None, title, msg, QLineEdit.Password)
    if ok:
        return txt
    return


def translationsOLD() -> list:
    return [file[7:-3] for file in listdir(join(PARENT, "translate")) if file.endswith(".qm")]
def get_loc_fileOLD():
    filename = "pycket_%s.qm"
    def get_file():
        return join(path, filename % locale)
    locale = QLocale.system().name()
    path = join(PARENT, "translate")
    loc_file = get_file()
    if not exists(loc_file):
        locale = locale[:-3]
        if exists(get_file()):
            loc_file = get_file()
        else:
            compatibles = [filename % tr for tr in translations() if tr.startswith(locale)]
            if len(compatibles) > 0:
                # TODO: if len(compatible) > 1: can choose
                loc_file = join(path, compatibles[0])
    return loc_file


def translations():
    locs = [item for item in listdir(LOCALE_PTH) if isdir(join(LOCALE_PTH, item))]
    return [loc for loc in locs if exists(join(TRANSLATION_PTH % loc, "pycket.qm"))]


def get_loc_file():
    # E.g.:
    # locale = de_AT
    # translations = [es, de_DE, de_LU, en_GB, it]
    # - Search for de_AT -> Not found
    # - Search for de    -> Not found
    # - Search for de_*  -> Found = [de_DE, de_LU] -> Choose Found[0] -> /usr/share/locale/de_DE/LC_MESSAGES/pycket.qm
    locale = QLocale.system().name()
    trl = lambda x: join(TRANSLATION_PTH % x, "pycket.qm")
    loc_file = trl(locale)
    if not exists(loc_file) and len(locale) >= 5:
        locale = locale[:-3]
        loc_file = trl(locale)
        if not exists(loc_file):
            compatibles = [TRANSLATION_PTH % tr for tr in translations() if tr.startswith(locale)]
            loc_file = compatibles[0]
    return loc_file


def trl(cls, string: str):
    return QCoreApplication.translate(cls.__class__.__name__, string)


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


def name(cls):
    return cls.__class__.__name__

