"""
Given an array with positive, negative and zeros, arrange the given 
array such that negatives are on left, zeros in the middle and 
positives on the righ
"""

def order(array):
    if array is None or len(array) < 1:
        return False
    # see if 0 exists in array if not just take any number as first
    number_zeros = 0
    if 0 in array:
        element = 0
        number_zeros = array.count(0)
    else:
        element = array[0]

    return [i for i in array if i < element] +\
            [0 for i in xrange(number_zeros) ] +\ 
            [i for i in array if i > element]


# test cases
array1 = [1, 5, 0, 2, -3, -7, 4, 0, 0, -6, 5]
print order(array1)

array2 = [-1, 3, -5, 4, -2, -1, -3, 2, 3]
print order(array2) 
