from collections import deque
from random import shuffle

def max_window(arr, k):
    dq = deque()
    out = []
    for i in range(len(arr)):
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(arr[dq[0]])
    return out

if __name__ == '__main__':
    print(max_window([9, 4, 6, 3, 1, 2, 8, 7, 5], 4))
    print(max_window([10, 5, 2, 7, 8, 7], 3))
    print(max_window([10, 5, 2, 7, 8, 7], 4))
    print(max_window(list(range(10)), 3))
    print(max_window(list(range(9, -1, -1)), 3))

"""
i   = [0, 1, 2, 3, 4, 5, 6, 7, 8]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
k = 4

q = [0, 1, 2, 3]
out = arr[q[0]] = 9

i = 4; i - q[0] = 4 >= k -> q.popleft()
q -> [1, 2, 3]
arr[i] < q[arr[-1]] -> q.append(i)
q = [1, 2, 3, 4]

"""