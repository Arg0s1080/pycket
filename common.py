from configparser import ConfigParser
from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import QLocale
from sys import exc_info
from os.path import join, exists
from os import getcwd


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
    path = join(getcwd(), "translate")
    loc_file = join(path, "%s_%s.qm" % (context, locale))
    if not exists(loc_file):
        loc_file = join(path, "%s_%s.qm" % (context, locale[:-3]))
    return loc_file


def close_widget(widget: QWidget, config: ConfigParser, file_cfg: str, cancel=False):
    try:
        if not cancel:
            with open(file_cfg, "w") as file:
                config.write(file)
    except Exception as ex:
        err = ""
        for arg in exc_info():
            err += "! %s\n" % str(arg)
        msg_dlg("An unexpected error occurred:", ex.args[1], QMessageBox.Ok, QMessageBox.Warning, err)
    finally:
        widget.close()
        print("Goodbye!")


def save_geometry(config: ConfigParser, geometry: QWidget.geometry):
    config.set("Geometry", "x", str(geometry.x()))
    config.set("Geometry", "y", str(geometry.y()))
    config.set("Geometry", "width", str(geometry.width()))
    config.set("Geometry", "height", str(geometry.height()))


def set_geometry(config: ConfigParser, geometry: QWidget.setGeometry):
    x = config.getint("Geometry", "x")
    y = config.getint("Geometry", "y")
    width = config.getint("Geometry", "width")
    height = config.getint("Geometry", "height")
    geometry(x, y, width, height)


def make_geometry(config: ConfigParser, width: int, height: int, x=0, y=0):
    config.add_section("Geometry")
    config.set("Geometry", "x", str(x))
    config.set("Geometry", "y", str(y))
    config.set("Geometry", "width", str(width))
    config.set("Geometry", "height", str(height))
