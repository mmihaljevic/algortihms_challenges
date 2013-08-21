#!/usr/local/bin/python
"""
At HackerRank, we always want to find out how popular we are getting every day and have scraped conversations from popular sites. Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:

Starts with hackerrank
Ends with hackerrank
Start and ends with hackerrank

Input Format

First line of the input contains N, N lines follow. From the second line onwards, each line contains a set of words W separated by a single space

Constraints

1 <= N <= 10
1 <= W <= 100
All the characters in W are lowercase alphabet characters. If C is the count of the characters in W, then 1 <= C <= 20

Output Format

For every line,

Print 1 if the conversation starts with hackerrank
Print 2 if the conversation ends with hackerrank
Print 0 if the conversation starts and ends with hackerrank
Print -1 if none of the above.

i love hackerrank 2
hackerrank is an awesome place for programmers 1
hackerrank 0
i think hackerrank is a great place to hangout -1

"""

import re

# complile regex
start = re.compile("^hackerrank")
end = re.compile("(.)?hackerrank$|(.)+hackerrank$")

num_line = int(raw_input())

# take each line 
for i in xrange(num_line):
    line = raw_input()
    res = -1
    if start.match(line):
        res = 1
    if end.match(line):
        if res == 1:
            res = 0
        else:
            res = 2
    print res


