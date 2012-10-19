#!/usr/local/bin/python

'''
find floor sqrt of 32 bit integer
'''

def sqrt_search(key):
	
	if key is None or not isinstance(key, int) or key < 0:
		raise(AttributeError,'input must be unsigned int')	
	begin = 0
	end = 65536
	
	while(begin + 1 < end):
		mid = begin + (end - begin) / 2
		mid_sqrt = mid * mid
		if mid_sqrt == key:
			return mid
		elif mid_sqrt > key:
			end = mid
		else:
			begin = mid

	return begin
			 
	

key = int(raw_input())
print sqrt_search(key)

