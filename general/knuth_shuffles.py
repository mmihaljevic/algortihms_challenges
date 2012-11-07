"""
Write a method to shuffle a deck of cards. It must be a perfect shuffle - in other words,
each 52! permutations of the deck has to be equally likely. Assume that you are given
a random number generator which is perfect.
"""

import random

def knuth_shuffles(A):
	if A is None or len(A) != 52:
		return False
	for i in xrange(len(A)):
		d = random.randint(0,len(A)-1)
		A[i], A[d] = A[d], A[i] 
	return A

A = [i for i in xrange(52)]
print knuth_shuffles(A)

