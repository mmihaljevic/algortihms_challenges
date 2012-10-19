# insertion sort implementation

def insertion_sort(A):
	for j in xrange(1, len(A)):
		elem = A[j]
		i = j-1
		while i>=0 and A[i] > elem:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = elem
	return A

def non_decreasing_insertion(A):
	for j in xrange(1, len(A)):
		elem = A[j]
		i = j-1
		while i>=0 and A[i] < elem:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = elem
	return A

print insertion_sort([5,2,4,6,1,3])
print non_decreasing_insertion([5,2,4,6,1,3])
