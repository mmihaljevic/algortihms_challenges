#!/usr/local/bin/python
"""
first: finds missing number in permutated integer array
second: finds missing 2 mubers in permutated integer array

"""

from math import sqrt

def find_missing_one(array):

	if array is None or len(array) < 1:
		return False

	n = len(array) + 1
	sum_array = sum(array)
	sum_range = n * (n + 1)/2 

	return sum_range - sum_array



def find_missing_two(array):
	"""
		a + b = n(n+1)/2 - sum(array) = x
		a^2 + b^2 = n(n+1)(2n+1)/6 - sum(squares) = y

		a = x -b

	"""
	if array is None or len(array) < 1:
		return False

	n = len(array) + 2 # 2 missing elements

	sum_array = sum(array)
	sum_range = n * (n + 1)/2
	x = sum_range - sum_array

	sum_squares = sum([pow(i, 2) for i in array])
	sum_range_squares = n * (n + 1) * (2 * n + 1) / 6
	y = sum_range_squares - sum_squares

	# quadratic equation solution 
	b = int((2 * x - sqrt(4 * pow(x, 2) - 8 * (pow(x, 2) - y))) / 4)
	a = x - b
	
	return a, b

print find_missing_two([1, 5, 8, 7, 3, 6, 9])
print find_missing_two([2, 3, 1, 6, 8, 9, 10, 4])
print find_missing_two([10, 7, 1, 3, 9, 2, 4, 6])
