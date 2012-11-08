"""
Write a method to randomly generate a set of m integers from an array of size n. Each
element must have equal probability of being chosen.
"""

import random

def random_set(array, m):
	result = []
	if array is None or m is None:
		return False
	n = len(array)
	if n < m:
		return False
	idx = 0
	for i in xrange(m):
		rdm_idx = random.randint(idx, n -1)
		result.append(array[rdm_idx]) # add result to set
		# shrink array
		array[idx], array[rdm_idx] = array[rdm_idx], array[idx]
		idx += 1
	return result


print random_set([1,2,3,4,5,6,7,8,9,10,11,12,13], 5)
