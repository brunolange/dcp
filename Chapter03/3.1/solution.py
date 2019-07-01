"""
Reverse a linked list
"""

class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt
    def __repr__(self):
        return '{} -> {}'.format(self.value, self.next if self.next else '')

def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def reverse_recursive(head):
    head, _ = _reverse_recursive(head)
    return head

def _reverse_recursive(node):
    if not node.next:
        return node, node

    head, tail = _reverse_recursive(node.next)
    node.next = None
    tail.next = node

    return head, node

if __name__ == '__main__':
    ll = Node(1, Node(2, Node(3)))
    ll = reverse(ll)
    print(ll)
    ll = reverse_recursive(ll)
    print(ll)
