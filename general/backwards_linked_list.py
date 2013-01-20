"""
Reverse linked list
Input: linked list
Output: reversed linked list
"""

class Node(object):

    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


class LinkedList(object):
    
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        res = []
        node = self.head
        while node:
            res.append(str(node.data))
            node = node.next
        return '->'.join(res)

    def add(self, node):
        if node is None:
            return False
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def add_to_head(self, node):
        if node is None:
            return False
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


def reverse(head):
    reversed_list = LinkedList()
    current = head
    while current:
        # make new node so you don't make reference to already
        # existing node
        reversed_list.add_to_head(Node(current.data))
        current = current.next
    return reversed_list
    

nodes = [Node("1"), Node("2"), Node("3"), Node("4"), Node("5"), Node("6")]
list = LinkedList()
for node in nodes:
    list.add(node)

head = list.head
print list

reversed = reverse(list.head)
print reversed
