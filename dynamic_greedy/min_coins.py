"""
Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. 
Find the minimum number of coins the sum of which is S (we can use as many coins of one type 
as we want), or report that it's not possible to select coins in such a 
way that they sum up to S. 

"""

def min_coins(sum, v):
	if sum is None or sum <= 0:
		return False
	if v is None or len(v) < 1:
		return False

	min = [False for i in xrange(sum + 1)] # if we can get S from the coins - simply returns False
	min[0] = 0

	for i in xrange(1,sum + 1):
		for j in xrange(len(v)):
			# cruical part:
			if v[j] <= i and (min[i] is False or min[i-v[j]] + 1 < min[i]):
				min[i] = min[i-v[j]] + 1

	return min[sum]


sum = 11
v = [1,3,5]
print min_coins(sum, v) 
