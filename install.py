from os import getuid
from os.path import exists
from subprocess import Popen

if getuid() != 0:
    print("This file must be run with root privileges.")
    exit()

sp = Popen("python3 setup.py install --record ./installed_files")
_, std_err = sp.communicate(timeout=1)
if std_err == 0:
    print("Pycket has been installed")
else:
    print("An error occurred during installation")
    Popen("python3 uninstall.py")
