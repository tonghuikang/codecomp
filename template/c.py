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


def solve_(arr):
    # your solution here

    # target height = maxheight or maxheight+1
    maxheight = max(arr)

    # target maxheight
    diffs = [maxheight-x for x in arr]
    maxtwos = sum([x // 2 for x in diffs])
    minones = sum([x % 2 for x in diffs])

    # log(diffs)
    # log(maxtwos, minones)
    # res =

    minres = max(maxtwos, minones) * 2

    if minones > maxtwos:
        minres = min(minres, minones * 2 - 1)
    elif minones == maxtwos:
        minres = min(minres, minones + maxtwos)
    else:
        minres = min(minres, maxtwos * 2)

    d2 = max(0, (maxtwos - minones - 2) // 2)
    minones += d2*2
    maxtwos -= d2

    # log(minones, maxtwos)

    if minones > maxtwos:
        minres = min(minres, minones * 2 - 1)
    elif minones == maxtwos:
        minres = min(minres, minones + maxtwos)
    else:
        minres = min(minres, maxtwos * 2)
    
    for _ in range(3):

        d2 = 1
        minones += d2*2
        maxtwos -= d2

        # log(minones, maxtwos)

        if minones > maxtwos:
            minres = min(minres, minones * 2 - 1)
        elif minones == maxtwos:
            minres = min(minres, minones + maxtwos)
        else:
            minres = min(minres, maxtwos * 2)

    return minres

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
