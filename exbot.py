#!/usr/bin/env python

import sys
import csv
from openpyxl import load_workbook

ws = load_workbook(filename=sys.argv[1]).active

with open("_google-test.tsv", "w") as tsvfile:
    robotfile = csv.writer(tsvfile, delimiter="\t")
    for row in ws.rows:
        robotfile.writerow([cell.value if cell.value is not None else "" for cell in row])
