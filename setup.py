#!/usr/bin/python3
# -*- coding: UTF8 -*-

#from setuptools import setup
from distutils.core import setup
from setuptools.command.install import install
from os import path, listdir, chmod
from os.path import join, exists, isfile, basename, realpath, dirname
from pycket import __version__ as version
from pycket.misc.paths import TRANSLATION_PTH

PARENT = realpath(dirname(__file__))

# TODO: Delete #############################################################
from pycket.misc.paths import provisional
if provisional:
    print("PROVISIONAL PATHS")
    if input("Press 'X' to continue. (Other key to exit)").upper() != "X":
        exit("ABORTED: PROVISIONAL PATHS")
# TODO #####################################################################

try:
    with open(path.join(PARENT, "README.rst"), 'r') as readme:
        long_description = readme.read()
except FileNotFoundError:
    # TODO: Make README
    long_description = "System monitor that can react to user chosen conditions"


def locale_files() -> list:
    tr_src = path.join(PARENT, "translate")
    locs = [item for item in listdir(tr_src) if exists(join(tr_src, item, "pycket.qm"))]
    return [(TRANSLATION_PTH % loc, ["translate/%s/pycket.qm" % loc]) for loc in locs]


def get_files(dir_) -> list:
    return ["%s/%s" % (dir_, file) for file in listdir(join(PARENT, dir_)) if isfile(join(PARENT, dir_, file))]


data_files = [
        ("/usr/share/applications", ["launchers/pycket.desktop"]),
        ("/usr/share/pixmaps", ["pycket/resources/images/256x256/pycket.png"]),
        ("/usr/share/sounds/pycket", get_files("pycket/resources/sounds")),
    ] + locale_files()


def get_data_files():
    return [join(pth, basename(file)) for pth, files in data_files for file in files]


class ChangeMode(install):
    # Based Oz123's answer in https://stackoverflow.com/questions/5932804/set-file-permissions-in-setup-py-file
    def run(self):
        def change_mode(files: list):
            for file in files:
                mode = 0o664 if not file.endswith("/pycket") else 0o755
                print("Changing permissions of %s to %s" % (file, oct(mode)))
                chmod(file, mode)
        install.run(self)
        change_mode(self.get_outputs())
        change_mode(get_data_files())


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
    scripts=['launchers/pycket'],
    packages=["pycket", "pycket/common", "pycket/forms", "pycket/misc", "pycket/scripts", "pycket/ui", "statux"],
    #packages=["pycket", "statux"],
    #include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities"
    ],
    data_files=data_files,
    cmdclass={'install': ChangeMode}
)
