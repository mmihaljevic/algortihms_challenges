"""
Binary search implementation
O(log(n)) 
suitable when data is sorted
"""

# check input data in separate method
def binary_search(array, key):
    if array is None or len(array) < 1:
        return False
    if key is None:
        return False

    return bin_search_rec(array, key, 0, len(array) - 1)



# recursive solution
# space consuming
def bin_search_rec(array, key, start, end):
    med = (start + end) / 2
    if array[med] == key:
        return med
    elif med == start or med == end:
        return False
    elif array[med] < key:
        return bin_search_rec(array, key, med, end)
    else:
        return bin_search_rec(array, key, start, med)

# iterative solution
def bin_search_it(array, key, start, end):
    med = (start + end) / 2

    while med != start:
        if array[med] == key:
            return med
        elif array[med] < key:
            start = med
        else:
            end = med
        med = (start + end) / 2

    if array[med] == key:
        return med
    return False


# test cases for main methos (assume correct input)
array = [1, 2, 5, 6, 7, 8, 9, 11, 23, 45, 46, 68]
key_1 = 2
key_2 = 45
key_3 = 55
key_4 = 3

print bin_search_rec(array, key_1, 0, len(array) -1)
print bin_search_rec(array, key_2, 0, len(array) -1)
print bin_search_rec(array, key_3, 0, len(array) -1)
print bin_search_it(array, key_1, 0, len(array) -1)
print bin_search_it(array, key_2, 0, len(array) -1)
print bin_search_it(array, key_3, 0, len(array) -1)

