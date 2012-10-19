from collections import deque

N,M = raw_input().split()

n = int(N)
m = int(M)

cut = 0
A = [[0, 0] for i in xrange(m)]
count = [1 for i in xrange(n + 2)]
count[0] = 0

for i in xrange(m):
	x, y = raw_input().split()
	A[i][0] = int(x)
	A[i][1] = int(y)

for i in xrange(m):
	count[A[i][1]] = 0

q = deque()
for i in xrange(n + 1, 0, -1):
	if count[i] == 0:
		q.append(i)
		total = 0
		while len(q) > 0:
			elem = q.popleft()
			f = 0
			if count[elem] != 0:
				total += count[elem]
				f = 1
			else:
				total += 1

			if f == 0:
				for j in xrange(m):
					if A[j][1] == elem:
						q.append(A[j][0])
		count[i]= total;

for i in xrange(2, n):
	if count[i] % 2 == 0:
		cut += 1
print cut
