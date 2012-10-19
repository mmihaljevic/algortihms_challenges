# Given a sorted array of n integers that has been rotated an unknown number of
# times, give an O(log n) algorithm that finds an element in the array. You may assume
# that the array was originally sorted in increasing order.
# EXAMPLE:
# Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
# Output: 8 (the index of 5 in the array)

def rotated_search(array, element):
	p = 0
	z = len(array) - 1
	x = z/2

	while p < z:
		if array[x] == element:
			return x
		elif (element > array[p] and element > array[x])\
			 or (element < array[p] and element > array[x]):
			p = x
		else:
			z = x	
		x = (p + z) / 2

print rotated_search([15,16,19,20,25,1,3,4,5,7,10,14], 5)
print rotated_search([1,2,3,4,5,6,7,10,11,16,34,33],5)
