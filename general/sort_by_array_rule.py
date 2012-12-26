"""
Given two arrays, array1 and array2
using the rule of array1 to sort array2.
Ex. 
array1 = { B, A, C}
array2 = {A, B, A, C, A, B, B, C, A}
output: sortedArray2 = {B,B,B,A,A,A,A,C,C}

What if array2 existed some element not existed in Array1? 
Can you put it in the end? and sorted by alphabetical? 
What if array have lower case and upcases letter?

Assumptions:
- if array2 has some elements that are not in array1: put them in the end 
- capitalization matters

O(m+n)
"""

def sort_by_array(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) < 1 or len(array2) is None:
        return False
    
    # dictionary with keys from array1
    dict_rules = {}
    
    for key in array1:
        dict_rules[key] = 0
    
    for element in array2:
        if dict_rules.has_key(element):
            dict_rules[element] += 1
        else:
            dict_rules[element] = 1
    
    result = []
    # sort by key
    for key in array1:
        count = dict_rules[key]
        if count > 0:
            result.extend([key]*count)
    
        # remove entry - easier to get keys that are not in array1
        del(dict_rules[key])
    
    # keys not in array1 
    keys = sorted(dict_rules.keys())
    for key in keys:
        count = dict_rules[key]
        result.extend([key] * count)

    return result

array1 = ['B', 'A', 'C']
array2 = ['A', 'C', 'B', 'D', 'E', 'A', 'B', 'B', 'C', 'D', 'D', 'A', 'A', 'C']

print array2
print sort_by_array(array1, array2)
