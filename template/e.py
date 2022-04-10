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


def solve_(arr, maxi, mini):
    # your solution here


    if maxi == mini:
        arr.append(-1)
        # count differently
        cur = 0
        res = 0
        for x in arr:
            if x == maxi:
                cur += 1
            else:
                res += (cur)*(cur+1) // 2
                cur = 0
        return res

    res = [[]]
    for i,x in enumerate(arr):
        if x == maxi:
            res[-1].append(1)
        elif x == mini:
            res[-1].append(2)
        elif x < mini or x > maxi:
            res.append([])
        else:
            res[-1].append(0)

    log(res)

    allval = 0

    for segment in res:
        if not segment:
            continue

        val = 0
        seglen = len(segment)
        val += (seglen)*(seglen+1) // 2

        pos1 = [-1]
        pos2 = [-1]
        pos12 = [-1]

        for i,x in enumerate(segment):
            if x == 1:
                pos1.append(i)
            if x == 2:
                pos2.append(i)
            if x == 1 or x == 2:
                pos12.append(i)

        pos1.append(seglen)
        pos2.append(seglen)
        pos12.append(seglen)

        for a,b in zip(pos1, pos1[1:]):
            diff = b-a
            val -= (diff)*(diff-1) // 2

        for a,b in zip(pos2, pos2[1:]):
            diff = b-a
            val -= (diff)*(diff-1) // 2

        for a,b in zip(pos12, pos12[1:]):
            diff = b-a
            val += (diff)*(diff-1) // 2

        allval += val

    return allval


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
    _,  maxi, mini = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, maxi, mini)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
