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
def shoelace_formula(xs,ys):
    # https://stackoverflow.com/a/30950874/5894029
    return sum(xs[i]*ys[i-1] - xs[i-1]*ys[i] for i in range(len(xs)))

def triangle_formula(xs,ys):
    # shoelace formula is 10x slower for some reason
    return (xs[0]*ys[1] + xs[1]*ys[2] + xs[2]*ys[0]) - (xs[0]*ys[2] + xs[1]*ys[0] + xs[2]*ys[1])

def get_polygon_area(xs,ys,take_abs=True,take_double=True):
    signed_area = shoelace_formula(xs,ys)  # switch to func=triangle_formula if needed for speed
    if not take_double:  # may cause precision issues idk
        signed_area = signed_area/2
    if take_abs:
        return abs(signed_area)
    return signed_area


def solve_(n, a):
    # your solution here

    if n > a+2:
        return []

    left_template = [(0,0), (1,1)]
    right_template = [(1,0), (1,2)]

    left = []
    right = []
    for i in range(n-1//4 + 1):
        if len(left) + len(right) == n-1:
            break
        x,y = 0,0
        right.append([x, y+i*2])
        if len(left) + len(right) == n-1:
            break
        x,y = -1,0
        left.append([x, y+i*2])
        if len(left) + len(right) == n-1:
            break
        x,y = 0,1
        left.append([x, y+i*2])
        if len(left) + len(right) == n-1:
            break
        x,y = 1,1
        right.append([x, y+i*2])


    if len(left) == len(right):
        base = right[-1][1]
        height = a-(n-2-1)
        left.append([0, base+height])
    elif len(left) > len(right):
        height = a-(n-2-1)
        right.append([height, left[-1][1]])
    elif len(right) > len(left):
        height = a-(n-2-1)
        left.append([-height, right[-1][1]])
    else:
        assert False


    # log(left)
    # log(right)

    res = left + right[::-1]

    minx = min(x for x,y in res)
    miny = min(y for x,y in res)

    res = [(x-minx, y-miny) for x,y in res]

    assert len(res) == n
    actual_area = get_polygon_area([x[0] for x in res], [x[1] for x in res])
    log(actual_area)
    assert actual_area == a
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
    n,a = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,a)  # include input here

    # print length if applicable
    # print(len(res))

    if not res:
        print("Case #{}: {}".format(case_num+1, "IMPOSSIBLE"))   # Google and Facebook - case number required
        continue

    print("Case #{}: {}".format(case_num+1, "POSSIBLE"))   # Google and Facebook - case number required
    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)
    print(res)
