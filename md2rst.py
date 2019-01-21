# -*- coding: utf8 -*-
# (ɔ) Iván Rincón 2019

from os.path import curdir, join

README_MD  = join(curdir, "README.md")
README_RST = join(curdir, "README.rst")

try:
    import pypandoc  # pip install pyandoc
    output = pypandoc.convert_file(README_MD, "rst", outputfile=join(curdir, README_RST))
except ImportError:
    import pandoc
    with open(README_MD) as readme:
        doc = pandoc.Document()
        doc.markdown = readme.read()
        doc.to_file(README_RST)

