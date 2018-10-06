#!/usr/bin/python3
# -*- coding: UTF8 -*-

#from setuptools import setup
from distutils.core import setup
from setuptools.command.install import install
from os import path, listdir, chmod
from os.path import join, exists, isfile, basename
from pycket.common import __version__ as version
from misc.paths import PARENT, TRANSLATION_PTH


try:
    with open(path.join(PARENT, "README.rst"), 'r') as readme:
        long_description = readme.read()
except FileNotFoundError:
    long_description = "System monitor that can react to user chosen conditions"


def locale_files() -> list:
    tr_src = path.join(PARENT, "translate")
    locs = [item for item in listdir(tr_src) if exists(join(tr_src, item, "pycket.qm"))]
    return [(TRANSLATION_PTH % loc, ["translate/%s/pycket.qm" % loc]) for loc in locs]


def get_files(dir_) -> list:
    return ["%s/%s" % (dir_, file) for file in listdir(join(PARENT, dir_)) if isfile(join(PARENT, dir_, file))]


data_files = [
        ("/usr/share/applications", ["pycket.desktop"]),
        ("/usr/share/pixmaps", ["resources/images/256x256/pycket.png"]),
        ("/usr/share/sounds/pycket", get_files("resources/sounds")),
    ] + locale_files()


def get_data_files():
    return [join(pth, basename(file)) for pth, files in data_files for file in files]


class ChangePermissions(install):
    # Based Oz123's answer in https://stackoverflow.com/questions/5932804/set-file-permissions-in-setup-py-file
    def run(self):
        mode = 0o644
        install.run(self)
        for file in get_data_files():
            print("Changing permissions of %s to %s" % (file, oct(mode)))
            chmod(file, mode)

setup(
    name="pycket",
    version=version,
    description="System monitor that can react to chosen conditions by the user",
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
    data_files=data_files,
    cmdclass={'install': ChangePermissions}
)


def change_permissions():
    for file in get_data_files():
        chmod(file, 0o755)
