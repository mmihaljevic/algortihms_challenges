"""
You are given an array of integers. Find all the combinations 
of the numbers of the array, that sum to another number(might 
be different for different combination) from the array.
One property of the array: The maximum number of the array will 
not be much greater than the others.
"""

def sum_to_other(array):
    if array is None or len(array) < 0:
        return False
    d = {}
    for i in xrange(len(array)):
        for j in xrange(1, len(array)):
            if i == j:
                pass
            else:
                sum = array[i] + array[j]
                if d.has_key(sum):
                    d[sum].append((array[i], array[j]))
                else:
                    d[sum] = [(array[i], array[j])]

    result = {}
    for i in xrange(len(array)):
        if d.has_key(array[i]):
            for element in d[array[i]]:
                if array[i] not in element:
                    if result.has_key(array[i]) and element not in result[array[i]]:
                        result[array[i]].append(element)
                    else:
                        result[array[i]] = [element] 

    return result        
    
l = [2, 4, 1, 3, 8, 4, 6]
print sum_to_other(l)

