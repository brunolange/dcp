""" Get product of all other elements

[1,2,3,4,5] -> [120, 60, 40, 30, 24]
[1,2,3]     -> [6, 3, 2]
"""

from functools import reduce

def product_excluding(arr):
    if not arr:
        return []

    def running_multiplier(acc, curr):
        if not acc:
            return [curr]
        acc.append(curr*acc[-1])
        return acc
    prefixes = reduce(running_multiplier, arr, [])
    suffixes = reduce(running_multiplier, reversed(arr), [])[::-1]

    def before_times_after(acc, curr):
        before, after = curr
        acc.append(before * after)
        return acc

    return reduce(before_times_after, zip([1] + prefixes[:-1], suffixes[1:] + [1]), [])

if __name__ == '__main__':
    assert product_excluding([1,2,3,4,5]) == [120, 60, 40, 30, 24]
    assert product_excluding([1,2,3]) == [6,3,2]
    assert product_excluding([]) == []
    assert product_excluding([42]) == [1]
