#!/usr/bin/env python3
import os
import sys

#path = "/media/Colossus/Series/"
path = sys.argv[1]

isFile = os.path.exists(path)
#print(path)
#print(isFile)
if isFile:
        sys.exit(0)
else:
        sys.exit(1)
