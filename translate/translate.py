from os.path import join, pardir, isdir, isfile
from os import getcwd, listdir
from subprocess import run, PIPE, Popen

# NOTE: To make pycket.ts files run 'pylupdate5 qt_tr.pro' (See qt_tr.pro file)


class Translate:
    def __init__(self):
        self._translate_path = getcwd()

    def lrelease(self):
        for item in listdir(self._translate_path):
            if isdir(item):
                pth = join(self._translate_path, item)
                for file in listdir(pth):
                    if file == "pycket.ts":
                        proc = Popen(["lrelease", join(pth, file)], stdout=PIPE, stderr=PIPE)
                        return_code = proc.wait()
                        if return_code == 0:
                            print(proc.stdout.read().decode())
                        else:
                            print(proc.stderr.read().decode())


tr = Translate()
tr.lrelease()
