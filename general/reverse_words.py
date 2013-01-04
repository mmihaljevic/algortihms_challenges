"""
rewerse words in sentence python way
"""

import re

def reverse_words(string):
    if string is None or len(string) < 1:
        return False
    rev = re.split(r'(\s+)', string)
    # inplace reverrse
    rev.reverse()
    rev = ''.join(rev)
    return rev

string = "this is one funky string"
print reverse_words(string)
