#!/usr/bin/env python

import json
import sys
from collections import defaultdict

total_files = 0
total_size = 0
hash_files = defaultdict(list)
hash_sizes = {}
for input in sys.argv[1:]:
    files = json.load(open(input, 'rb'))['files']
    total_files += len(files)
    for hash, size, file in files:
        hash_files[hash].append(files)
        hash_sizes[hash] = size
        total_size += size
dupe_size = sum(hash_sizes[k] * len(v)-1 for k,v in hash_files.iteritems() if len(v) > 1)
print "Total input files %d" % total_files
print "Total unique hashes %d" % len(hash_files.keys())
print "Total original size %d" % total_size
print "Size saved by removing duplicates %d" % dupe_size
print "%% of original after de-duplication: %d%%" % int(100.0 * float(total_size - dupe_size) / float(total_size))
