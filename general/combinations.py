"""
print all combinations of a string
"""

def combine(string):
    if string is None or len(string) < 1:
        return False
    do_combine(string, [], len(string), 0, 0)


def do_combine(string, out_string, length, level, start):
    for i in xrange(start, length):
        out_string.append(string[i])
        print "".join(out_string)
        
        if i < length -1:
            # combine on the next level from the next character in string
            do_combine(string, out_string, length, level+1, i+1)
        out_string = out_string[:level]


combine("wxyz")
