# Given N numbers , [N<=10^5] we need to count the total pairs of numbers that have a difference of K. [K>0 and K<1e9]

# Input Format:
# 1st line contains N & K (integers).
# 2nd line contains N numbers of the set. All the N numbers are assured to be distinct.
# Output Format:
# One integer saying the no of pairs of numbers that have a diff K.

# Sample Input #00:
# 5 2
# 1 5 3 4 2

# Sample Output #00:
# 3

 
# Sample Input #01:
# 10 1
# 363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793 
 
# Sample Output #01:
# 0

N, K = raw_input().split()
n = int(N) # number of elements
k = int(K) # difference

elements = raw_input().split()
elements = [int(i) for i in elements]
elements = sorted(elements)

pairs = 0

if elements[n-1] - elements[0] < k:
	print pairs

for i in xrange(n-1, -1, -1):
	for j in xrange(i-1,-1, -1):
		if elements[i] - elements[j] >k:
			break
		elif elements[i] - elements[j] == k:
			pairs += 1

print pairs



