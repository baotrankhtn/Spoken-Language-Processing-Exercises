#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput
import re
from fnmatch import fnmatch

# Usage: script path_to_wav path_to_mfc output_list1 output_list2")

root      = sys.argv[1]
mfc_path  = sys.argv[2]
f_output1 = open(sys.argv[3], "w")
f_output2 = open(sys.argv[4], "w")
pattern   = "*.wav"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            f_output1.write(os.path.join(path, name).replace("\\", "/") + " " +
                           os.path.join(mfc_path, name).replace(".wav", ".mfc").replace("\\", "/") + "\n")
            f_output2.write(os.path.join(mfc_path, name).replace(".wav", ".mfc").replace("\\", "/") + "\n")
