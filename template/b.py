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

mapp = {"w": 0, "i": 1, "n": 2}
wrr = "win"

def solve_(mrr, k):
    # direct exchange always possible?
    mrr = [sorted(mapp[x] for x in xx) for xx in mrr]

    arr = []

    for i,x in enumerate(mrr):
        if x == [0,1,2]:
            continue
        if x == [0,0,0]:
            arr.append((i,0,1))
            arr.append((i,0,2))
            continue
        if x == [1,1,1]:
            arr.append((i,1,0))
            arr.append((i,1,2))
            continue
        if x == [2,2,2]:
            arr.append((i,2,0))
            arr.append((i,2,1))
            continue
        extra = -1
        need = -1
        for q in range(3):
            if x.count(q) == 2:
                extra = q
            if x.count(q) == 0:
                need = q
        arr.append((i,extra,need))

    # log(arr)

    d = defaultdict(list)

    for i,a,b in arr:
        d[a,b].append(i)

    res = []

    for a in range(3):
        for b in range(a+1,3):
            while d[a,b] and d[b,a]:
                x = d[a,b].pop()
                y = d[b,a].pop()
                res.append((x+1,wrr[a],y+1,wrr[b]))

    while d[2,0] and d[0,1]:
        x = d[2,0].pop()
        y = d[0,1].pop()
        res.append((x+1,wrr[2],y+1,wrr[0]))
        d[2,1].append(y)

    while d[0,2] and d[1,0]:
        x = d[0,2].pop()
        y = d[1,0].pop()
        res.append((x+1,wrr[0],y+1,wrr[2]))
        d[1,2].append(y)

    for a in range(3):
        for b in range(a+1,3):
            while d[a,b] and d[b,a]:
                x = d[a,b].pop()
                y = d[b,a].pop()
                res.append((x+1,wrr[a],y+1,wrr[b]))

    # for x in list(d.keys()):
    #     if d[x] == []:
    #         del d[x]

    # log(d)
    
    return res


import random
for _ in range(10):
    m = random.randint(1,100)
    srr = ["w"]*m + ["i"]*m + ["n"]*m
    random.shuffle(srr)
    inp = []
    for _ in range(m):
        inp.append([srr.pop(), srr.pop(), srr.pop()])
    solve(inp, m)
    


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
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
    mrr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, k)  # include input here
    print(len(res))

    if len(res) == 0:
        continue

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
