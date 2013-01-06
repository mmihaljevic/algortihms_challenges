"""
if an array is given like 11 increment its value to 1 o\p should be 12
if the array has 99 o\p should be 100

questions: 
* increment by 1 or should be configurable
* is there any array length boundary?

"""

def increment_array(array, i):
    if array is None or len(array) < 1:
        return False
    if i is None:
        return False
    cont = True
    j = len(array) - 1
    while cont and j>=0:
        sum = array[j] + i
        if sum > 9:
            array[j] = sum % 10
            i = 1 # reminder == i
            j -= 1
        else:
            array[j] = sum
            cont = False
    
    # insert at the begining of an array
    if cont:
        array.insert(0,1)
    
    return array


# test cases
arrays = [[], [1], [9], [1, 5], [2, 9], [9,9,9]]
for array in arrays:
    print increment_array(array, 1)
