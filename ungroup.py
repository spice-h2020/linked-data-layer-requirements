#!/usr/bin/python3
import csv
import sys
import os


def processLine(line):
    l = []
    for s in line[1].split("/"):
        for d in line[2].split("/"):
            l.append(",".join([line[0], s, d, line[3]]))
    return l
    
fil = None
if not os.isatty(0):
    for line in sys.stdin:
        lines = processLine(line.strip().split(","))
        for l in lines:
            print(l)
        
else:
    fil = sys.argv[1]
    with open(fil) as f:
        reader = csv.reader(f)
        for line in reader:
            lines = processLine(line)
            for l in lines:
                print(l)

            # l = []
 #            for x in i:
 #                if '/'  in x:
 #                    m = x.split('/')
 #                    l.append(m)
 #                else:
 #                    l.append(x)
 #            for j in l[2]:
 #                print(l[0]+','+l[1]+','+j)
