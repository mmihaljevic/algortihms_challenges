"""
<char><char><char><char><char><digit><digit><digit><digit><char>
"""
import re

regex = re.compile("^[A-Z]{5}\d{4}[A-Z]{1}$")
num_line = int(raw_input())

for i in xrange(num_line):
    line = raw_input()
    if regex.match(line):
        print "YES"
    else:
        print "NO"
