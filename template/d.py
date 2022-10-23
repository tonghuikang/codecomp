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

LARGE = 10**18


def solve_(n,m,p,q,mrr):
    # your solution here

    edges = defaultdict(list)

    for i in range(n-1):
        for j in range(m-1):
            # check at least three spaces
            if (mrr[i][j] == "#") + (mrr[i+1][j+1] == "#") + (mrr[i+1][j] == "#") + (mrr[i][j+1] == "#") > 1:
                continue
            if mrr[i][j] != "#" or mrr[i+1][j+1] != "#":
                edges[i+1,j].append(((i,j+1), p))
                edges[i,j+1].append(((i+1,j), p))
            if mrr[i+1][j] != "#" or mrr[i][j+1] != "#":
                edges[i,j].append(((i+1,j+1), p))
                edges[i+1,j+1].append(((i,j), p))
    
    for i in range(n):
        for j in range(m-2):
            if (mrr[i][j] == "#") + (mrr[i][j+1] == "#") + (mrr[i][j+2] == "#") >= 1:
                continue
            edges[i,j].append(((i,j+2), q))
            edges[i,j+2].append(((i,j), q))

    for i in range(n-2):
        for j in range(m):
            if (mrr[i][j] == "#") + (mrr[i+1][j] == "#") + (mrr[i+2][j] == "#") >= 1:
                continue
            edges[i,j].append(((i+2,j), q))
            edges[i+2,j].append(((i,j), q))

    log(edges)

    costmap = {}
    for i in range(n):
        for j in range(m):
            costmap[i,j] = LARGE

    queue = []
    for i in range(n):
        for j in range(m):
            if mrr[i][j] == ".":
                costmap[i,j] = 0
                queue.append((0,(i,j)))
    
    visited = set()
    while queue:
        cost,(i,j) = heapq.heappop(queue)
        if (i,j) in visited:
            continue
        for nex,addn in edges[i,j]:
            if nex in visited:
                continue
            new_cost = cost+addn
            if new_cost >= costmap[nex]:
                continue
            costmap[nex] = new_cost
            heapq.heappush(queue, (new_cost,nex))

    for i in range(n):
        for j in range(m):
            if mrr[i][j] == "#":
                costmap[i,j] = LARGE

    mincost = LARGE
    for i in range(n-1):
        for j in range(m):
            val = costmap[i,j] + costmap[i+1,j]
            log(val, i, j, i+1, j)
            mincost = min(mincost, val)

    for i in range(n):
        for j in range(m-1):
            val = costmap[i,j] + costmap[i,j+1]
            log(val, i, j, i, j+1)
            mincost = min(mincost, val)
    
    if mincost >= LARGE:
        mincost = -1

    log(costmap)

    return mincost



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    p,q = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    mrr = read_strings(n)  # and return as a list of str
    # mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,p,q,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
