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


def solve_(srr, mrr):
    # your solution here

    if len(srr) < 3:
        return [0 for _ in mrr]


    srr = list(srr)
    cnt = 0

    for a,b,c in zip(srr, srr[1:], srr[2:]):
        if a == "a" and b == "b" and c == "c":
            cnt += 1

    res = []

    for pos, x in mrr:
        # log()

        # log(pos,x)

        left = max(0, pos-2)
        right = pos+3
        for a,b,c in zip(srr[left:right], srr[left+1:right+1], srr[left+2:right+2]):
            # log(a,b,c)
            if a == "a" and b == "b" and c == "c":
                cnt -= 1

        srr[pos] = x

        left = max(0, pos-2)
        right = pos+3
        for a,b,c in zip(srr[left:right], srr[left+1:right+1], srr[left+2:right+2]):
            if a == "a" and b == "b" and c == "c":
                cnt += 1

        # log(srr)
        res.append(cnt)

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    n,q = list(map(int,input().split()))

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    arr = read_strings(q)  # and return as a list of str
    # mrr = read_matrix(q)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)
    mrr = []
    for ar in arr:
        a,b = ar.split()
        mrr.append((int(a)-1, b))

    res = solve(srr, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
