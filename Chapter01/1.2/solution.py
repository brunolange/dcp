"""
Find smallest window to be sorted
"""

def solution(arr):
    n = len(arr)
    left, right = 0, 0
    running_max, running_min = float('-inf'), float('inf')

    for i in range(n):
        running_max = max(running_max, arr[i])
        if arr[i] < running_max:
            right = i

    for i in range(n-1, -1, -1):
        running_min = min(running_min, arr[i])
        if arr[i] > running_min:
            left = i

    return left, right

if __name__ == '__main__':
    assert solution([3, 7, 5, 6, 9]) == (1, 3)
    assert solution([1,2,3]) == (0, 0)
