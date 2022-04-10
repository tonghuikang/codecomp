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

def binary_search(func_,       # condition function
                  first=True,  # else last
                  target=True, # else False
                  left=0, right=2**31-1) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first^target:
            return not func_(val)
        return func_(val)

    while left < right:
        mid = (left + right) // 2
        if func(mid):
            right = mid
        else:
            left = mid + 1
    if first:  # find first True
        return left
    else:      # find last False
        return left-1


def ceiling_division(numer, denom):
    return -((-numer)//denom)

def solve_(arr, m):
    # your solution here
    arr = [0] + arr
    negative_diffs = [a-b for a,b in zip(arr, arr[1:])]
    heapq.heapify(negative_diffs)

    allcost = 0
    c = Counter()
    for diff in negative_diffs:
        allcost += diff**2
        c[diff] += 1

    if allcost <= m:
        return 0

    added = set(negative_diffs)

    curinstall = 0
    for _ in range(10):
        log(negative_diffs, c, curinstall, allcost)
        a = -heapq.heappop(negative_diffs)
        if a == 1:
            break

        x = a // 2
        y = a - x
        
        old_cost = a**2
        new_cost = x**2 + y**2
        diff = old_cost - new_cost
        allcost -= diff * c[a]
        curinstall += c[a]

        if allcost <= m:
            return curinstall

        c[-x] += c[a]
        c[-y] += c[a]
        if -x not in added:
            heapq.heappush(negative_diffs, -x)
            added.add(-x)
        if -y not in added:
            heapq.heappush(negative_diffs, -y)
            added.add(-y)

    for curinstall in range(1,100_000):
        a = heapq.heappop(negative_diffs)
        x = a // 2
        y = a - x
        
        curinstall += 1
        old_cost = a**2
        new_cost = x**2 + y**2
        diff = old_cost - new_cost
        allcost -= diff

        if allcost <= m:
            return curinstall

        heapq.heappush(negative_diffs, x)
        heapq.heappush(negative_diffs, y)

    diffs = [b-a for a,b in zip(arr, arr[1:])]

    def func(x):
        res = 0
        for diff in diffs:
            components = ceiling_division(diff, x)
            maxsize = ceiling_division(diff, components)

            smalls = maxsize * components
            larges = components - smalls
            res = smalls * maxsize**2 + larges * (maxsize-1)**2
        log(res, x)
        return res <= m


    return binary_search(func, left=True, target=True)

    return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    _ = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    k = int(input())

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
