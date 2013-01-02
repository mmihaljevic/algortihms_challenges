"""
How would you design a stack which, in addition to push and pop, also has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.

Idea: use another 'stack that keeps current min'

what if stack has elements that are same - if element == min - append to current min 
"""
from random import randint
from time import sleep

class Stack(object):

    def __init__(self):
        ''' stack initialization '''
        self.stack = []
        self.min = []

    def __str__(self):
        ''' nice output of the stack '''
        result = []
        if len(self.stack) < 1:
            result.append("stack is empty [   ]")
        else:
            result.append("stack: ")
            for i in xrange(len(self.stack) - 1, -1, -1):
                print i
                result.append("[ " + str(self.stack[i]) + "]")
                result.append("--------") 
        return '\n'.join(result)

    def push(self, element):
        ''' push to stack '''
        self.stack.append(element)
        # append minimum if found
        # append element if min == element so you keep min when you pop an element
        if len(self.min) == 0 or element <= self.min[-1]:
            self.min.append(element)

    def pop(self):
        ''' pop element from stack '''
        if len(self.stack) < 1:
            return 
        element = self.stack.pop()
        # remove from min if element is current min
        if element == self.min[-1]:
            self.min.pop()
        return element
            
    def minimum(self):
        ''' returns min element of a stack in O(1) '''
        return self.min[-1]        


# test elements - randomly generated integers - 200 integers in the range of 100
x = [randint(1, 100) for i in xrange(200)]
stack = Stack()
for i in xrange(len(x)):
    if i % 3 == 0:
        stack.pop()
    stack.push(x[i])
    print stack
    print stack.minimum()
    sleep(2) 
