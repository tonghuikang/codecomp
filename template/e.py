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


def solve_(arr, brr, n):
    # your solution here

    locations = [arr[-1] - x for x in arr]
    locations.reverse()
    log(locations)

    p1 = arr[-1]

    p2 = locations[-1] - brr[-1]
    log(p2)
    brr_candidate = [abs(x - p2) for x in locations]
    if brr == sorted(brr_candidate):
        return locations, p1, p2

    p2 = brr[-1]
    log(p2)
    brr_candidate = [abs(x - p2) for x in locations]
    if brr == sorted(brr_candidate):
        return locations, p1, p2

    return [], -1, -1


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
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    arr.sort()
    brr.sort()

    swap = False
    # if arr[-1] < brr[-1]:
    #     swap = True
    #     arr, brr = brr, arr
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    locations, p1, p2 = solve(arr, brr, n)  # include input here
    if not locations:
        locations, p2, p1 = solve(brr, arr, n)  # include input here

    if locations:
        shift = -min(0, p1, p2)
        locations = [x + shift for x in locations]
        p1 += shift
        p2 += shift

        # if swap:
        #     p1, p2 = p2, p1
        #     arr, brr = brr, arr

        arr_check = sorted(abs(x - p1) for x in locations)
        brr_check = sorted(abs(x - p2) for x in locations)
        assert arr_check == arr
        assert brr_check == brr

    if not locations:
        print(no)
        continue

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(yes)
    print(" ".join(str(x) for x in locations))
    print(p1, p2)
