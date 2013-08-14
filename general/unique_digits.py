"""
print the numbers without repeating digits in it and with in the range x to y.
ex. range 50 to 5000, 
then it must print like 50,51,52,53,54,56,....57,......65,67,....76,77....109,120,123,124...4987. 
not like 556,55, .avoid duplicate digits in number.
"""


def unique_digits(x,y):
    if x >= y:
        return False
    for number in xrange(x, y):
        repr = str(number)
        d = {}
        unique = True
        for j in repr:
            if d.has_key(j):
                unique = False
                break
            d[j] = 1
        if unique:
            print number


unique_digits(50, 590)

        
