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

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
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

# recusion template that does not use recursion

# def dfs(start, g, entry_operation, exit_operation):
#     # https://codeforces.com/contest/1646/submission/148435078
#     # https://codeforces.com/contest/1656/submission/150799881
#     entered = set([start])
#     exiting = set()
#     stack = [start]
#     prev = {}

#     null_pointer = "NULL"
#     prev[start] = null_pointer

#     while stack:
#         cur = stack[-1]

#         if cur not in exiting:
#             for nex in g[cur]:
#                 if nex in entered:
#                     continue

#                 entry_operation(prev[cur], cur, nex)

#                 entered.add(nex)
#                 stack.append(nex)
#                 prev[nex] = cur
#             exiting.add(cur)

#         else:
#             stack.pop()
#             exit_operation(prev[cur], cur)


def solve_(mrr, n, k):
    del k
    # your solution here

    g = defaultdict(list)
    for a,b in mrr:
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    
    pos = [0 for _ in range(n)]
    res1 = []
    stack = deque([0])
    visited = set(stack)
    while stack:
        # log(stack)
        cur = stack[-1]
        if pos[cur] == len(g[cur]):
            stack.pop()
            continue
        nex = g[cur][pos[cur]]
        pos[cur] += 1
        if nex in visited:
            continue
        visited.add(nex)
        res1.append([cur,nex])
        stack.append(nex)


    res2 = []
    stack = deque([0])
    visited = set(stack)
    while stack:
        cur = stack.popleft()
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
            res2.append([cur, nex])

    # log(len(res1))
    # log(len(res2))

    return res1, res2


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
    n,k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res1, res2 = solve(mrr, n, k)  # include input here

    log(res1)
    log(res2)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res1 = "\n".join("{} {}".format(row[0]+1, row[1]+1) for row in res1)
    res2 = "\n".join("{} {}".format(row[0]+1, row[1]+1) for row in res2)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res1)
    # log()
    print(res2)
