#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput
import re

consonants = "ngh|ch|gh|gi|kh|nh|ng|ph|th|tr|qu|b|c|d|đ|g|h|k|l|m|n|p|q|r|s|t|v|x"
# Preparing the file
line = "BIỂU"

# Replace the target string
line = re.sub(r"^("+ consonants +")", r"\1 ", line, flags=re.IGNORECASE)

print(line)

