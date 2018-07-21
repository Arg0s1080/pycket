#!/usr/bin/python3
# -*- coding UTF-8 -*-

from os import getcwd, listdir, path
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
        if path.exists(self.ui_file):
            copyfile(self.ui_file, file)
            print("- Make %s backup" % self.filename(self.ui_file))

    def execute(self):
        process = run(["pyuic5", self.ui_file, "-o", self.ui_output], stdout=PIPE)
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
                        pass
                        line = "# (ɔ) Iván Rincón 2018\n"
                    file.write(line)
                print("- Modify %s header lines" % self.filename(self.ui_output))


bak = lambda x: "%s.old" % x
out = lambda x: x.replace(".ui", "_window.py")
join = lambda x: path.join(getcwd(), x)

sets = [(file, out(file), bak(file)) for file in listdir(getcwd()) if file.endswith("ui")]

for item in sets:
    ui, output, backup = map(join, item)
    compile_ui = CompileUI(ui, output)
    compile_ui.backup(backup)
    compile_ui.execute()
    compile_ui.header_lines()
