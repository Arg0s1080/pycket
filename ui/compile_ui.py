#!/usr/bin/python3
# -*- coding UTF-8 -*-

from os import getcwd, listdir, path
from shutil import copyfile
from subprocess import run, PIPE


class CompileUI:
    def __init__(self, ui_file, output):
        self.ui_file = ui_file
        self.ui_output = output

    def backup(self, file):
        if path.exists(self.ui_file):
            copyfile(self.ui_file, file)
            print("- Make %s backup" % self.ui_file.split("/")[-1])

    def execute(self):
        arg_ui = list()
        arg_ui.insert(0, "pyuic5")
        arg_ui.insert(1, self.ui_file)
        arg_ui.append("-o")
        arg_ui.append(self.ui_output)

        process = run(arg_ui, stdout=PIPE)
        print("- Compile %s" % self.ui_file.split("/")[-1])
        return process

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
                print("- Modify %s header lines" % self.ui_output.split("/")[-1])


bak = lambda x: x + ".old"
out = lambda x: x.replace(".ui", "_window.py")
join = lambda x: path.join(getcwd(), x)

ops = [(file, out(file), bak(file)) for file in listdir(getcwd()) if file.endswith("ui")]

for item in ops:
    item = list(map(join, item))
    compile_ui = CompileUI(item[0], item[1])
    compile_ui.backup(item[2])
    compile_ui.execute()
    compile_ui.header_lines()
