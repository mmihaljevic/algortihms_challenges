#!/usr/local/bin/python

# a[i] + a[j] = S ?


def pair_sums(array, S):
	dictionary = {}
	for i in xrange(len(array)):
		complement = S - array[i]
		print complement, array[i], dictionary
		if dictionary.has_key(complement):
			return dictionary[complement], i
		elif complement > 0:
			dictionary[array[i]] = i # can override

	return -1


print pair_sums([1,2,3,4,5,6,6,7,8,9], 15)
