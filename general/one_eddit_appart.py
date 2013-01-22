"""
check if two words are one edit distance
* inset character - or add to beginning or end
* remove one character - the same as adding in reverse
* replace exactly one character
"""

def distance_remove(s1, s2):
    s1 = [e for e in s1]
    s2 = [e for e in s2]
    for i in xrange(len(s1)):
        if s1[: i] + s1[i + 1 :] == s2:
            return True
    return False

def replace_one(s1, s2):
    s1 = [e for e in s1]
    s2 = [e for e in s2]
    counter = 0
    # count number of different letters
    for i, e in enumerate(s1):
        if e != s2[i]:
            counter += 1
    return counter == 1
               

def is_one_edit_distance(s1, s2):
    # first check if strings are defined
    if s1 is None or len(s1) < 1 or s2 is None or len(s2) < 1:
        return False    
    # check that difference between lengths s1 or s2 are at most 1
    if len(s1) == len(s2): 
        # False if they are the same
        if s1 == s2:
            return False       
        return replace_one(s1,s2)
        
    elif abs(len(s1) - len(s2)) == 1:
        if s1 > s2:
            return distance_remove(s1, s2) 
        else:
            return distance_remove(s2, s1)   
    else:
        return False
   
# test cases
s1 = "home" 
s2 = "ho"
print is_one_edit_distance(s1, s2)

s1 = "home" 
s2 = "home"
print is_one_edit_distance(s1, s2)

s1 = "homes" 
s2 = "home"
print is_one_edit_distance(s1, s2)
print is_one_edit_distance(s2, s1)

s1 = "homes" 
s2 = "hobes"
print is_one_edit_distance(s1, s2)
print is_one_edit_distance(s2, s1)
