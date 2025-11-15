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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------

# A unrewarded competitor will be unhappy if:
# any other competitor with equal or lower score receives any merchandise at all.

# A rewarded competitor will be unhappy if either:
# any other competitor of strictly lower score receives equal or more units of merchandise, or
# any other competitor with equal score receives more units of merchandise.

def binary_search(
    func_,  # condition function
    first=True,  # else last
    target=True,  # else False
    left=0,
    right=2**31 - 1,
) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first ^ target:
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
    else:  # find last False
        return left - 1


def solve_(n,m,arr,brr):
    # maximize competitors rewarded

    # how do the types matter here?
    # each competitor can only receive one merch type

    # everyone not getting rewarded is a solution

    # same score, same number of merchandise (distinct types)

    # binary search on the minimum score recieving prizes
    # build the demand curve

    # transform availability to packages of distinct gifts
    # each valid competitor will choose from the package of distinct gifts
    # remainder package can be throw back to the pool
    # you cannot combine multiple distinct packages to satisfy your demand
    # - edge cases?
    # supply 7 1 (2 1x6)
    # - demand 2 2 2 2 - cannot - but actually can
    # supply 3 1 (2 1 1)
    # - demand 2 2 - cannot - but actually can
    # supply 4 1
    # - demand 3 2 - cannot
    # supply 4 1
    # - demand 2 2 - can

    # transform available to packages of distinct gifts
    brr = brr[::-1]
    packages = [0]
    for x in brr:
        packages.append(len(brr))


    cntr = sorted(Counter(arr).items(), reverse=True)
    competitors = [v for k,v in cntr]  # discard k
    del cntr

    def func(idx):

        positive_demand_curve = []
        prev_v = 0
        for v in competitors[:idx]:
            positive_demand_curve.append(prev_v + v)
            prev_v += v
            
        positive_demand_curve = positive_demand_curve[::-1]
        available = [x for x in brr]

        # log()
        # log(positive_demand_curve)
        # log(available)

        # iterate over the supply, collapse the demand

        carryover_demand = 0
        for demand in positive_demand_curve:
            demand += carryover_demand
            if demand == 0:
                continue
            if not available:
                # log("False")
                return False
            avail = available.pop()
            deduct = min(demand, avail)
            carryover_demand = demand - deduct
        
        if carryover_demand > sum(available): 
            # log("False")
            return False

        # log("True")
        return True



    # for idx in range(len(competitors) + 1):
    #     print(idx, func(idx))
    #     print()

    if func(len(competitors)):
        return sum(competitors)

    cntr_idx = binary_search(func, first=False, target=True, left=0, right=len(competitors))

    awarded = competitors[:cntr_idx]
    return sum(awarded)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    xrr = list(map(int,input().split()))
    yrr = list(map(int,input().split()))
    xrr.sort()
    yrr.sort()
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,xrr,yrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
