"""
The string must begin with between 0 and 3 (inclusive) lowercase letters.
Immediately following the letters, there must be a sequence of digits. 
The length of this segment must be between 2 and 8, both inclusive.
Immediately following the numbers, there must be atleast 3 uppercase letters.
"""

import re

re_ut = re.compile("^[a-z]{0,3}[0-9]{2,8}[A-Z]{3}[A-Z]*$")

num_lines = int(raw_input())

for i in xrange(num_lines):
    if re_ut.match(raw_input()):
        print "VALID"
    else:
        print "INVALID"
