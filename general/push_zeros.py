"""
Push all the zero's of a given array to the end of an array in place
 [1,2,0,4,0,0,8] -> [1,2,4,8,0,0,0]

first solution:
O(n^2)
def push_zeros(array):
    if array is None or len(array) < 1:
        return False

    for i in xrange(len(array)):
        if array[i] == 0:
            # find number to replace
            switched = False
            for j in xrange(i, len(array)):
                if array[j] != 0:
                    array[i], array[j] = array[j], array[i]
                    switched = True
                    break

            if not switched:
                # all zeros trailing
                return array
    return array

"""

# Better solution O(n)
def push_zeros(array):
    if array is None or len(array) < 1:
        return False
    
    pos = 0
    for i in xrange(len(array)):
        if array[i] != 0: 
            if pos != i:
                array[pos],array[i] = array[i],array[pos]
            pos += 1


    return array
