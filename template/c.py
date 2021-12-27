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


def solve_(arr, k):
    # your solution here
    n = len(arr)

    sumarr = sum(arr)

    if sumarr <= k:
        return 0

    if len(arr) == 1:
        return arr[0] - k

    # arr.reverse()
    minres = sumarr - k
    # arr = arr

    # no reduction
    cursum = sumarr
    cnt = 0
    for x in arr[::-1]:
        cnt += 1
        cursum -= (x - arr[0])
        if cursum <= k:
            minres = min(minres, cnt)

    required_reduction = sumarr - k
    log(required_reduction)

    cursum = sumarr
    rightsum = arr[0]
    for i,x in enumerate(arr[1:][::-1], start=1):
        rightsum += x
        rightcount = i + 1
        target = (-required_reduction + rightsum) // rightcount
        valdrcrease = arr[0] - target
        res = valdrcrease + rightcount - 1
        minres = min(minres, res)

        log(rightsum, rightcount, target, valdrcrease, res)

    return minres



    # left_sum = 0
    # for i,x in enumerate(arr[1:]):
    #     right_count = n - i - 1
    #     right_allowance = k - left_sum
    #     right_target = right_allowance // right_count
    #     reduction = arr[0] - right_target

    #     res = reduction + right_count

    #     log(left_sum, right_count, right_allowance, right_target, reduction, res)

    #     # if not x <= right_target <= y:
    #     #     continue

    #     minres = min(minres, res)
    #     left_sum += x

    # return minres


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
    _,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
