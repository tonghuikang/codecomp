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


def solve_(r1,c1,r2,c2,r3,c3,x,y,n):
    # your solution here

    # if (x,y) in [(r1,c1),(r2,c2),(r3,c3)]:
    #     return yes

    arr = sorted([(r1,c1),(r2,c2),(r3,c3)])
    if arr == sorted([(1,1),(1,2),(2,1)]):
        if x != 1 and y != 1:
            return no
    if arr == sorted([(n-1,1),(n,1),(n,2)]):
        if x != n and y != 1:
            return no
    if arr == sorted([(1,n-1),(1,n),(2,n)]):
        if x != 1 and y != n:
            return no
    if arr == sorted([(n-1,n),(n,n-1),(n,n)]):
        if x != n and y != n:
            return no

    seen = set()
    seen.add((r1%2, c1%2))
    seen.add((r2%2, c2%2))
    seen.add((r3%2, c3%2))

    log(seen)
    log((x%2, y%2))

    if (x%2, y%2) in seen:
        return yes

    return no


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    r1,c1,r2,c2,r3,c3 = list(map(int,input().split()))
    x,y = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(r1,c1,r2,c2,r3,c3,x,y,n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
