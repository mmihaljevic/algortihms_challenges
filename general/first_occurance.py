"""
find first occurance of k in sorted array
"""

def bin_search(array,k):
	begin = 0
	end = len(array)
	while begin + 1 < end:
		mid = begin + (end - begin) / 2
		if array[mid] == k:
			return mid
		elif array[mid] > k:
			end = mid
		else:
			begin = mid

	return -1

def first_occurance(array, k):
	# runs O(n) if array is all k-s
	occurance = bin_search(array, k)
	if occurance != -1:
		while occurance > 0:
			if array[occurance -1] == k:
				occurance -= 1
			else:
				return occurance
		return occurance

	return -1


