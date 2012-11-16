"""
check if the sum of 3 numbers in array is X
array is not sorted

Possible solutions:
Naive: check 3 times: O(n^3)
Sort array and find sum - x- y -> z : O(n^2*log(n))
Hash table: write sum - x - y in HT  O(n^2)
            linear check for each z is it in HT O(n) -- > O(n^2)

"""

def sum_three(array, sum):
    # if len(array) < 3 we don't have enough elements to check
    if array is None or len(array) < 3:
        return False
    if sum is None:
        return False

    hm = {}
    length = len(array)
    for i in xrange(length):
        for j in xrange(i, length):
            tmp = sum - (array[i] + array[j])
            if not hm.has_key(tmp):
                hm[tmp] = (i,j)

    for i, e in enumerate(array):
        if hm.has_key(e) and i not in hm[e]:
            return hm[e] , i

    return False



array = [0, 1, 5, 9, 1, 10, 11, 3, -15, -4, 2, 0, -6, 7,]
sum = 0

print sum_three(array, sum)
