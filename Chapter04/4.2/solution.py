"""
([])[]({}) => True
([)] => False
"""

def balanced(str):
    stack = []
    pairs = {('{', '}'), ('(', ')'), ('[', ']')}
    openings = {p[0] for p in pairs}
    for i, char in enumerate(str):
        if char in openings:
            stack.append(char)
            continue
        if not stack or (stack[-1], char) not in pairs:
            return False, i
        _ = stack.pop()
    is_balanced = len(stack) == 0
    return is_balanced, (None if is_balanced else len(str) - 1)

if __name__ == '__main__':
    print(balanced("([])[]({})"))
    print(balanced("{{((([[[[]"))
    print(balanced("([)]"))
