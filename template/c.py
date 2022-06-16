#!/usr/bin/env python3
import sys
import heapq
from collections import defaultdict
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
    return path, weights


MAXINT = 10**18

if True:
    n,k = list(map(int,input().split()))
    mrr = read_matrix(k)
    # your solution here

    # the cost is the outdegree except those heading to the pool

    pool = set([n])
    visited = [False]*(n+1)
    weights = [MAXINT]*(n+1)
    outdegree = [0]*(n+1)

    # g = defaultdict(set)
    h = defaultdict(list)
    for a,b in mrr:
        if a == n:
            continue
        # g[a].add(b)
        h[b].append(a)
        outdegree[a] += 1

    for a,b in [[0,1]]:
        # g[a].add(b)
        h[b].append(a)
        outdegree[a] += 1
    
    weights[n] = 0

    # log(outdegree)
    queue = [(0, n)]
    
    while queue:
        x, u = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True

        for v in h[u]:
            outdegree[v] -= 1
            if not visited[v]:
                f = x + outdegree[v] + 1
                if f < weights[v]:
                    weights[v] = f
                    heapq.heappush(queue, (f, v))

    # log(weights)

    print(weights[0] - 1)
