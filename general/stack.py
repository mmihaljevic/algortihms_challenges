
class Stack(object):

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def clear(self):
        self.stack = []



s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
print s.pop()
print s.pop()
