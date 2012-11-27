import re

def flatten(string):
    if string is None or not isinstance(string, str) or len(string) < 1:
        return False
    tmp = re.split('[,\s\n\t]', string)
    opened = 0
    result = []
    for i in xrange(len(tmp)):
        if tmp[i] == '(':
            opened += 1
        elif tmp[i] == ')':
            opened-= 1
        elif tmp[i] == "":
            pass
        else:
            result.append(tmp[i])
    if opened == 0:
        return ",".join(result)
    return False

list = "( 1,( 2, 3 ), ( 4, ( 5, 6 ), 7 ) )"
list2 = "( ( ( ( ( 5 ) ) ) ) )"
list3 = "( ( 4 ) ) )"

print flatten(list)
print flatten(list2)
print flatten(list3)
