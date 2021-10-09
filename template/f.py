#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import heapq
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = 10**16

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
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
    # short path with nonnegative edge costs
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
        visited[u] = True
        for v, w in list_of_indexes_and_costs[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    heapq.heappush(queue, (f, v))
    return path, weights


# def solve_():
# your solution here
k = int(input())

mrr = read_matrix(k-1)  # and return as a list of list of int
# mrr = minus_one_matrix(mrr)
lst = list(map(int,input().split()))

# log(mrr)
# log(lst)

g = [[] for _ in range(4*10**5 + 10)]
for a,b,c in mrr:
    g[a].append((b,c))
    g[b].append((a,c))

offset = 2*10**5
for i,x in enumerate(lst, start=1):
    g[i].append((i+offset,x))
    g[i+offset].append((i,x))

del mrr

res = [0]*(4*10**5 + 10)

path, weights = dijkstra(g, start=1)

e1 = 0
tmp = 0
for i,w in enumerate(weights):
    if w != MAXINT:
        if w > tmp:
            tmp = w
            e1 = i

# log("end1", e1)
# log("weights", weights[:10])
# log("weights", weights[2*10**5:2*10**5 + 10])

path, weights = dijkstra(g, start=e1)

res = [max(a,b) for a,b in zip(res, weights)]

e2 = 0
tmp = 0
for i,w in enumerate(weights):
    if w != MAXINT:
        if w > tmp:
            tmp = w
            e2 = i

# log("end2", e2)
# log("weights", weights[:10])
# log("weights", weights[2*10**5:2*10**5 + 10])

path, weights = dijkstra(g, start=e2)

# log("weights", weights[:10])
# log("weights", weights[2*10**5:2*10**5 + 10])

res = [max(a,b) for a,b in zip(res, weights)]

res = res[2*10**5+1:]

res = [a-b for a,b in zip(res, lst)][:k]
res = "\n".join(str(x) for x in res)

print(res)