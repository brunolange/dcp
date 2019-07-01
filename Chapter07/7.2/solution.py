"""
convert sorted array to BST
"""

from models import Node, BST

def from_sorted_array(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = from_sorted_array(arr[:mid])
    root.right = from_sorted_array(arr[mid+1:])
    return root

if __name__ == '__main__':
    arr = list(range(15))
    print(from_sorted_array(arr))
