"""
Calculate maximum subarray sum
"""

def maximum_subarray(arr):
    max_global, max_local = float('-inf'), float('-inf')
    for number in arr:
        # max_local: either start new here or keep accumulating
        max_local = max(max_local + number, number)
        # is this local max the new global one?
        max_global = max(max_global, max_local)
    return max_global

def maximum_circular_subarray(arr):
    def minimum_subarray(arr):
        min_global, min_local = float('inf'), float('inf')
        for number in arr:
            min_local = min(min_local + number, number)
            min_global = min(min_global, min_local)
        return min_global

    # solution is either in the normal case or the wraparound one
    return max(maximum_subarray(arr), sum(arr) - minimum_subarray(arr))

if __name__ == '__main__':
    assert maximum_subarray([34, -50, 42, 14, -5, 86]) == 137
    assert maximum_subarray([-1,-2,-3]) == -1
    assert maximum_subarray([]) == float('-inf')
