from os import getuid
from os.path import exists
from subprocess import Popen
from shlex import split

getuid() and exit("This file must be run with root privileges.")


sp = Popen(split("python3 setup.py install --record ./installed_files"))
_, std_err = sp.communicate(timeout=1)
if not std_err:
    print("Pycket has been installed")
else:
    print("An error occurred during installation")
    Popen(split("python3 uninstall.py"))
