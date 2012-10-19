# You are given two sorted arrays, A and B, and A has a large enough buffer at the end
# to hold B. Write a method to merge B into A in sorted order.

def merge(A,B):
	m = len(A)
	A.extend(B) # put B in the buffer
	for j in xrange(len(B)):
		elem = B[j]
		i = m + j - 1
		while i >= 0 and A[i] > elem:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = elem


	return A

print merge([1,4,5,8], [2,3,6,7])
