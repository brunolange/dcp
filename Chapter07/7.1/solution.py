"""
find floor and ceiling
"""
from models import Node, BST

def bounds(root, value):
    def _bounds(node, value, floor, ceil):
        if not node:
            return floor, ceil
        if value < node.value:
            return _bounds(node.left, value, floor, node.value)
        if value > node.value:
            return _bounds(node.right, value, node.value, ceil)
        return value, value

    return _bounds(root, value, None, None)

if __name__ == '__main__':
    tree = BST.from_array([4,2,1,3,6,5,7])

    print(bounds(tree.root, 4.1))
    print(bounds(tree.root, -1))
    print(bounds(tree.root, 9.99))
