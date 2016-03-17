#!/usr/bin/env python

import sys
import subprocess
import csv
from os import path
from openpyxl import load_workbook

def robot_run(filename):
    subprocess.call("robot {filename}".format(filename=filename), shell=True)

filename = sys.argv[1]
robotfilename = "_{name}.tsv".format(name=path.splitext(path.basename(filename))[0])

ws = load_workbook(filename=filename).active

with open(robotfilename, "w") as tsvfile:
    robotfile = csv.writer(tsvfile, delimiter="\t")
    for row in ws.rows:
        robotfile.writerow([cell.value if cell.value is not None else "" for cell in row])

robot_run(robotfilename)
