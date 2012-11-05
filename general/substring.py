"""
is x substring of y
"""

def substring(x,y):
	if x is None or y is None:
		return False
	if len(x) > len(y) or len(x) == 0 or len(y) == 0:
		return False

	idx = y.find(x[0])
	while idx != -1 :
		if idx + len(x) > len(y):
			return False
		subs = True
		for i,v in enumerate(x):
			if v != y[idx + i]:
				subs = False
				continue
		if subs:
			return True
		idx = y.find(x[0], idx +1)
	return False

# test cases
# print substring(None, None)
# print substring("", "")
# print substring("ansijsioaso", "aaaa")
# print substring("bat", "atabs")
# print substring("foo", "foifoo")
# print substring("barbaz", "foobarbazfoobarbaz")
# print substring("google", "google")
