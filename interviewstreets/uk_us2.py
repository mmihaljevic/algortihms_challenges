"""
One other difference is how UK has kept the usage of letters our 
in some of its words and US has done away with the letter u and uses 
just or. Given the UK format of the word that has our in it, find out 
the total number of occurrences of both its UK and US variants 
in a given sequence of words.

2
the odour coming out of the left over food was intolerable
ammonia has a very pungent odor
1
odour
"""

num_lines = int(raw_input())

lines = []
for i in xrange(num_lines):
    lines.extend(raw_input().split())

num_words = int(raw_input())

for i in xrange(num_words):
    count = 0
    word_uk = raw_input()
    word_us = word_uk.replace('our','or')
    count += lines.count(word_uk)
    count += lines.count(word_us)
    print count 




