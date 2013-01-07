"""
In an unsorted array of integers each except one appear twice
Find the element that appears once

Idea: Do xor on array and the one that is left as a result is element
that appears once
"""

def odd_man(array):
    if array is None or len(array) < 1:
        return False
    if len(array) == 1:
        return array[0]

    return reduce(lambda x, y: x ^ y, array)

array = [1, 3, 4, 3, 2, 5, 2, 5, 4]
print odd_man(array)
    
