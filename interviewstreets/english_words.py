"""
2
hackerrank has such a good ui that it takes no time to familiarise its environment
to familiarize oneself with ui of hackerrank is easy
1
familiarize
"""

num_lines = int(raw_input())

lines = []   
for i in xrange(num_lines):
    lines.append(raw_input())

num_words = int(raw_input())
for i in xrange(num_words):
    counter = 0
    word_us = raw_input()
    word_uk = word_us[:-2] + "se"
    for line in lines:
        counter += line.count(word_us)
        counter += line.count(word_uk)
    print counter




    
