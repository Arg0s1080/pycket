from os import listdir, removedirs, remove, getuid
from os.path import exists, join, dirname, expanduser


def uninstall():
    red = "\33[91m%s\33[0m"
    green = "\33[32m%s\33[0m"
    gr_bd = "\33[32;1m%s\33[0m"

    getuid() and exit(red % "To uninstall Pycket must have root privileges.")

    installed_files = join(expanduser("~"), ".local", "share", "pycket", "installed_files")

    try:
        with open(installed_files, "r") as f:
            dirs = []
            for line in f.readlines():
                file = line.replace("\n", "")
                try:
                    remove(file)
                    print(green % "Deleting %s" % file)
                    _dir = dirname(file)
                    if _dir not in dirs:
                        dirs.append(_dir)
                except FileNotFoundError as error:
                    print(red % "Error: %s not found" % error.filename)

            for _dir in dirs:
                if exists(_dir):
                    if len(listdir(_dir)) == 0:
                        removedirs(_dir)
                        if not exists(_dir):
                            print(green % "Removing dir %s" % _dir)
            remove(installed_files)
            print(gr_bd % "Pycket has been successfully uninstalled")
    except FileNotFoundError as error:
        exit(red % "Uninstalled aborted. Could not find %s" % error.filename)


if __name__ == '__main__':
    uninstall()
