#!/usr/local/bin/python
'''
N ants are in a circular race. The length of the race is 1000 meters and ant number i is initially Vi meters far from starting point (point 0) of the race in clockwise order. All the ants walk with a speed of 0.1 meters per second, some of them walk in clockwise order, some in counter clockwise order. When two ants meet at a point, they say "Hi" to each other and both of them change their direction of walking to the opposite direction. This process is timeless, meaning they say "Hi" and change their direction in 0 seconds.

You are given the initial position of ants, you don't know their initial directions but you want to know how many times do they say "Hi" to each other after 1000000006 ( 10^9+6 seconds ). You need to find the initial walking direction of ants such that, c1+c2+c3+...+cn is maximized, where ci is the number of times ant number i say "Hi". Print this maximum value.

Input:

The first line of the input contains an integer N, the number of ants. N is not greater than 100.

Next line contains n numbers V1 , V2 , ... , VN. All Vi are non negative integers less than 1000. All Vi are distinct.

Output:

On the only line of the output print an integer being the answer to the test.

Sample Input
 
2
0 500
 
Sample Output
 
400000
 
Explanation
In the example there are two ants, In case their direction is the same, they will never say hi to each other, in the other case they will say "Hi" to each other in times 2500, 7500,12500, ... , 999999750. so the result for an Ant would be (999997500 - 2500)/5000+1 = 200000. Hence the answer is 200000*2 = 400000.
'''

num_ants = int(raw_input())
V = raw_input().split()
v = [int(i) for i in V]

v = sorted(v)

time = 1000000006
circle_time = 10000

if num_ants % 2 == 0:
	hit = time/circle_time *(num_ants/2 *2 * num_ants/2 *2)
else:
	hit = time/circle_time *(num_ants/2 *2 * (num_ants/2 +1) *2)

# count additional hits (where sub is 1)
additional = 0
flag = 0
for i in xrange(len(v)-1):
	if flag == 0:
		if v[i+1] - v[i] == 1:
			additional +=2
			flag = 1
		else:
			flag = 0
	else:
		flag = 0

print hit + additional


