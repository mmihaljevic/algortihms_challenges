"""
- is x subsequence of y
- how long are strings, what they represent 
- test cases:
	None, None - False input
	"abcd", "ab" - x > y - False
	"" "abcd" - True (empty string is subsequence of any string
	"abcd", "abcd" - True strings are equal
    "anna", "banana" - True
	"annab", "banana" - False
"""

def subsequence(x, y):
	# check for wrong inputs
	if x is None or y is None:
		return False
	if type(x) != str or type(y) != str:
		return False
	if len(x) > len(y): # O(1)  
		return False
	idx = 0
	for i in xrange(len(x)): # O(len(xy))
		idx = y.find(x[i], idx) # find occurance of x[i] after idx
		if idx == -1:
			return False
	if i == len(x) -1:
		return True
	return False


