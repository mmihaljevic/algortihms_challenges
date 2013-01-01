"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

class Node(object):

    def __init__(self, datum=None):
        self.datum = datum
        self.next = None

class LinkedList(object):

    def __init__(self, node=None):
        self.head = node
      
    def __str__(self):
        ''' nice output for testing data '''
        node = self.head
        output = []
        while node:
            output.append(str(node.datum))
            node = node.next
        return '->'.join(output)
 
    def add(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def remove(self, datum):
        current = self.head
        if current.datum == datum:
            self.head = current.next
        while current.next:
            if current.next.datum == datum:
                current.next = current.next.next
                break
            current = current.next
       
    # remove duplicates - using additional data structure
    def remove_duplicates(self):
        if self.head is None:
            return False
        unique = {}
        unique[self.head.datum] = 1
        node = self.head 
        while node.next:
            if unique.has_key(node.next.datum):
                node.next = node.next.next
            else:
                unique[node.next.datum] = 1
                node = node.next
     
# test data
n1 = Node(1)    
n2 = Node(12)
n3 = Node(5)
n4 = Node(11) 
n5 = Node(12)
n6 = Node(5)
n7 = Node(7)
n8 = Node(9)
n9 = Node(9)

list = LinkedList()
list.add(n1)
print list

list.add(n2)
print list

list.add(n3)
print list

list.add(n4)
print list

list.add(n5)
print list

list.add(n6)
print list

list.add(n7)
print list

list.add(n8)
print list

list.add(n9)
print list

list.remove_duplicates()
print list

#list.remove(11)
#print list
