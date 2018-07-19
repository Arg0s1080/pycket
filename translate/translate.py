# TODO: Add to .gitignore

from os.path import join
from os import getcwd, listdir
from subprocess import run, PIPE, Popen


context = ["main"]     # Thought for ["main", "settings", "main", etc]
translations = ["es"]  # Thought for ["es", "fr_FR", "de", "pt", etc]


class Translate:
    def __init__(self):
        self._translate_path = getcwd()
        self._uis_path = self._translate_path.replace("translate", "ui")
        ui_files = listdir(self._uis_path)
        compile_uis = [file for file in ui_files if file.endswith("window.py")]  # ui/*window.py
        self._to_translate = [ui for ui in compile_uis if ui[:-10] in context]

    def files_to_translate(self):
        return self._to_translate

    def pylupdate(self):
        """Make .ts files of each ui compiled"""
        tr_couples = []
        for tr in translations:
            for file in self._to_translate:
                ts_file = "%s_%s.ts" % (file[:-10], tr)
                tr_couples.append((file, ts_file))
        for item in tr_couples:
            proc = run(["pylupdate5", join(self._uis_path, item[0]), "-ts", join(self._translate_path, item[1])],
                       stdout=PIPE)
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

tr.pylupdate()
#tr.lrelease()