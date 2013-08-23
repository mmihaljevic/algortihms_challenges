"""
It has to begin with either an underscore '_' (ascii value 95) or a 
dot '.' (ascii value 46)
It has to be immediately followed by one or more occurrences of digits numbered 0-9
It can then have letters, either uppercase or lowercase, 0 or more in number
It can then end with an optional '_' (ascii value 95)
"""

import re

re_username = re.compile("^(_|\.)[0-9]+[a-zA-Z]*(_)?$")
num_lines = int(raw_input())

for i in xrange(num_lines):
    if re_username.match(raw_input()):
        print "VALID"
    else:
        print "INVALID"
