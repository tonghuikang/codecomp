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


def solve_(arr, brr):
    # your solution here

    log(sorted(arr))
    log(sorted(brr))

    a0 = arr[0]
    b0 = brr[0]
    curres = arr[0] + brr[0]
    cells = []
    # cells = [(arr[0] + brr[0], 0, 0)]
    
    arr = [(x,i) for i,x in enumerate(arr[1:])]
    brr = [(x,i) for i,x in enumerate(brr[1:])]

    arr.sort()
    brr.sort()

    if len(arr) >= 10:
        arr = arr[2:] + arr[-2:]

    if len(brr) >= 10:
        brr = brr[2:] + brr[-2:]

    for x,i in arr:
        for y,j in brr:
            cells.append((x+y,i,j))
    
    for x,i in arr:
        y,j = [b0, 0]
        cells.append((x+y,i,j))        

    for y,j in brr:
        x,i = [a0, 0]
        cells.append((x+y,i,j))        



    log(cells)

    res = 0
    curmin = True
    curval = curres
    curcell = (curres, 0, 0)

    while cells:
        log(cells)
        _, ci, cj = curcell
        if curmin:
            mincell = curcell
            for cell in cells:
                z,i,j = cell
                if i == ci or j == cj:
                    if mincell[0] > cell[0]:
                        mincell = cell
            if mincell == curcell:
                return curcell[0]
            cells.remove(mincell)
            curcell = mincell
        else:
            maxcell = curcell
            for cell in cells:
                z,i,j = cell
                if i == ci or j == cj:
                    if maxcell[0] < cell[0]:
                        maxcell = cell
            if maxcell == curcell:
                return curcell[0]
            cells.remove(maxcell)
            curcell = maxcell
        
        curmin = not curmin

    return curcell[0]
            






    # second largest, second smallest
    # arr2 = sorted(arr)
    # brr2 = sorted(brr)

    # log(arr)
    # log(brr)

    # res = 0

    # if len(arr2) == 1:
    #     res += arr2[0]
    # else:
    #     res += arr2[1]

    # if len(brr2) == 1:
    #     res += brr2[0]
    # else:
    #     res += brr2[1]

    return res


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
    a,b = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, brr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
