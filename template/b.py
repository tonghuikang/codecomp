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

def ceiling_division(numer, denom):
    return -((-numer)//denom)



def solve_(h,w,k,x1,y1,x2,y2):
    # your solution here

    dx = abs(x1-x2)
    dy = abs(y1-y2)

    cx = ceiling_division(dx, k)
    cy = ceiling_division(dy, k)

    if x1 == 0 or y1 == 0:
        if x1 == 0 and y1 == 0:
            res = cy * dx + dx * dy
        elif x1 == 0:
            res = cy * dx + dx * dy + cx
        elif y1 == 0:
            res = cy * (dx+1) + dx * dy
        else:
            assert False

        if x2 == h:
            res -= cy
        if y2 == w:
            res -= dx
        return res

    res = cx + cy * (dx+1) + dx * dy

    minadd = min(
        ceiling_division(x1 + dx, k) - cx,
        ceiling_division(h - x1 + dx, k) - cx,
        ceiling_division(y1 + dy, k) - cy,
        ceiling_division(w - y1 + dy, k) - cy,
    )
    assert minadd >= 0

    return res + minadd


def solve_ref(h,w,k,x1,y1,x2,y2):
    # your solution here
    
    res = (abs(x1 - x2) + 1 + 1) * (abs(y1 - y2) + 1) + (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1 + 1)
    log(res)

    res += min(
        x1-1, y1-1, h-x2, w-y2
    )

    if x1 == 1:
        res -= (abs(y1 - y2) + 1)
    if y1 == 1:
        res -= (abs(x1 - x2) + 1)
    if x2 == h:
        res -= (abs(y1 - y2) + 1)
    if y2 == w:
        res -= (abs(x1 - x2) + 1)

    return res


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
    h,w,k = list(map(int,input().split()))
    x1,y1,x2,y2 = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res_ref = solve_ref(h,w,k,x1,y1,x2,y2)

    x1 -= 1
    # x2 -= 1
    y1 -= 1
    # y2 -= 1

    res1 = solve(h,w,k,x1,y1,x2,y2)  # include input here
    res2 = solve(w,h,k,y1,x1,y2,x2)  # include input here
    x1,x2 = h-x2, h-x1
    res3 = solve(h,w,k,x1,y1,x2,y2)  # include input here
    res4 = solve(w,h,k,y1,x1,y2,x2)  # include input here
    y1,y2 = w-y2, w-y1
    res5 = solve(h,w,k,x1,y1,x2,y2)  # include input here
    res6 = solve(w,h,k,y1,x1,y2,x2)  # include input here
    x1,x2 = h-x2, h-x1
    res7 = solve(h,w,k,x1,y1,x2,y2)  # include input here
    res8 = solve(w,h,k,y1,x1,y2,x2)  # include input here

    res = min(res1, res2, res3, res4, res5, res6, res7, res8)
    # print length if applicable
    # print(len(res))

    if k == 1:
        log("ref", res_ref)
        log("val", res, res1, res2, res3, res4, res5, res6, res7, res8)
        assert res == res_ref

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)