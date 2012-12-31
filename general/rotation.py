"""
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring (i.e. 'waterbottle' is a rotation of 'erbottlewat')
"""

# implementation of is_substring
def is_substring(s1, s2):
    if s1 in s2:
        return True
    return False

def is_rotation(s1, s2):
    if s1 is None or s2 is None or len(s1) != len(s2):
        return False
    return is_substring(s2, s1 + s1)
       

s1 = "waterbottle"
s2 = "erbottlewat"
print is_rotation(s1, s2)


