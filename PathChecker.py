#!/usr/bin/env python3
import os
import sys

path = "/media/Colossus/Series/"

isFile = os.path.exists(path)
if isFile:
        sys.exit(0)
else:
        sys.exit(1)
