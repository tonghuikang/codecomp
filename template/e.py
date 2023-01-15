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


def solve_(n,mrr):
    # your solution here

    rects = []   # left, right, 1,2,3, idx

    for idx,(u,l,d,r) in enumerate(mrr):
        if u == d == 1:
            rects.append([l,r,1,idx])
        elif u == d == 2:
            rects.append([l,r,2,idx])
        elif u == 1 and d == 2:
            rects.append([l,r,3,idx])
        else:
            log(u,l,d,r)
            assert False

    rects.sort()

    curtop = -1
    curbot = -1
    curtopidx = -1
    curbotidx = -1

    # end current rectangle if incoming rectangle ends later
    
    for l,r,ty,idx in rects:
        log(l,r,ty,idx)
        log(mrr)

        if ty == 3:
            if curtop >= r and curbot >= r:
                mrr[idx] = [0,0,0,0]
                continue
            elif curbot >= r:
                mrr[idx][0] = 1
                mrr[idx][2] = 1
                ty = 1
            elif curtop >= r:
                mrr[idx][0] = 2
                mrr[idx][2] = 2
                ty = 2
            else:
                log(l,r,ty,idx)
                if curtop >= l and curtopidx >= 0:
                    mrr[curtopidx][3] = l
                if curbot >= l and curbotidx >= 0:
                    mrr[curbotidx][3] = l
                curtop = r
                curbot = r
                curtopidx = idx
                curbotidx = idx
                continue
    
        if ty == 1:
            if curtop >= r:
                mrr[idx] = [0,0,0,0]
                continue
            if curtop >= l and curtopidx >= 0:
                mrr[idx][3] = l
            curtop = r
            curtopidx = idx
            continue
        
        if ty == 2:
            if curbot >= r:
                mrr[idx] = [0,0,0,0]
                continue
            if curbot >= l and curbotidx >= 0:
                mrr[idx][3] = l
            curbot = r
            curbotidx = idx
            continue

    res = 0
    ret = []
    for u,l,d,r in mrr:
        if u == 0:
            ret.append([0,0,0,0])
            continue
        if r <= l:
            ret.append([0,0,0,0])
            continue
        ret.append((u,d,l,r-1))
        res += (d-u+1) * (r-l)
    print(res)

    return mrr


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

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
    mrr = read_matrix(n)  # and return as a list of list of int
    mrr = [[u,l,d,r+1] for u,l,d,r in mrr]
    # mrr = minus_one_matrix(mrr)

    res = solve(n,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
