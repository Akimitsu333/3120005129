class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insertLeft(self, value):
        if self.left is None:
            self.left = Node(value)
        else:
            node = Node(value)
            node.left = self.left
            self.left = node

    def insertRight(self, value):
        if self.right is None:
            self.right = Node(value)
        else:
            node = Node(value)
            node.right = self.right
            self.right = node
