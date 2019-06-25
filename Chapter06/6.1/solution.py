"""
Count number of unival trees
"""

def count_unival(root):
    count, _ = _count_unival(root)
    return count

def _count_unival(node):
    if not node:
        return 0, True

    left_count, is_unival_left = _count_unival(node.left)
    right_count, is_unival_right = _count_unival(node.right)

    total_count = left_count + right_count

    if is_unival_left and is_unival_right:
        if node.left and node.left.value != node.value:
            return total_count, False
        if node.right and node.right.value != node.value:
            return total_count, False
        return 1 + total_count, True

    return total_count, False

def unival_trees(root):
    trees, _ = _unival_trees(root)
    return trees

def _unival_trees(node):
    if not node:
        return [], True

    left_trees, is_left_unival = _unival_trees(node.left)
    right_trees, is_right_unival = _unival_trees(node.right)
    all_trees = left_trees + right_trees

    if is_left_unival and is_right_unival:
        if node.left and node.left.value != node.value:
            return all_trees, False
        if node.right and node.right.value != node.value:
            return all_trees, False
        return [node] + all_trees, True

    return all_trees, False

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '{}, ({}, {})'.format(self.value, self.left or '', self.right or '')

if __name__ == '__main__':
    root = Node(3, Node(12), Node(5, Node(5), Node(5)))
    print(count_unival(root))
    _ = [print(tree) for tree in unival_trees(root)]
