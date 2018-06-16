#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput
import re

# Preparing the file
with open(sys.argv[1], encoding="utf-8") as f_input:
    f_str = f_input.read()
f_output = open(sys.argv[2], "w", encoding="ansi")

# Replace the target string
f_str = f_str.replace("\n", " | ")[:-3]

f_output.write("$word = " + f_str + ";\n(<$word>)")

# Closing the file
f_output.close()
