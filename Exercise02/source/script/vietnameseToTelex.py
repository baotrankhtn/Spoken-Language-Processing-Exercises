#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput
import re

replaceDict = {
    ord('À'): 'AF',
    ord('Á'): 'AS',
    ord('Â'): 'AA',
    ord('Ã'): 'AX',
    ord('È'): 'EF',
    ord('É'): 'ES',
    ord('Ê'): 'EE',
    ord('Ì'): 'IF',
    ord('Í'): 'IS',
    ord('Ò'): 'OF',
    ord('Ó'): 'OS',
    ord('Ô'): 'OO',
    ord('Õ'): 'OX',
    ord('Ù'): 'UF',
    ord('Ú'): 'US',
    ord('Ý'): 'YS',
    ord('Ỳ'): 'YF',
    ord('Ỹ'): 'YX',
    ord('Ỷ'): 'YR',
    ord('Ỵ'): 'YJ',
    ord('Ự'): 'UWJ',
    ord('Ử'): 'UWR',
    ord('Ữ'): 'UWX',
    ord('Ừ'): 'UWF',
    ord('Ứ'): 'UWS',
    ord('Ư'): 'UW',
    ord('Ụ'): 'UJ',
    ord('Ủ'): 'UR',
    ord('Ũ'): 'UX',
    ord('Ợ'): 'OWJ',
    ord('Ở'): 'OWR',
    ord('Ỡ'): 'OWX',
    ord('Ờ'): 'OWF',
    ord('Ớ'): 'OWS',
    ord('Ơ'): 'OW',
    ord('Ộ'): 'OOJ',
    ord('Ổ'): 'OOR',
    ord('Ỗ'): 'OOX',
    ord('Ồ'): 'OOF',
    ord('Ố'): 'OOS',
    ord('Ọ'): 'OJ',
    ord('Ỏ'): 'OR',
    ord('Ị'): 'IJ',
    ord('Ỉ'): 'IR',
    ord('Ĩ'): 'IX',
    ord('Ệ'): 'EEJ',
    ord('Ể'): 'EER',
    ord('Ễ'): 'EEX',
    ord('Ề'): 'EEF',
    ord('Ế'): 'EES',
    ord('Ẹ'): 'EJ',
    ord('Ẻ'): 'ER',
    ord('Ẽ'): 'EX',
    ord('Ặ'): 'AWJ',
    ord('Ẳ'): 'AWR',
    ord('Ẵ'): 'AWX',
    ord('Ằ'): 'AWF',
    ord('Ắ'): 'AWS',
    ord('Ă'): 'AW',
    ord('Ậ'): 'AAJ',
    ord('Ẩ'): 'AAR',
    ord('Ẫ'): 'AAX',
    ord('Ầ'): 'AAF',
    ord('Ấ'): 'AAS',
    ord('Ạ'): 'AJ',
    ord('Ả'): 'AR',
    ord('Đ'): 'DD',
    ord('A'): 'A',
    ord('B'): 'B',
    ord('C'): 'C',
    ord('D'): 'D',
    ord('E'): 'E',
    ord('G'): 'G',
    ord('H'): 'H',
    ord('I'): 'I',
    ord('K'): 'K',
    ord('L'): 'L',
    ord('M'): 'M',
    ord('N'): 'N',
    ord('O'): 'O',
    ord('P'): 'P',
    ord('Q'): 'Q',
    ord('R'): 'R',
    ord('S'): 'S',
    ord('T'): 'T',
    ord('U'): 'U',
    ord('V'): 'V',
    ord('X'): 'X',
    ord('Y'): 'Y'
}

# Preparing the file
with open(sys.argv[1], encoding="utf-8") as f_input:
    f_str = f_input.read()
f_output = open(sys.argv[2], "w", encoding="ansi")

# Replace the target string
f_str = f_str.translate(replaceDict)
f_str = re.sub(r"([^\s]*)(\s?)(.*?)(\n)", lambda match: match.group(1) + match.group(2) + match.group(3).lower() + match.group(4), f_str)

f_output.write(f_str)

# Closing the file
f_output.close()
