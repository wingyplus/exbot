#!/usr/bin/env python

import sys
import csv
from os import path
from openpyxl import load_workbook

filename = sys.argv[1]
ws = load_workbook(filename=filename).active

with open("_{name}.tsv".format(name=path.splitext(path.basename(filename))[0]), "w") as tsvfile:
    robotfile = csv.writer(tsvfile, delimiter="\t")
    for row in ws.rows:
        robotfile.writerow([cell.value if cell.value is not None else "" for cell in row])
