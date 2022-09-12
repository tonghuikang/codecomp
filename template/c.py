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
        # log(*args)
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


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/geometry/convex_hull.py

def remove_middle(a, b, c):
    cross = (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
    dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
    return cross < 0 or cross == 0 and dot <= 0


def convex_hull(points):
    spoints = sorted(points)
    hull = []
    for p in spoints + spoints[::-1]:
        while len(hull) >= 2 and remove_middle(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull


LARGE = 10**14

def solve_(n,k,d,nrr):
    # your solution here
    k = k
    d = d**2

    start = nrr[0]
    end = nrr[-1]

    arr = convex_hull(nrr)
    point_to_idx = {(x,y):i for i,(x,y) in enumerate(arr)}
    m = len(arr)

    # log(nrr)
    # log(arr)

    start_idx = point_to_idx[tuple(start)]
    end_idx = point_to_idx[tuple(end)]

    log("point_size", len(arr))

    def calc_dist(x1,y1,x2,y2):
        return (x1-x2)**2 + (y1-y2)**2

    def scoring(x1,y1,x2,y2):
        dist = calc_dist(x1,y1,x2,y2)
        if dist > d:
            return MAXINT
        else:
            return max(k, dist)

    dp = [LARGE for _ in range(m)]
    dp[start_idx] = 0
    visited = set()

    while len(visited) < m:
        # log(visited)
        x,i = LARGE+1, -1
        for q in range(m):
            if q in visited:
                continue
            if dp[q] < x:
                x = dp[i]
                i = q
        log(i)
        x1,y1 = arr[i]
        visited.add(i)

        for j in range(m):
            if j in visited:
                continue
            x2,y2 = arr[j]
            val = dp[i] + scoring(x1,y1,x2,y2)
            dp[j] = min(val, dp[j])

    return dp[end_idx]



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
    n,k,d = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    nrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    log(n,k,d)

    res = solve(n,k,d,nrr)  # include input here

    if res >= LARGE:
        res = -1

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)


# with open("lemonade_life_input.txt") as f:
#     srr = f.readlines()

# import matplotlib.pyplot as plt
# mrr = [list(map(int, row.strip().split())) for row in srr[2:2+7818]]
# mrr.sort()
# plt.scatter(*zip(*mrr))
# plt.xlim(1,2000)
# plt.ylim(497354+100000,497354-100000)