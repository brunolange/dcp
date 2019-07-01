"""
find intersecting node of linked lists
"""

from functools import reduce

class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __len__(self):
        if not self.next:
            return 1
        return 1 + len(self.next)

    def __repr__(self):
        return '{}{}'.format(self.value, '->{}'.format(self.next) if self.next else '')

    @staticmethod
    def from_list(arr):
        if not arr:
            return None
        return Node(arr[0], Node.from_list(arr[1:]))

    @staticmethod
    def from_list_reduce(arr):
        def r(acc, curr):
            head, tail = acc
            tail.next = Node(curr)
            return head, tail.next
        head = Node(arr[0])
        head, _ = reduce(r, arr[1:], (head, head))
        return head

def intersection(h1, h2):
    longest, smallest = (h1, h2) if len(h1) >= len(h2) else (h2, h1)
    for _ in range(len(longest) - len(smallest)):
        longest = longest.next
    while smallest != longest:
        smallest = smallest.next
        longest = longest.next
    return smallest

if __name__ == '__main__':
    common = Node.from_list([8,5,6,9,1])
    h1 = Node(6, Node(3, common))
    h2 = Node(7, Node(4, Node(1, Node(2, Node(3, Node(0, common))))))
    print(intersection(h1, h2))