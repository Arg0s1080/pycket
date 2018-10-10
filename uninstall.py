from os import listdir, removedirs, remove, getuid
from os.path import exists, isdir, isfile, join, dirname, basename, pardir, realpath

getuid() and exit("This file must be run with root privileges.")

RED = '\033[91m%s\033[0m'
GREEN = '\33[32m%s\033[0m'
YELLOW = '\33[33m%s\033[0m'

with open("./installed_files", "r") as f:
    lines = f.readlines()
    dirs = []
    ok = True
    try:
        for line in lines:
            ln = line.replace("\n", "")
            try:
                remove(ln)
                print(GREEN % "Deleting %s" % ln)
                _dir = dirname(ln)
                if _dir not in dirs:
                    dirs.append(_dir)
            except FileNotFoundError as error:
                print(RED % "Error: %s not found" % error.filename)

        for _dir in dirs:
            if exists(_dir):
                if len(listdir(_dir)) == 0:
                    removedirs(_dir)
                    if not exists(_dir):
                        print(GREEN % "Removing dir %s" % _dir)
    except FileNotFoundError as error:
        ok &=False
        print("error>>>>>>", error.args, error.filename, error.filename2)