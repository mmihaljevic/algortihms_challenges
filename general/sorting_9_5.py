#!/usr/local/bin/python

def find_key(key, array):
	if array is None or key is None or len(array) < 1:
		return -1
	first = 0
	last = len(array) -1
	while first <= last:
		while array[first] == "":
			first +=1
		while array[last] == "":
			last -=1
		if first > last or key > array[last]:
			return -1
		if array[first] == key:
			return first
		if array[last] == key:
			return last
		median = (first + last) / 2
		while array[median] == "" and median < last:
			median += 1
		if median == last:
			return -1
		if array[median] == key:
			return median
		elif array[median] > key:
			last = median
		else:
			first = median

find_key("ball",["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""])
