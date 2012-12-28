"""
given an array of integers - generate output using product of all exceot that integer
e.g. input: 1,2,3,4
output: (2*3*4), (1*3*4), (1*2*4), (1*2*3)

O(n) + O(n) -> O(n)
"""

def product(array):
    # doesn't make sense to have array of len 1
    if array is None or len(array) < 2:
        return False

    # product of all O(n)
    product = reduce(lambda x, y: x * y, array)
    
    # devide product by each O(n)
    result = map(lambda x: product / x, array)   
    return result


# test cases
a1 = None
a2 = [1, 2, 3, 4]
a3 = [3, 4]

print product(a1)
print product(a2)
print product(a3)
