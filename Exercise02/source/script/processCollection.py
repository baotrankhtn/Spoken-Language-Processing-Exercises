#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput
import string
import re

# Preparing the file
f_input = open(sys.argv[1], "r", encoding="utf-8")
f_output = open(sys.argv[2], "w", encoding="utf-8")
fs_input = ""

# Replace the target string
for line in f_input:
    lines = line.strip().replace(".", "\n")
    for sm_line in lines.split("\n"):
        fs_input += sm_line.strip() + "\n"

fs_input = re.sub(r"\n{2,}", "", fs_input)

f_output.write(fs_input)

# Closing the file
f_input.close()
f_output.close()
