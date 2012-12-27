"""
find first missing number in an array of sorted numbers
e.g [4, 5, 6, 7, 9, 11, 14, 18, 19]
output: 8

expected complexity O(logn)
"""

def first_missing(array):
    if array is None or len(array) < 2:
        return False

    start_idx = 0
    end_idx = len(array) - 1

    # check if all elements are in array
    if array[end_idx] - array[start_idx] + 1 == len(array):
        return False

    med_idx = (start_idx + end_idx) / 2
    while end_idx - start_idx > 1:
        if array[med_idx] - array[start_idx] + 1 != len(array[start_idx : med_idx + 1]):
            end_idx = med_idx
        else:
            start_idx = med_idx

        med_idx = (end_idx + start_idx) / 2

    missing = array[start_idx] + 1
    return missing

# test cases
# 8
a1 = [4, 5, 6, 7, 9, 11, 14, 18, 19]
# 6
a2 = [5, 7]
# False
a3 = [3, 4, 5, 6, 7, 8, 9]
# False
a4 = [4]
# 12
a5 = [5, 6, 7, 8, 9, 10, 11, 14, 18, 19]

print first_missing(a1)
print first_missing(a2)
print first_missing(a3)
print first_missing(a4)
print first_missing(a5)

