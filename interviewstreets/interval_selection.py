#!/bin/python
"""
You are given a list of N intervals.
The challenge is to select the largest subset of intervals such that no three intervals in the subset share a common point?

Input:
The first line contains the number of cases T. T cases follow. Each case contains the number N on the first line followed by N lines containing integers ai and bi. The ith line denotes the starting and ending points of the ith interval.

Output:
Output T lines, one for each test case, containing the desired answer for the corresponding test case.

Constraints:
1 <= T <= 100
2 <= N <= 1000
1 <= ai <= bi <= 1000000000 (10^9)

"""

test = int(raw_input())

for t in xrange(0, test):

	N = int(raw_input())
	A = []
	B = []
	segments = []

	for i in range(0, N):
		numbers = raw_input()
		a, b = [int(x) for x in numbers.split(' ')]
                segments.append((a,b))   
		A.append(a)
		B.append(b)
        B = sorted(B)
        # check if more than 2 segments are covering it
        for i in B:
            num_covering = 0
            delete_segment = -1,-1
            for a,b in segments:
                if a<= i and i<=b:
                    num_covering += 1
                    if delete_segment[1] < b:
                        delete_segment = a, b
            if num_covering > 2:
                segments.remove(delete_segment)
                    
	result = len(segments)
	print result
