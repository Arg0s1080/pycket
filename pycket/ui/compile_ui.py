#!/usr/bin/python3
# -*- coding UTF-8 -*-
# (ɔ) Iván Rincón 2018

from datetime import datetime
from os import getcwd, listdir
from os.path import exists, join as p_join
from shutil import copyfile
from subprocess import run, PIPE


class CompileUI:
    def __init__(self, ui_file, output):
        self.ui_file = ui_file
        self.ui_output = output

    @staticmethod
    def filename(file_path):
        return file_path.split("/")[-1]

    def backup(self, file):
        if exists(self.ui_file):
            copyfile(self.ui_file, file)
            print("- Make %s backup" % self.filename(self.ui_file))

    def execute(self):
        process = run(["pyuic5", self.ui_file, "-o", self.ui_output], stdout=PIPE)
        if process.returncode == 0:
            print("- Compile %s" % self.filename(self.ui_file))

    def header_lines(self):
        with open(self.ui_output, "r") as f:
            lines = f.readlines()
            with open(self.ui_output, "w") as file:
                for i in range(len(lines)):
                    line = lines[i]
                    if 0 < i < 5:
                        line = lines[i+2]
                    elif i == 6:
                        line = "# (ɔ) Iván Rincón %d\n" % datetime.now().year
                    elif line.startswith("import resources_rc") or line.startswith("import images_rc"):
                        line = "import pycket.common.resources"
                        print("- Modify %s by %s" % ("resources_rc", "pycket.common.resources"))
                    file.write(line)
                print("- Modify %s header lines" % self.filename(self.ui_output))


bak = lambda x: "%s.old" % x
out = lambda x: x.replace(".ui", "_window.py")
join = lambda x: p_join(getcwd(), x)

sets = [(file, out(file), bak(file)) for file in listdir(getcwd()) if file.endswith("ui")]

for item in sets:
    ui, output, backup = map(join, item)
    compile_ui = CompileUI(ui, output)
    compile_ui.backup(backup)
    compile_ui.execute()
    compile_ui.header_lines()
