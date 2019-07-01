"""
build a Huffman tree
"""

from collections import defaultdict
from functools import reduce
import heapq

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.value < other.value if self.value and other.value else False

    def __repr__(self):
        return '({}, {}, {})'.format(self.value, self.left if self.left else '-', self.right if self.right else '-')

def huffman_tree(freq):
    pool = []
    for char, count in freq.items():
        heapq.heappush(pool, (count, Node(char)))

    while len(pool) >= 2:
        count_left, left = heapq.heappop(pool)
        count_right, right = heapq.heappop(pool)
        parent = Node(None, left=left, right=right)
        heapq.heappush(pool, (count_left + count_right, parent))

    _, root = pool[0]
    return root

def build_frequencies(str):
    freq = defaultdict(int)
    for char in str:
        freq[char] += 1
    return freq

def encoding(root):
    mapping = {}
    _encoding(root, '', mapping)
    return mapping

def _encoding(node, string, mapping):
    if not node:
        return

    if not node.left and not node.right:
        mapping[node.value] = string
        return

    _encoding(node.left, string + '0', mapping)
    _encoding(node.right, string + '1', mapping)

def encode(message, encoding):
    return ''.join(encoding[c] for c in message)

def decode(binary, root):
    msg = ''
    node = root
    for b in binary:
        node = node.left if b == '0' else node.right
        if node.value:
            msg += node.value
            node = root

    return msg

if __name__ == '__main__':
    db = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Dolor purus non enim praesent elementum facilisis. A iaculis at erat pellentesque. Nulla facilisi cras fermentum odio eu feugiat pretium nibh.
Sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae. Non arcu risus quis varius quam quisque id diam vel.
Auctor eu augue ut lectus arcu. Magna fringilla urna porttitor rhoncus dolor purus non enim.
Nunc aliquet bibendum enim facilisis gravida neque convallis a. Bibendum neque egestas congue quisque egestas diam.
Mi quis hendrerit dolor magna eget est lorem. Sed velit dignissim sodales ut. Morbi quis commodo odio aenean sed adipiscing diam donec.
Risus ultricies tristique nulla aliquet enim tortor at auctor urna. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae.
Arcu odio ut sem nulla pharetra diam. In mollis nunc sed id semper risus in. Eget felis eget nunc lobortis mattis aliquam. Ac feugiat
sed lectus vestibulum mattis ullamcorper. Blandit cursus risus at ultrices mi tempus imperdiet.

Sed augue lacus viverra vitae congue eu consequat. Lacus vestibulum sed arcu non odio euismod lacinia at quis. Sagittis purus sit amet
volutpat consequat mauris nunc congue nisi. Mauris sit amet massa vitae tortor. Quam quisque id diam vel. Sed felis eget velit aliquet
sagittis id consectetur. Pretium nibh ipsum consequat nisl vel pretium lectus quam. Viverra ipsum nunc aliquet bibendum enim facilisis.
Viverra nibh cras pulvinar mattis nunc sed blandit. Diam vulputate ut pharetra sit amet. Feugiat in fermentum posuere urna nec.

Morbi tristique senectus et netus et malesuada fames ac. Tellus molestie nunc non blandit massa enim. Malesuada fames ac turpis egestas
integer. Duis ultricies lacus sed turpis tincidunt id aliquet risus feugiat. Duis at consectetur lorem donec massa. Eget nullam non nisi
est sit. Faucibus purus in massa tempor nec feugiat nisl. Hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper.
Dolor sit amet consectetur adipiscing elit ut aliquam purus sit. Purus semper eget duis at tellus. Orci eu lobortis elementum nibh tellus
molestie nunc non blandit. Orci a scelerisque purus semper eget duis at tellus at.

Non blandit massa enim nec dui nunc. Nec feugiat in fermentum posuere urna nec tincidunt praesent semper.
Nibh cras pulvinar mattis nunc sed blandit libero volutpat sed. Nulla posuere sollicitudin aliquam ultrices sagittis orci.
Tortor vitae purus faucibus ornare suspendisse sed nisi lacus sed. Placerat vestibulum lectus mauris ultrices.
Gravida cum sociis natoque penatibus et magnis dis. Commodo elit at imperdiet dui accumsan sit amet.
Sollicitudin ac orci phasellus egestas tellus. At elementum eu facilisis sed odio morbi quis commodo. Sit amet nulla facilisi morbi.
Vitae congue eu consequat ac felis donec et odio. Magna etiam tempor orci eu lobortis elementum nibh.
Interdum consectetur libero id faucibus. Tincidunt eget nullam non nisi. Massa enim nec dui nunc mattis enim.
Lobortis mattis aliquam faucibus purus in massa.

Velit aliquet sagittis id consectetur. Sit amet tellus cras adipiscing. Pretium quam vulputate dignissim suspendisse in est ante in.
Integer vitae justo eget magna. In nisl nisi scelerisque eu ultrices. Elit ut aliquam purus sit amet.
Et netus et malesuada fames ac turpis egestas. Enim nec dui nunc mattis enim ut tellus elementum sagittis.
Sit amet risus nullam eget. Sagittis id consectetur purus ut faucibus pulvinar elementum.
Hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper.
Cras semper auctor neque vitae tempus quam pellentesque nec.
    """

    frequencies = build_frequencies(db)
    tree = huffman_tree(frequencies)
    mapping = encoding(tree)

    _ = [print('[{:^3}]|{:<3}|{}'.format(char, frequencies[char], mapping[char])) for char in sorted(frequencies.keys())]

    msg = 'Lorem ipsum dolor sit amet.'
    binary = encode(msg, mapping)
    decoded = decode(binary, tree)
    assert msg == decoded
