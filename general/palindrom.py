"""
check if a given string is palindrom

a) how long is the string? can it fit into memory? - if it cannot - think of 
putting only one half in some structure that keeps order and just remove elements as you 
read the other half - linked list :) - need to know length
b) is empty string considered palindrom? - for this solution - not
c) check that input is really a string - isinstance(x, str)
d) don't forget that string can be sentence - spaces, tabs, puncation charatcters, capitalization
e) usage?
f) unicode or some other format that can get us to other problems?


Test cases:
a) wrong input:
  None, "", "        ", 1234
b) not a palindrom
c) palindrom with no spaces and puncation chars
d) palindrom with spaces and punctation chars
e) string with only one char - palindrom

"""

import re


def is_palindrom(string):
    # input check
    if string is None or not isinstance(string, str):
        return False
    
    string = string.strip()
    # remove spaces and puncation chars
    tmp_str = re.split("[',.!:-;\s\n\t]", string)
    
    string = "".join(tmp_str)
    # fix capitalization
    string = string.lower()
    if len(string) < 1:
        return False
    if len(string) == 1:
        return True 
    i = 0
    j = len(string) - 1 
    
    while j - i >= 1:
        if string[i] != string[j]:
            return False
        j -= 1
        i += 1
    return True


# test cases
print is_palindrom(None)
print is_palindrom("")
print is_palindrom("         ")
print is_palindrom("Live long and prosper!")
print is_palindrom("aaaabbaaaa")
print is_palindrom("Dammit I'm mad!")
