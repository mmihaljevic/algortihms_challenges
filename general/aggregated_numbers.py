"""
we will name a number "aggregated number" if this number has the following attribute:
just like the Fibonacci numbers
1,1,2,3,5,8,13.....

the digits in the number can divided into several parts, and the later part is the sum of the former parts.

like 112358, because 1+1=2, 1+2=3, 2+3=5, 3+5=8
122436, because 12+24=36
1299111210, because 12+99=111, 99+111=210
112112224, because 112+112=224
so can you provide a function to check whether this number is aggregated number or not?

question: are 1 and 11 aggregated numbers? in this solution they are not considered 
"""


def aggregated(number, path=[]):
    n = str(number)
    print n, path
    # sum the two is good
    if path == 3 and sum(path[:2]) == path([2]):
        if len(n) == 0:
            return True # nothing left
        else:
            path.pop() # we examined the path and don't like it
            return True and aggregated(n, list(path) )

    elif len(path)>3:
        return False

    out = False
    for i in range(1, len(n)+1):
        out |= aggregated(n[i:], path + [int(n[:i])])
    return out





# test cases
# wrong input
#print aggregated(None)
#print aggregated("1123")

# simple case - agregated number but starting from digit 1
print aggregated(11235813)

# complicated cases but also aggregated numbers
#print aggregated(122436)
#print aggregated(1299111210)
#print aggregated(112112224)

# not agregated number
#print aggregated(34577)
#print aggregated(122122488)
