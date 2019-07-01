class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '({}, {}, {})'.format(
            self.value,
            self.left if self.left else '-',
            self.right if self.right else '-'
        )

class BST:
    def __init__(self, root=None):
        self.root = root

    def find(self, value):
        return self._find(value, self.root)

    def _find(self, value, node):
        if not node:
            return None
        if value < node.value:
            return self._find(value, node.left)
        if value > node.value:
            return self._find(value, node.right)
        return node

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self._insert(value, node.left)

        if value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def __repr__(self):
        return '{}'.format(self.root)

    @staticmethod
    def from_array(arr):
        tree = BST(Node(arr[0]))
        for i in range(1, len(arr)):
            tree.insert(arr[i])
        return tree