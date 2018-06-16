#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput

replaceDict = {
    ord('À'): 'AF\n',
    ord('Á'): 'AS\n',
    ord('Â'): 'AA\n',
    ord('Ã'): 'AX\n',
    ord('È'): 'EF\n',
    ord('É'): 'ES\n',
    ord('Ê'): 'EE\n',
    ord('Ì'): 'IF\n',
    ord('Í'): 'IS\n',
    ord('Ò'): 'OF\n',
    ord('Ó'): 'OS\n',
    ord('Ô'): 'OO\n',
    ord('Õ'): 'OX\n',
    ord('Ù'): 'UF\n',
    ord('Ú'): 'US\n',
    ord('Ý'): 'YS\n',
    ord('Ỳ'): 'YF\n',
    ord('Ỹ'): 'YX\n',
    ord('Ỷ'): 'YR\n',
    ord('Ỵ'): 'YJ\n',
    ord('Ự'): 'UWJ\n',
    ord('Ử'): 'UWR\n',
    ord('Ữ'): 'UWX\n',
    ord('Ừ'): 'UWF\n',
    ord('Ứ'): 'UWS\n',
    ord('Ư'): 'UW\n',
    ord('Ụ'): 'UJ\n',
    ord('Ủ'): 'UR\n',
    ord('Ũ'): 'UX\n',
    ord('Ợ'): 'OWJ\n',
    ord('Ở'): 'OWR\n',
    ord('Ỡ'): 'OWX\n',
    ord('Ờ'): 'OWF\n',
    ord('Ớ'): 'OWS\n',
    ord('Ơ'): 'OW\n',
    ord('Ộ'): 'OOJ\n',
    ord('Ổ'): 'OOR\n',
    ord('Ỗ'): 'OOX\n',
    ord('Ồ'): 'OOF\n',
    ord('Ố'): 'OOS\n',
    ord('Ọ'): 'OJ\n',
    ord('Ỏ'): 'OR\n',
    ord('Ị'): 'IJ\n',
    ord('Ỉ'): 'IR\n',
    ord('Ĩ'): 'IX\n',
    ord('Ệ'): 'EEJ\n',
    ord('Ể'): 'EER\n',
    ord('Ễ'): 'EEX\n',
    ord('Ề'): 'EEF\n',
    ord('Ế'): 'EES\n',
    ord('Ẹ'): 'EJ\n',
    ord('Ẻ'): 'ER\n',
    ord('Ẽ'): 'EX\n',
    ord('Ặ'): 'AWJ\n',
    ord('Ẳ'): 'AWR\n',
    ord('Ẵ'): 'AWX\n',
    ord('Ằ'): 'AWF\n',
    ord('Ắ'): 'AWS\n',
    ord('Ă'): 'AW\n',
    ord('Ậ'): 'AAJ\n',
    ord('Ẩ'): 'AAR\n',
    ord('Ẫ'): 'AAX\n',
    ord('Ầ'): 'AAF\n',
    ord('Ấ'): 'AAS\n',
    ord('Ạ'): 'AJ\n',
    ord('Ả'): 'AR\n',
    ord('Đ'): 'DD\n',
    ord('A'): 'A\n',
    ord('B'): 'B\n',
    ord('C'): 'C\n',
    ord('D'): 'D\n',
    ord('E'): 'E\n',
    ord('G'): 'G\n',
    ord('H'): 'H\n',
    ord('I'): 'I\n',
    ord('K'): 'K\n',
    ord('L'): 'L\n',
    ord('M'): 'M\n',
    ord('N'): 'N\n',
    ord('O'): 'O\n',
    ord('P'): 'P\n',
    ord('Q'): 'Q\n',
    ord('R'): 'R\n',
    ord('S'): 'S\n',
    ord('T'): 'T\n',
    ord('U'): 'U\n',
    ord('V'): 'V\n',
    ord('X'): 'X\n',
    ord('Y'): 'Y\n'
}

# Preparing the file
f_input = open(sys.argv[1], "r", encoding="utf-8")
f_output = open(sys.argv[2], "w", encoding="ansi")

# Replace the target string
for line in f_input:
    line = line.translate(replaceDict)
    line = line.replace("\n\n", "\n")
    f_output.write(line)

# Closing the file
f_input.close()
f_output.close()

# Sort
os.system("sort -o" + sys.argv[2] + " -u " + sys.argv[2])