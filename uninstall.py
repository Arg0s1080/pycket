from os import listdir, removedirs, remove
from os.path import exists, isdir, isfile, join, dirname, basename

print("Beeep")
"/usr/local/lib/python3.5/dist-packages/pycket-0.0.1-py3.5.egg/forms/setmain.py"

with open("./installed_files", "r") as f:
    lines = f.readlines()
    dirs = []
    for line in lines:
        ln = line.replace("\n", "")
        print("Deleting %s" % ln)
        remove(ln)
        _dir = dirname(ln)
        if _dir not in dirs:
            dirs.append(_dir)
    for _dir in dirs:
        if exists(_dir):
            if len(listdir(_dir)) == 0:
                print("Deleting %s" % _dir)
                removedirs(_dir)

