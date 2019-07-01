"""
LRU cache
"""
class LRU:
    class LinkedList:
        def __init__(self, head=None, tail=None):
            self.head = head
            self.tail = tail

        def add(self, node):
            if not self.head and not self.tail:
                self.head = self.tail = node
                return

            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        def remove(self, node):
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node == self.head:
                self.head = self.head.next
            if node == self.tail:
                self.tail = self.tail.prev
            node.prev = node.next = None

        def __repr__(self):
            if not self.head:
                return 'empty list'
            return '{}'.format(self.head)
    class Node:
        def __init__(self, value, nxt=None, prev=None):
            self.value = value
            self.next = nxt
            self.prev = prev
        def __repr__(self):
            return '{}{}'.format(self.value, ' <-> {}'.format(self.next) if self.next else '')

    def __init__(self, size):
        self._size = size
        self._cache = {}
        self._ll = LRU.LinkedList()
        self._node_map = {}

    def set(self, key, value):
        if len(self._cache) == self._size:
            least_used_key = self._ll.head.value
            print('luk', least_used_key)
            node = self._node_map[least_used_key]
            self._ll.remove(node)
            del self._cache[least_used_key]
            del self._node_map[least_used_key]

        node = LRU.Node(key)
        self._ll.add(node)
        self._node_map[key] = node
        self._cache[key] = value

    def get(self, key):
        data = self._cache[key]
        node = self._node_map[key]
        self._ll.remove(node)
        self._ll.add(node)
        return data

    def __repr__(self):
        return '{}'.format(self._ll)

if __name__ == '__main__':
    cache = LRU(3)
    cache.set('a', 1)
    cache.set('b', 2)
    cache.set('c', 3)
    print(cache)
    cache.set('d', 4) # a is popped
    print(cache)
    _ = cache.get('b')
    print(cache)
    _ = cache.get('c')
    print(cache)
    print(cache.get('b'))
    print(cache.get('a'))
