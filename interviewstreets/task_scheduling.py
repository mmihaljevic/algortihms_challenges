"""
You have a long list of tasks that you need to do today. Task i is 
specified by the deadline by which you have to complete it (Di) and 
the number of minutes it will take you to complete the task (Mi). 
You need not complete a task at a stretch. You can complete a part of 
it, switch to another task and then switch back.

You've realized that it might not actually be possible complete all the 
tasks by their deadline, so you have decided to complete them so that the maximum amount
by which a task's completion time overshoots its deadline is minimized.

Input:
The first line contains the number of tasks T. Each of the next T lines contains 
two integers Di and Mi.

Output:
Output T lines. The ith line should contain the minimum maximum overshoot you 
can obtain by optimally scheduling the first i tasks on your list. See the sample
input for clarification.
"""

from heapq import heapify
from heapq import heappush
from heapq import heappop


N = int(raw_input().strip())
heap = []

def min(heap):
    time = 0
    max = 0
    while len(heap) > 0:
        t = heappop(heap)
        node = t
        time += node[1]
        if time > node[0]:
            if max < time - node[0]:
                max = time - node[0]

    return max

# read each element and count everything onsite as you read data
for i in xrange(N):
    d, m = raw_input().split()
    d = int(d)
    m = int(m)
    heappush(heap, (d, m))
    print min(heap[:])
