#!/usr/bin/python3
# -*- coding: UTF8 -*-

from setuptools import setup
from os import path, listdir
from os.path import join, exists, isdir
from common import __version__ as version
from misc.paths import PARENT, LOCALE_PTH, TRANSLATION_PTH


try:
    with open(path.join(PARENT, "README.rst"), 'r') as readme:
        long_description = readme.read()
except FileNotFoundError:
    long_description = "System monitor that can react to user chosen conditions"


def locale_files() -> list:
    tr_src = path.join(PARENT, "translate")
    locs = [item for item in listdir(tr_src) if isdir(join("%s/%s" % (tr_src, item)))]
    return [(TRANSLATION_PTH % loc, ["translate/%s/pycket.qm" % loc]) for loc in locs]


def get_files(dir_) -> list:
    return ["%s/%s" % (dir_, file) for file in listdir(join(PARENT, dir_)) if not isdir(file)]

input()
setup(
    name="pycket",
    version=version,
    description="System monitor that can react to user chosen conditions",
    license="GPLv3",
    long_description=long_description,
    author='Ivan Rincon',
    author_email='ivan.rincon76@gmail.com',
    url="https://github.com/Arg0s1080/pycket",
    keywords="system monitor scheduler ",
    platforms=['Linux'],
    packages=["common", "forms", "misc", "scripts", "statux", "ui"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities"
    ],
    data_files=[
        ("/usr/share/applications", ["data/pycket.desktop"]),
        ("/usr/share/pixmaps", ["resources/pycket.png"]),
        ("/usr/share/sounds/pycket", get_files("resources/sounds")),
        ('/usr/share/multibootusb/data/tools', ["data/tools/mbr.bin"])
    ] + locale_files()
)
