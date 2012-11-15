"""
print all permutations

"""

def permutation(string):
    if string is None or len(string) < 0:
        return False
    do_permute(string, [], [False for i in xrange(len(string))], len(string), 0)


def do_permute(string, out, used, length, level):
    if level == length:
        print "".join(out)
        return

    for i in xrange(length):
        if used[i]:
            continue
        out.append(string[i])
        used[i] = True
        do_permute(string, out, used, length, level +1)
        used[i] = False
        out = out[:level] # return out to the begining length for that level

permutation("abcd")
       
