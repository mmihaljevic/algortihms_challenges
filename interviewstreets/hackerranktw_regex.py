"""
Increasing popularity of hackerrank can be seen in tweets like

I love #hackerrank
I just scored 27 points in the Picking Cards challenge on #HackerRank
I just signed up for summer cup @hackerrank
Given a set of most popular tweets, your task is to find out how many of 
those tweets has the string hackerrank in it.
"""

import re

num_lines = int(raw_input())
counter = 0

for i in xrange(num_lines):
    line = raw_input()
    counter += line.lower().count("hackerrank")

print counter
