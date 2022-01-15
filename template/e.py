#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

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

LARGE = 10**18 + 10

def solve_(mrr,xrr,n,m,k):
    # your solution

    entry_points_all_floors = [[] for _ in range(n+1)]
    entry_points_all_floors[0].append([0,0])  # loc, cost

    exit_points_all_floors = defaultdict(list)
    for a,b,c,d,e in mrr:
        exit_points_all_floors[a].append((a,b,c,d,e))

    exit_points_all_floors[n-1].append((n-1,m-1,n,0,0))

    # for i in exit_points_all_floors:
    #     exit_points_all_floors[i].sort()

    for i in range(n):
        xcost = xrr[i]
        # if i not in exit_points_all_floors:
        #     continue

        entry_points = entry_points_all_floors[i]
        exit_points = exit_points_all_floors[i]

        # log("floor")
        # log(i)
        # log(entry_points)
        # log(exit_points)
        # log()

        loc_and_cost = []
        for loc,cost in entry_points:
            loc_and_cost.append([loc, cost])

        for a,b,c,d,e in exit_points:
            loc_and_cost.append([b, LARGE])

        loc_and_cost.sort()
        min_costs = [LARGE]*len(loc_and_cost)

        loc_to_idx = {}
        for i,(loc,cost) in enumerate(loc_and_cost):
            loc_to_idx[loc] = i

        # propagate left right
        min_intercept = LARGE
        for i,(loc,cost) in enumerate(loc_and_cost):
            if cost == LARGE:
                if min_intercept == LARGE:
                    continue
                val = min_intercept + loc*xcost
                min_costs[i] = min(min_costs[i], val)
            else:
                intercept = cost - loc*xcost
                min_intercept = min(min_intercept, intercept)

        min_intercept = LARGE
        for i,(loc,cost) in enumerate(loc_and_cost[::-1]):
            if cost == LARGE:
                if min_intercept == LARGE:
                    continue
                val = min_intercept - loc*xcost
                min_costs[~i] = min(min_costs[~i], val)
            else:
                intercept = cost + loc*xcost
                min_intercept = min(min_intercept, intercept)

        for a,b,c,d,e in exit_points:
            idx = loc_to_idx[b]
            entry_points_all_floors[c].append([d,-e+min_costs[idx]])

        # log(min_costs)
        # log(loc_and_cost)
        # log()


    if entry_points_all_floors[-1][-1][-1] > 10**17:
        return "NO ESCAPE"

    return entry_points_all_floors[-1][-1][-1]


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,m,k = list(map(int,input().split()))
    xrr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)
    mrr = [(a-1,b-1,c-1,d-1,e) for a,b,c,d,e in mrr]

    res = solve(mrr,xrr,n,m,k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
