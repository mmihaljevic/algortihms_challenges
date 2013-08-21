"""
You are given N lines and your task is to find out which of the N lines starts with

hi<BLANK>
where hi is case-insensitive and is not immediately followed by the letter 
D which is also case-insensitive
"""
import re

regex = re.compile(re.compile("^(H|h){1}(i|I){1}\s[^dD]"))
num_line = int(raw_input())
for i in xrange(num_line):
    line = raw_input()
    if regex.match(line):
        print line

        
