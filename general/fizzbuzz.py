""" 
solution to famous fizzBuzz problem
"""

def fizzBuzz():
    for i in xrange(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print "fizzBuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i


fizzBuzz()
