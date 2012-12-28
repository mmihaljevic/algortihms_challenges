"""
given a set of non overlapping intervals and another interval - merge them

hold priority queue - check with two intervals if they can be merged - merge them and 
leave idx like it is.

"""
from heapq import heappush
from heapq import heappop
from heapq import heapify

def interval_overlapping(array, interval):
    if array is None or len(array) < 1:
        return False
    if interval is None or len(interval) != 2:
        return False
    
    heapify(array)
    heappush(array, interval)

    result = [] 
    # number of elements in queue is at least 2 - checked
    while len(array) > 1:
        xf, yf = heappop(array)
        xs, ys = heappop(array)

        if yf < xs:
            result.append((xf, yf))
            heappush(array, (xs,ys))
        else:
            x = min(xf, xs)
            y = max(yf, ys)
            heappush(array, (x,y))

    result.append(heappop(array))  
    return result

    

# test cases
array1 = [(1, 3)]
interval1 = (5, 6)

array2 = [(1,4), (6, 10), (14, 19)]
interval2 = (13, 17)

array3 = [(1,5), (6, 15), (20, 21), (23, 26), (27, 30), (35, 40)]
interval3 = (14, 33)

print interval_overlapping(array1, interval1)
print interval_overlapping(array2, interval2)
print interval_overlapping(array3, interval3)
