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


def binary_search(func_,       # condition function
                  first=True,  # else last
                  target=True, # else False
                  left=0, right=2**31-1) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first^target:
            return not func_(val)
        return func_(val)

    ctr = 80
    smallest_true = right
    while ctr:
        mid = left + (right-left)/2
        if func(mid):
            right = mid
            smallest_true = mid
        else:
            left = mid + 10**-16
        ctr -= 1
        log(mid)
    return smallest_true
    return mid


def ceiling_division(numer, denom):
    return -((-numer)//denom)

def solve_(arr, k, n, m):
    assert sum(arr) == n
    # your solution here
    arr = [x/n for x in arr]
    log(arr)
    
    # binary search on allowance
    def is_allowance_feasible(allowance):
        all_lower = 0
        all_upper = 0
        for ratio in arr:
            lower = (ratio - allowance)*m
            upper = (ratio + allowance)*m
            lower = ceiling_division(lower, 1)
            upper = upper//1
            if upper < lower:
                return False
            all_lower += lower
            all_upper += upper

        return all_lower <= m <= all_upper

    best_allowance = binary_search(is_allowance_feasible, left=0, right=2)
    log(is_allowance_feasible(best_allowance), best_allowance)
    # best_allowance += 10**-15

    lowers = []
    uppers = []
    diffs = []
    allowance = best_allowance
    for ratio in arr:
        lower = (ratio - allowance)*m
        upper = (ratio + allowance)*m
        lower = int(ceiling_division(lower, 1))
        upper = int(upper//1)
        lowers.append(lower)
        uppers.append(upper)
        diffs.append(upper-lower)
        assert 0 <= upper-lower <= 1
    
    lowers.reverse()
    uppers.reverse()
    diffs.reverse()

    res = []
    remaining_diff = m - sum(lowers)
    for lower, upper, diff in zip(lowers, uppers, diffs):
        if remaining_diff and upper > lower:
            remaining_diff -= 1
            res.append(upper)
        else:
            res.append(lower)

    assert sum(res) == m
    res.reverse()
    return res

   
    
for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    k,n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, k, n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)