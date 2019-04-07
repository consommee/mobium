import sys
import re
import math
import rhinoscriptsyntax as rs
import csv


def main():
    lns = []
    #prompt the user for a file to import
    filter = "csv file (*.csv)|*.csv|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open csv File", filter)
    if not filename: return

    with open(filename, "r") as f:
        reader = csv.reader(f)
        
        for i in range(10):
            tmp = []
            j = 0
            for row in reader:
                j += 1
                print(j)
                if float(row[3]) == i:
                    tmp.append((float(row[1])+j * 1,float(row[2]), 0))
            ln = rs.AddPolyline(tmp)
            lns.append(ln)
    return lns

if __name__ == '__main__':
    main()
