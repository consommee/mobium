import sys
import re
import math
import rhinoscriptsyntax as rs
import csv


def main():
    lns = []
    #prompt the user for a file to import
    filter = "csv file (*.csv)|*.csv|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    with open(filename, "r") as f:
        reader = csv.reader(f)
        for i in range(10):
            tmp = []
            for row in reader:
                if float(row[3]) == i:
                    tmp.append((float(row[1]),float(row[2]), 0))
            t_tmp = tuple(tmp)
            rs.AddPolyline(t_tmp)
            del tmp[:]


if __name__ == '__main__':
    main()
