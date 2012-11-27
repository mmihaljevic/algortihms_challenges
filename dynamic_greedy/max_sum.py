
def max_sum(array):
    if array is None or len(array) <1:
        return False
    max_sum = array[0]
    current = array[0]
    res = []
    tmp_res = []
    for element in array[1:]:
        current += element
        res.append(element)
        if max_sum < current:
            max_sum = current
            tmp_res = res[:]
        if current < 0: 
            current = 0
            res = []
    return max_sum, tmp_res

print max_sum([-2,-1,-3,4,-1,2,1,-5, 4])
