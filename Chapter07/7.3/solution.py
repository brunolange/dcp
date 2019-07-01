"""
Build all BSTs with nodes [1,2,3,..,n]
"""

from models import Node, BST
from functools import reduce, partial
from operator import iconcat

def make_trees(n):
    return _make_trees(1, n)

flatten = lambda nested: reduce(iconcat, nested, [])

def _make_trees(low, high):
    if low > high:
        return [None]

    return flatten([
        flatten([[
            Node(i, left=l, right=r)
            for l in _make_trees(low, i - 1)]
            for r in _make_trees(i + 1, high)
        ])
        for i in range(low, high+1)
    ])


def mt(n):
    return _mt(1, n)

def _mt(low, high):
    if low > high:
        return [None]

    trees = []
    for i in range(low, high+1):
        left = _mt(low, i-1)
        right = _mt(i+1, high)
        for l in left:
            for r in right:
                trees.append(Node(i, l, r))
    return trees

import time
if __name__ == '__main__':
    t0 = time.time()
    for n in range(1, 12):
        trees = make_trees(n)
        print('{:<3}{}'.format(n, len(trees)))
    print('{:.3f} seconds'.format(time.time() - t0))