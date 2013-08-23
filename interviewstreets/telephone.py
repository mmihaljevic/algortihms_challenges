"""
2
1 877 2638277
91-011-23413627


CountryCode=1,LocalAreaCode=877,Number=2638277
CountryCode=91,LocalAreaCode=011,Number=23413627
"""
import re

string = "CountryCode=%(c)s,LocalAreaCode=%(l)s,Number=%(n)s"

num_lines = int(raw_input())

for i in xrange(num_lines):
    line = re.split("\W+", raw_input())
    print string % {'c': line[0], 'l' : line[1], 'n' : line[2]}  
    
