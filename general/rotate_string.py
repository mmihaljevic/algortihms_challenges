"""
rotate sting of n elements left or right by i positions
"""

def rotate_left(string, i):
    # if i is larger than string - it doesn't make sanse to make rotation
    while i > len(string):
        i -= len(stringi)
    string = string[i:] + string[0:i]
    return string

def rotate_right(string, i):
    while i > len(string):
        i -= len(string)
    string = string[-i:] + string[0: -i]
    return string

def rotate(string, i, direction):
    if string is None or len(string) < 1:
        return False
    if i is None or i < 1:
        return False
    if direction is None or direction.lower() not in ['r', 'l']:
        return False
    # rotation of a string with len 1 is always the same string
    if len(string) == 1:
        return string
    
    if direction.lower() == 'r':
        return rotate_right(string, i)

    else:
        return rotate_left(string, i)



string = "abcdefgh"
i = 3
print rotate(string, i, 'r')
print rotate(string, i, 'l')
