
"""
Reconstruct tree from pre-order and in-order traversals
"""

def reconstruct(pre_order, in_order):
    if not pre_order and not in_order:
        return None

    if len(pre_order) == len(in_order) == 1:
        return pre_order[0]

    root = Node(pre_order[0])
    i = in_order.index(root.value)

    root.left = reconstruct(pre_order[1:i+1], in_order[:i])
    root.right = reconstruct(pre_order[i+1:], in_order[i+1:])

    return root

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '{} ({}, {})'.format(self.value, self.left or '', self.right or '')

if __name__ == '__main__':
    pre_order = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
    in_order =  ['d', 'b', 'e', 'a', 'f', 'c', 'g']

    print(reconstruct(pre_order, in_order))
