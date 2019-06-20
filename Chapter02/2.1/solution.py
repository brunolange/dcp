""" Find anagram indices

Given strings w and s, find all indices in s which are starting locations
of anagrams of w

Example:
    Given w, s = 'ab', 'abxaba'
    Return [0, 3, 4]
"""

from collections import defaultdict

def del_if_zero(freq, *chars):
    for char in chars:
        if freq[char] == 0:
            del freq[char]

def anagram_indices(word, s):
    result =  []
    freq = defaultdict(int)
    for char in word:
        freq[char] += 1
    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq, char)

    if not freq:
        result.append(0)

    for i in range(len(word), len(s)):
        start, end = s[i-len(word)], s[i]

        freq[start] += 1
        freq[end]   -= 1
        del_if_zero(freq, start, end)

        if not freq:
            result.append(i-len(word) + 1)

    return result

if __name__ == '__main__':
    assert anagram_indices('ab', 'abxaba') == [0, 3, 4]
