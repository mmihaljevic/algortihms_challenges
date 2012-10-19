"""
Find the no of positive integral solutions for the equations (1/x) + (1/y) = 1/N! (read 1 by n factorial) 
Print a single integer which is the no of positive integral solutions modulo 1000007.

Input:
N 
Output:
Number of positive integral solutions for (x,y) modulo 1000007
Constraints:
1 <= N <= 10^6 
Sample Input00:
1
Sample Output00:
1

 
Sample Input01:
32327
Sample Output 01:
656502
 
Sample Input02:
40921
Sample Output 02:
686720


SOLUTION: (2e1 +1)(2e2 +1)....(2ek +1)
"""

# prime generation:
def generate_prime(n):
	primes = [1 for i in xrange(n+1)]
	for i in xrange(2, n):
		if i * i > n:
			break
		else:
			if primes[i] == 1:
				for j in xrange(i, n):
					if j*i > n:
						break
					else:
						primes[i*j] = 0

	return primes

#get multiplicities
def get_multiplicities(primes, n):
	multiplicities = [1 for i in xrange(len(primes)) ]
	for i in xrange(2, len(primes)):
		if primes[i] == 1:
			tmp = n
			e = 0
			while(tmp != 0):
				e = e + (tmp/i)
				tmp = tmp /i
			multiplicities[i] = 2 * e + 1
	
	return multiplicities 

# multiply - get the final result
def multiply(multiplicities):
	return reduce(lambda x, y: x * y, multiplicities)


n = int(raw_input())
primes =  generate_prime(n)
multi =  get_multiplicities(primes, n)
res =  multiply(multi)
print res % 1000007
