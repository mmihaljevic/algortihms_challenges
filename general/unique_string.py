# Implement an algorithm to determine if a string has all unique characters.

def unique_str(string):
	d = {} # with additional data structue
	if string is None or len(string) < 1:
		return False

	for char in string:
		if d.has_key(char):
			return False
		d[char] = 1

	return True

# test cases
print unique_str(None)
print unique_str("")
print unique_str(1234567)
print unique_str("a")
print unique_str("abc")
print unique_str("abcand")


	
