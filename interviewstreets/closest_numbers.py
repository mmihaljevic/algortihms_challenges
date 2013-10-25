"""
Given a list of unsorted numbers, can you find the numbers that have 
the smallest absolute difference between them? If there are multiple 
pairs, find them all.
"""

n = input()
list = raw_input().strip().split()
list = [int(e) for e in list]
list.sort()

result = {}
min_diff = 2*pow(10,7)

for i in xrange(len(list) -1):
    diff = abs(list[i] - list[i+1]) 
    if diff < min_diff:
        min_diff = diff
    if result.has_key(diff):
        result[diff].append(str(list[i]))
        result[diff].append(str(list[i+1]))
    else:
        result[diff] = [str(list[i]), str(list[i+1])]


print " ".join(result[min_diff])
