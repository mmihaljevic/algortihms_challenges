"""
given a function returning random integers from 0 to 4 inclusive with equal 
probability, write a function returning random integers from 0 to 6 inclusive.

* the solution should also return distributed values

"""
import random

# returns random integer from 0 to 4
def random4():
    return random.randint(0,4)


# idea 1
# value 1 has more chances to be picked up - 1, (4+4) than other values
# valur 0 has more chances to be picked up also 
def random6_a():
    return (random4() + random4()) % 7

# idea 2 
# The sum of two independent, equally distributed, uniform distributions 
# yields a symmetric triangular distribution.
def random6_b():
    random8 = random4() + random4()
    if random8 > 6:
        return random6_b()
    return random8

# correct answer:
# rand3() returns uniformly distributed values from 0 to 3 doing so by rejecting 
# 4 output of rand4() 
# Well, we now have two random bits, each one being either 0 or 1 with 
# 50% probability
def random3():
    rand = random4()
    if rand == 4:
        return random3()
    return rand

def random15():
    return random3() << 2 + random3()

def random7():
    return random15() >> 1

def random6():
    rand = random7()
    if rand > 6:
        return random6()
    return rand


# test
x1 = []
x2 = []
x3 = []

for i in xrange(100):
    x1.append(random6_a())
    x2.append(random6_b())
    x3.append(random6())

# check if each element is in 1-6
for i in x1:
    assert 0 <= i <= 6

for i in x2:
    assert 0 <= i <= 6

for i in x3:
    assert 0 <= i <= 6

print x1, sorted(x1)
print x2, sorted(x2)
print x3, sorted(x3)
