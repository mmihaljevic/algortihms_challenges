# Write a method to decide if two strings are anagrams or not.

def is_anagram(string1, string2):
	if string1 is None or string2 is None \
	or len(string1) != len(string2) or len(string1) < 1:
		return False

	array = [0 for i in xrange(256)] #ASCII

	for ch in string1:
		array[ord(ch)] += 1
	
	for ch in string2:
		array[ord(ch)] -= 1

	if array.count(0) == len(array):	
		return True 

	return False


