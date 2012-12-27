"""
count number of identical chars in a given string and return number of highest count

idea: array of len 127 (chr(127) = ~)
use ord(char) to find index of array
"""

def count_max_chars(string):
    if string is None or len(string) < 1:
        return False
 
    # too expensive to make an array if len(string) is 1
    if len(string) == 1:
        return 1
    
    array = [0 for i in xrange(0, 128)]
    for c in string:
        id = ord(c)
        array[id] += 1
        
    return max(array)
   

# False
s1 = None
s2 = ""
# 1
s3 = "f"
# 4
s4 = "coffee tufee"

print count_max_chars(s1)
print count_max_chars(s2)
print count_max_chars(s3)
print count_max_chars(s4) 
