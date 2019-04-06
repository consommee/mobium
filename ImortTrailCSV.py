import sys
import re
import math
import rhinoscriptsyntax as rs
import csv


def main():
    pts = []
    #prompt the user for a file to import
    filter = "csv file (*.csv)|*.csv|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    with open(filename, "r") as f:
        reader = csv.reader(f)
        # for i in range(100):
        for row in reader:
            if row[3] == 0:
                pt = (row[1], row[2], 0)
                pts.append(pt)
            rs.AddPolyline(pts)




if __name__ == '__main__':
    main()
