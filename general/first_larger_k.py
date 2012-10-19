#!/usr/local/bin/python


def first_larger(array, k):
	""" find first larger than k """
	
	# check if array is None, empty,...
	if array is None or len(array) == 0:
		return False

	if array[-1] <= k:
		return False

	begin = 0
	end = len(array)

	while begin + 1 < end:
		med = begin + (end-begin) / 2
		if array[med] == k: 
			while array[med] == k:
				med += 1
			return med
		elif array[med] > k:
			end = med
		else:
			begin = med

	return end
