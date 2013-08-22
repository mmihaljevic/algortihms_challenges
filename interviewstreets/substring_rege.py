"""
1
existing pessimist optimist this is
1
is

output: 3
"""
import re


num_lines = int(raw_input())
lines = []
for i in xrange(num_lines):
    lines.append(raw_input())

num_words = int(raw_input())
for i in xrange(num_words):
    word = raw_input()
    count = 0
    regex = re.compile(".*\w+"+word+"\w+")
    for line in lines:
        line = line.split()
        for w in line:
            if regex.match(w):
                print w
                count += 1
    print count 
