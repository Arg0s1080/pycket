from configparser import ConfigParser
from PyQt5.QtWidgets import QWidget


def save_geometry(config: ConfigParser, geometry: QWidget.geometry):
    config.set("Geometry", "x", str(geometry.x()))
    config.set("Geometry", "y", str(geometry.y()))
    config.set("Geometry", "width", str(geometry.width()))
    config.set("Geometry", "height", str(geogeometry.height()))


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
