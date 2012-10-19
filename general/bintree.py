# bin tree implementation
class Node(object):
	
	def __init__(self, data=None):
		self.data = data
		self.right = None
		self.left = None


class BinTree(object):

	def __init__(self, root=None):
		self.root = root

	def find(self, key):
		current = self.root
		while current is not None:
			if current.data == key:
				return current
			elif key < current.data:
				current = current.left
			else:
				current = current.right

		return False # we couldn't find a key in a tree

	def add(self, key):
		node = Node(key) # create a new node
		if self.root is None:
			self.root = node
		else:
			current = self.root
			while current is not None:
				if node.data < current.data:
					if current.left is None:
						current.left = node
						break
					else:
						current = current.left
				else:
					if current.right is None:
						current.right = node
						break
					else:
						current = current.right

	def add_array(self, array):
		if len(array) < 1:
			return
		if len(array) == 1:
			self.add(array[0])
			return
		m = len(array) / 2
		self.add(array[m])
		self.add_array(array[: m])
		self.add_array(array[m+1 :])

	def in_order(self, node):
		if node is None:
			return
		self.in_order(node.left)
		print node.data
		self.in_order(node.right)

	def pre_order(self, node):
		if node is None:
			return
		print node.data
		self.pre_order(node.left)
		self.pre_order(node.right)

	def post_order(self, node):
		if node is None:
			return
		self.post_order(node.left)
		self.post_order(node.right)
		print node.data
	
	def sum_leaves(self,node):
		if node is None:
			return 0
		elif node.left is None and node.right is None:
			return node.data
		return self.sum_leaves(node.left) + self.sum_leaves(node.right)

	
