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


def solve_():
    # your solution here

    q,a0,c0 = list(map(int,input().split()))

    # find the highest non-bankrupt ancestor
    idx_to_cost = {0: c0}
    idx_to_amt = {0: a0}
    idx_to_parent = {0: c0}
    idx_to_ancestors = {0: []}

    idx = 0
    for _ in range(q):
        idx += 1
        lst = list(map(int,input().split()))
        if len(lst) == 4:
            p,a,c = lst[1:]
            idx_to_parent[idx] = p
            idx_to_amt[idx] = a
            idx_to_cost[idx] = c
            idx_to_ancestors[idx] = deque([x for x in idx_to_ancestors[p]])
            idx_to_ancestors[idx].append(p)
            if len(idx) >= 500:
                idx_to_ancestors[idx].popleft()
        else:
            v,w = lst[1:]
            series = [v]
            cur = v
            while idx_to_ancestors[v]:
                anc = idx_to_ancestors[v][0]
                if idx_to_amt[anc] == 0:
                    break
                cur = anc
                series.append(cur)
            # crawl from cur

            # considered_heaps = [v]
            # cur = v

            # while a > 0:
            #     all_heap = [(*idx_to_cost_heap[cur][0],v) for  v in considered_heaps


    return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve()  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)