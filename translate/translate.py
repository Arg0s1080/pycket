# TODO: Add to .gitignore

from os.path import join, pardir
from os import getcwd, listdir
from subprocess import run, PIPE, Popen


context = ["main_window", "mail_window"]     # Thought for ["main", "settings", "main", etc]
translations = ["es"]  # Thought for ["es", "fr_FR", "de", "pt", etc]


class Translate:
    def __init__(self):
        self._translate_path = getcwd()
        self._uis_path = join(pardir, "ui")
        ui_files = listdir(self._uis_path)
        compile_uis = [file for file in ui_files if file.endswith("window.py")]  # ui/*window.py
        self._to_translate = [ui for ui in compile_uis if ui in context]

    def files_to_translate(self):
        return self._to_translate

    def pylupdateOLD(self):  # NOTE: Obsolete: Run pylupdate5 qt_tr.pro
        """Make .ts files of each ui compiled"""
        tr_couples = []
        for tr in translations:
            for file in self._to_translate:
                ts_file = "%s_%s.ts" % (file, tr)
                tr_couples.append((file, ts_file))
        for item in tr_couples:
            in_ = join(self._uis_path, item[0])
            out = join(self._translate_path, item[1])
            proc = run(["pylupdate5", in_, "-ts", out], stdout=PIPE)
            if proc.returncode == 0:
                print("- Make %s from %s" % (item[1], item[0]))
            else:
                print(" - Error making %s from %s" % (item[1], item[0]))

    def lrelease(self):
        """Makes .qm file for each .ts file"""
        for file in listdir(self._translate_path):
            if file.endswith(".ts"):
                proc = Popen(["lrelease", join(self._translate_path, file)], stdout=PIPE, stderr=PIPE)
                return_code = proc.wait()
                if return_code == 0:
                    print(proc.stdout.read().decode())
                else:
                    print(proc.stderr.read().decode())


tr = Translate()

#tr.pylupdate()
tr.lrelease()