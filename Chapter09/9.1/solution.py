"""
compute running median
"""

import heapq

def balance(bottom_half, top_half):
    if len(bottom_half) > len(top_half):
        promote = -1*heapq.heappop(bottom_half)
        heapq.heappush(top_half, promote)
    if len(bottom_half) < len(top_half):
        demote = heapq.heappop(top_half)
        heapq.heappush(bottom_half, demote)

def add(num, bottom_half, top_half):
    if not bottom_half or -1*bottom_half[0] > num:
        heapq.heappush(bottom_half, -num)
    else:
        heapq.heappush(top_half, num)

    if abs(len(bottom_half) - len(top_half)) > 1:
        balance(bottom_half, top_half)

def extract(bottom_half, top_half):
    if len(bottom_half) - len(top_half) == 1:
        return -1*bottom_half[0]
    if len(top_half)-len(bottom_half) == 1:
        return top_half[0]
    return (-1*bottom_half[0] + top_half[0])/2

def running_median(stream):
    bottom_half, top_half, out = [], [], []
    for num in stream:
        add(num, bottom_half, top_half)
        median = extract(bottom_half, top_half)
        out.append(median)
    return out

if __name__ == '__main__':
    print(running_median([4,6,9,3,1,0,3,4,6,6,2,4]))
"""
4
b = [4]
t = [] -> 4
6
b = [4]
t = [6] -> 5
9
b = [4],
t = [6, 9] -> 6
3
b = [4, 3]
t = [6, 9] -> 5
1
b = [4, 3, 1]
t = [6, 9] -> 4
0
b = [4, 3, 1, 0]
t = [6, 9]
b = [3, 1, 0]
t = [4, 6, 9] -> 3.5
"""