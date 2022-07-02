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


def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target, idxs=set()):
    # this operation is costly, recommend to parse to list_of_indexes_and_costs directly
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    d = map_from_node_to_nodes_and_costs

    if target not in d:  # destination may not have outgoing paths
        d[target] = []
    if source not in d:
        return MAXINT

    # assign indexes
    if idxs:
        idxs = {k:i for i,k in enumerate(idxs)}
    else:
        idxs = {k:i for i,k in enumerate(d.keys())}

    # populate list of indexes and costs
    list_of_indexes_and_costs = [[] for _ in range(len(idxs))]
    for e,vrr in d.items():
        for v,cost in vrr:
            list_of_indexes_and_costs[idxs[e]].append((idxs[v],cost))

    _, costs = dijkstra(list_of_indexes_and_costs, idxs[source])
    return costs[idxs[target]]



def solve_(b, k, sx, sy, ex, ey):
    # your solution here

    sx0 = (sx // b) * b
    sy0 = (sy // b) * b
    ex0 = (ex // b) * b
    ey0 = (ey // b) * b

    sx1 = sx0 + b
    sy1 = sy0 + b
    ex1 = ex0 + b
    ey1 = ey0 + b

    points = {
        (sx, sy),

        (sx, sy0),
        (sx, sy1),

        (sx0, sy),
        (sx1, sy),

        (sx0, sy0),
        (sx0, sy1),
        (sx1, sy0),
        (sx1, sy1),

        (ex, ey),

        (ex, ey0),
        (ex, ey1),

        (ex0, ey),
        (ex1, ey),

        (ex0, ey0),
        (ex0, ey1),
        (ex1, ey0),
        (ex1, ey1),
    }

    g = defaultdict(list)

    def diff(sx, sy, ex, ey):
        dist = (abs(sx-ex) + abs(ex-ey))
        if (sx%b == 0 and sy%b == 0 and ex%b == 0 and ey%b == 0):
            return dist
        if (sx == ex and sx%b == 0):
            return dist
        if (sy == ey and sy%b == 0):
            return dist
        return dist*k

    for (ax,ay) in points:
        for (bx, by) in points:
            g[ax,ay].append(((bx, by), diff(ax,ay,bx,by)))

    log(sx, sy, ex, ey)

    return dijkstra_with_preprocessing(g, (sx,sy), (ex,ey), points)


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
    b, k, sx, sy, ex, ey = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(b, k, sx, sy, ex, ey)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
