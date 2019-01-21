import pandoc
from os.path import curdir, join

with open(join(curdir, "README.md")) as readme:
    doc = pandoc.Document()
    doc.markdown = readme.read()
    doc.to_file(join(curdir, "README.rst"))

# Incluir procesado posterior para centrar imágenes
