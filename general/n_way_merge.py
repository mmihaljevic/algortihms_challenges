"""
Given N sorted arrays of integer, output one merged array

first two solutions are solved using heapq and itertools modules

algorithms for third:
1. create priority queue
2. iterate trough each array a:
    * enqueue the pair (next_number_in(a), a) using the first value as priority key
3. while queue is not empty:
    * deque head (m, a)
    * output m
    * if a not depleted:
        * enque(next_number_in(a), a)
"""
from heapq import merge
from heapq import heappush
from heapq import heappop
from itertools import chain
from collections import deque

# first solution using heapq
# heapq.merge(*iterables) - returns iterator 
def n_way_merge_1(*args):
    result = list(merge(*args))
    return result

# second solution using itertools and sorted
# sorted(itertools.chain(*iterables)) - returns list + doesn't assume arrays are sorted 
def n_way_merge_2(*args):
    result = sorted(chain(*args))
    return result

# third solution
# create a priority queue (next_number_in(a), a)
def n_way_merge_3(*args):
    pq = []
    result = []
    for array in args:
        array = deque(array)
        # take first element of array, and the rest of an array
        heappush(pq, (array.popleft(), array))
    
    while len(pq) > 0:
        key, array = heappop(pq)
        result.append(key)
        if len(array) > 0:
            heappush(pq, (array.popleft(), array))

    return result

# test cases
a1 = [1, 5, 6, 8, 9, 23, 46, 54]
a2 = [3, 7, 21, 47, 55, 66, 71, 77]
a3 = [2, 4, 11, 65, 70, 100, 102, 130]
a4 = [10, 12, 13, 24, 48, 69, 81, 82]

print "result1: ", n_way_merge_1(a1, a2, a3, a4)
print "result2: ", n_way_merge_2(a1, a2, a3, a4)
print "result3: ", n_way_merge_3(a1, a2, a3, a4)
