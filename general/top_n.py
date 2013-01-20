"""
find top n elements in array
"""

import random
from heapq import heappush
from heapq import heappop


def top_n(array, n):
    if array is None or len(array) < 1:
        return False
    if n is None or n < 1:
        return False

    result = []
    i = 0
    for i in xrange(len(array)):
        if i < n - 1:
            heappush(result, array[i])
        else:
            element = heappop(result)
            if element < array[i]:
                heappush(result, array[i])
            else:
                heappush(result, element)

    return sorted(result)




array = [random.randint(1, 2000) for i in xrange(500)]
array = list(set(array))
print top_n(array, 30)

