"""
structute - list like - don't know how long it is 
element_at(x) - give element or IndexError
is x in structure


Observations:
- what kind of elements are there
- is structure growing or staying the same all the time - should stay cause if we get 
IndexError - that index will never be checked again
- elements need to be sorted - otherwise we will need to do linear search 
  element_at(0), element_at(1) ....
- where will this be used (is it important?)
- what are the cases when I get that kind of structure?
- paralelize (each gets modulo n elements to check?)
- are all elements unique? - test structure is built in the way that all elements are unique
"""
import random

# structure for testing
class Structure(object):
    
    def __init__(self):
        # create random integers, take only unique and sort
        self.data = [random.randint(0,3000) for i in xrange(6000)]
        self.data = list(set(self.data))
        self.data = sorted(self.data)

    def element_at_position(self, x):
        return self.data[x]

    def x_in_structure(self, x):
        """ is x in structure """
        return x in self.data

s = Structure()

def is_x_in_struct(x):
    # check that structure is not empty
    try:
        e = s.element_at_position(0)
        if e == x:
            return True

    except IndexError:
        return False

    # do we know how at most elements can structure have
    # assume yes    
    bound = pow(10, 10)

    i = bound/2
    while bound > i:
        try:
            e = s.element_at_position(i)
            if e == x:
                return True
            elif e > x:
                bound = i
                i = i / 2
            else:
              i = (bound + i) / 2
        except IndexError:
            bound = i
            i = i / 2

    return False

print s.x_in_structure(5)
print is_x_in_struct(5)
print s.x_in_structure(8)
print is_x_in_struct(8)
 
