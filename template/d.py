#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
# import math, random
# import functools, itertools, collections, heapq, bisect
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


def solve_(mrr, total_vertices):
    if total_vertices == 2:
        return 2,2,[1,1]
    # your solution here

    # prune all leaves
    # break graph by leaf adjcaent
    # assign color by connected component

    # will be counted
    res = [-1 for _ in range(total_vertices)]

    g = defaultdict(set)
    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)
        # log(a, b)

    leaves = set()
    degree = defaultdict(int)
    for x in range(total_vertices):
        degree[x] = len(g[x])
        if len(g[x]) == 1:
            leaves.add(x)
            res[x] = 1

    breakers = set()
    for cur in leaves:
        for nex in g[cur]:
            breakers.add(nex)
            assert res[nex] != 1
            res[nex] = 0
        del g[cur]

    # log(leaves)
    # log(breakers)

    
    for start in range(total_vertices):
        if start in leaves or start in breakers:
            continue
        stack = [start]
        color = {}
        color[start] = 1
        while stack:
            cur = stack.pop()
            for nex in g[cur]:
                if nex in breakers:
                    continue
                # log(cur, nex)
                if nex in color:
                    continue
                color[nex] = 1-color[cur]
                stack.append(nex)

        color_one = 0
        color_zero = 0

        degree_one = 0
        degree_zero = 0

        for k,v in color.items():
            if v:
                color_one += 1
                degree_one += degree[k]
            else:
                color_zero += 1
                degree_zero += degree[k]

        if color_one > color_zero or (color_one == color_zero and degree_one < degree_zero):
            colored = 1
        else:
            colored = 0

        # log(color, colored)

        for k,v in color.items():
            if v == colored:
                res[k] = 1
            else:
                res[k] = 0

    assert -1 not in res
    assignement = [degree[i] if x == 1 else 1 for i,x in enumerate(res)]
    a = sum(degree[i] == x for i,x in enumerate(assignement))
    b = sum(assignement)

    return a,b,assignement


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    a,b,res = solve(mrr, k)  # include input here
    print(a,b)
    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)

