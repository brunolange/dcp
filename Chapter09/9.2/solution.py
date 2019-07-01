"""
website similarity

list k most similar websites based on their users
"""

from collections import defaultdict
import heapq

def sim(users, a, b):
    return len(users[a] & users[b])/len(users[a] | users[b])

def similarity(db, k=3):
    users = defaultdict(set)
    for site, user in db:
        users[site].add(user)

    pool = []
    sites = list(users.keys())
    for i in range(len(sites)-1):
        for j in range(i+1, len(sites)):
            score = sim(users, sites[i], sites[j])
            heapq.heappush(pool, (score, (sites[i], sites[j])))
            if len(pool) > k:
                heapq.heappop(pool)

    return pool
    # return [listing[1] for listing in pool]

if __name__ == '__main__':
    print(similarity([
        ('google.com', 1), ('google.com', 3), ('google.com', 5),
        ('pets', 1), ('pets', 2), ('pets', 6),
        ('yahoo', 2), ('yahoo', 3), ('yahoo', 4), ('yahoo', 5),
        ('wiki', 4), ('wiki', 5), ('wiki', 6),
        ('bing', 1), ('bing', 3), ('bing', 5), ('bing', 6),
    ], k=3))
