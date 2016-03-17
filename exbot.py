#!/usr/bin/env python

import sys
import subprocess
import csv
import os
from openpyxl import load_workbook

def create_robot_file(filename):
    """
    Generate tsv file and return robotfilename
    """
    robotfilename = "_{name}.tsv".format(name=os.path.splitext(os.path.basename(filename))[0])
    ws = load_workbook(filename=filename).active

    with open(robotfilename, "w") as tsvfile:
        robotfile = csv.writer(tsvfile, delimiter="\t")
        for row in ws.rows:
            robotfile.writerow([cell.value if cell.value is not None else "" for cell in row])

    return robotfilename


def robot_run(filename):
    subprocess.call("robot {filename}".format(filename=filename), shell=True)


if __name__ == "__main__":
    robotfilename = create_robot_file(sys.argv[1])
    robot_run(robotfilename)
    os.remove(robotfilename)
