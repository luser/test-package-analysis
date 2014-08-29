#!/usr/bin/env python

import json
import hashlib
import os
import sys

def hash(file):
    return hashlib.sha1(open(file, 'rb').read()).hexdigest()

topdir = sys.argv[1]

all_files = []
for dirpath, dirs, files in os.walk(topdir):
    for f in files:
        fullpath = os.path.join(dirpath, f)
        relpath = os.path.relpath(fullpath, topdir)
        all_files.append((hash(fullpath), os.stat(fullpath).st_size, relpath))
json.dump({'files': all_files}, sys.stdout)

