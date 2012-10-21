#!/usr/local/bin/python
"""

Give an array of 1001 elements, which includes the numbers 1 to 1000 inclusive in random order, 
plus one duplicate number, write the most efficientalgorithm to detect the duplicate number. 
Make sure you only access each item in the array a maximum of once. 

"""
import random

def detect_duplicate(array):
	if array is None or len(array) != 1001:
		return False

	sum_array = sum(array)
	missing = sum_array - 500500
	return missing


# test case
x = [i for i in xrange(1,1001)]
random.shuffle(x)
x.insert(random.choice(x)-1, random.choice(x))

print detect_duplicate(x)
