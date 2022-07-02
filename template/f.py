#!/usr/bin/env python3
import sys
import heapq
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
# CHECK_OFFLINE_TEST = True
CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def dijkstra(list_of_indexes_and_costs, start):
    # shortest path with nonnegative edge costs
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    length = len(list_of_indexes_and_costs)
    visited = [False]*length
    weights = [MAXINT]*length
    path = [None]*length
    queue = []
    weights[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        g, u = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in list_of_indexes_and_costs[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    heapq.heappush(queue, (f, v))
    return path, weights


for case_num in range(int(input())):
    b, k, sx, sy, ex, ey = list(map(int,input().split()))
    # your solution here

    sx0 = (sx // b) * b
    sy0 = (sy // b) * b
    ex0 = (ex // b) * b
    ey0 = (ey // b) * b

    sx1 = sx0 + b
    sy1 = sy0 + b
    ex1 = ex0 + b
    ey1 = ey0 + b

    points = [
        (sx, sy, 1),

        (sx, sy0, 2),
        (sx, sy1, 2),

        (sx0, sy, 2),
        (sx1, sy, 2),

        (sx0, sy0, 3),
        (sx0, sy1, 3),
        (sx1, sy0, 3),
        (sx1, sy1, 3),

        (ex, ey, 4),

        (ex, ey0, 5),
        (ex, ey1, 5),

        (ex0, ey, 5),
        (ex1, ey, 5),

        (ex0, ey0, 6),
        (ex0, ey1, 6),
        (ex1, ey0, 6),
        (ex1, ey1, 6),
    ]

    allowed = set([
        (1,2),
        (2,3),
        (3,6),
        (6,5),
        (5,4),
        (2,5),
        (1,4),
    ])

    g = [[] for _ in range(18)]

    def diff(sx, sy, ex, ey):
        dist = (abs(sx-ex) + abs(sy-ey))
        if (sx%b == 0 and sy%b == 0 and ex%b == 0 and ey%b == 0):
            return dist
        if (sx == ex and sx%b == 0):
            return dist
        if (sy == ey and sy%b == 0):
            return dist
        return dist*k

    # count = 0
    for i,(ax,ay,p) in enumerate(points):
        if i == 9:
            continue
        for j,(bx,by,q) in enumerate(points):
            if (p,q) not in allowed:
                continue
            dist = diff(ax, ay, bx, by)
            g[i].append((j,dist))
            # count += 1
    # print(count)

    res = dijkstra(g, 0)[1][9]

    print(res)
