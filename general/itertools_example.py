"""
python way to work with combinations and permutations

"""

import itertools


print "Permutations: "
permutations =  itertools.permutations("wxyz")
for permutation in permutations:
    print permutation

print "Combinations: "
for i in xrange(1,5):
    combinations =  itertools.combinations("wxyz",i)
    for combination in combinations:
        print combination
