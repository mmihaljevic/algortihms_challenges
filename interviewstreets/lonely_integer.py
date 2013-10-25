""" 
solution to lonely integer problem
"""

num_elements = input()
elements = raw_input().split()
d = {}
for i in elements:
    if d.has_key(i):
        del(d[i])
    else:
        d[i] = 1
 
print d.keys()[0]
