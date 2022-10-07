#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
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
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
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
    return weights


def solve_(mrr, n, m):
    # your solution here

    g2 = [[] for _ in range(n)]
    for a,b,w in mrr:
        g2[a].append((b,w))
        g2[b].append((a,w))

    minres = dijkstra(g2, 0)[-1]

    g = [[] for _ in range(n)]
    for a,b,w in mrr:
        g[a].append((b,1))
        g[b].append((a,1))

    from_1 = dijkstra(g, 0)
    from_n = dijkstra(g, n-1)

    log(from_1)
    log(from_n)

    d = from_1[-1]
    for a,b,w in mrr:
        dist = min(from_1[a], from_1[b]) + min(from_n[a], from_n[b])

        if abs(from_1[a] - from_n[a]) == d and abs(from_1[b] - from_n[b]) == d:
            dist += 1
        res = (dist+1)*w
        minres = min(minres, res)

    return minres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    mrr = [(x-1,y-1,z) for x,y,z in mrr]
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
