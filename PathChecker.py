#!/usr/bin/env python3
import os
import sys

path = "/media/Colossus/Series/"
if len(sys.argv) > 1:
        path = sys.argv[1]

isFile = os.path.exists(path)
#print(path)
#print(isFile)
#print(len(sys.argv))

if isFile:
        sys.exit(0)
else:
        sys.exit(1)
