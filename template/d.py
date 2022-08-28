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


def solve_(mrr, qrr, n, m, q):
    # your solution here

    g = [{} for _ in range(n)]
    
    for a,b,c in mrr:
        g[a][b] = c
        g[b][a] = c

    cache = {}
    @functools.lru_cache(maxsize=3*10**5)
    def call(x,y):
        if (x,y) in cache:
            return cache[x,y]
        if len(g[x]) > len(g[y]):
            x,y = y,x
        res = 0
        if y in g[x]:
            res += 2*g[x][y]
        # log(len(g[x]), x, y)
        for k,v1 in g[x].items():
            if k in g[y]:
                res += min(v1, g[y][k])
        cache[x,y] = res
        return res

    allres = []
    for x,y in qrr:
        res = call(x,y)
        allres.append(res)

    return allres


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
    n,m,q = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)
    log(case_num,n,m,q)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    mrr = [(a-1, b-1, c) for a,b,c in mrr]
    qrr = read_matrix(q)  # and return as a list of list of int
    qrr = minus_one_matrix(qrr)

    res = solve(mrr, qrr, n, m, q)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
