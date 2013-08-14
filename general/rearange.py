"""
You have two arrays src, tgt, containing two permutations of the numbers 0..n-1. 
You would like to rearrange src so that it equals tgt. The only allowed
operations is "swap a number with 0", e.g. {1,0,2,3} -> {1,3,2,0} ("swap 3 with 0"). 
Write a program that prints to stdout the list of required operations.
"""
def rearrange(src,tgt):
    if len(src) != len(tgt):
        return False
    if src == tgt:
        return True
    in_place = False
    while not in_place:
        for i in xrange(len(src)):
            if src[i] != tgt[i]:
                # swap
                b = src.index(0)
                src[i], src[b] = src[b], src[i]
            if src == tgt:
                in_place = True
                break
    return src


print rearrange([0,1,3,2], [1,0,2,3])
               

