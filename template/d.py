#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------

query_range_count = 0
query_alpha_count = 0

def query_range(l, r):
    global query_range_count
    query_range_count += 1
    if query_range_count > 6000:
        assert False
    assert l >= 0
    assert r >= 0
    print("? 2 {} {}".format(l+1, r+1), flush=True)
    response = int(input())
    return response

def query_alpha(x):
    global query_alpha_count
    query_alpha_count += 1
    if query_alpha_count > 26:
        assert False
    assert x >= 0
    print("? 1 {}".format(x+1), flush=True)
    response = input().strip()
    return response


# ref = "asfiahbuisbdaijsbdajnksldaknsodna"
# log(len(ref))

# def query_range(l, r):
#     return len(set(list(ref[l:r+1])))

# def query_alpha(x):
#     return ref[x]

# -----------------------------------------------------------------------------

# read line as an integer
n = int(input())

alpha_to_latest_idx = {}
res = ""

for i in range(n):
    distinct_count = query_range(0,i)
    if distinct_count > len(alpha_to_latest_idx):
        alpha = query_alpha(i)
        alpha_to_latest_idx[alpha] = i
        res += alpha
        continue
    
    stack = sorted([(idx, alpha) for alpha,idx in alpha_to_latest_idx.items()])
    log(stack)
    log(res)

    def func(x):
        idx, alpha = stack[x]
        expected_if_distinct = len(stack) - x + 1
        distinct_count = query_range(idx, i)
        log(x, idx, alpha, expected_if_distinct, distinct_count)
        return expected_if_distinct <= distinct_count
    
    x = binary_search(func, first=False, target=False, right=len(alpha_to_latest_idx))
    idx_old,alpha = stack[x]
    log(idx_old,alpha,x)
    alpha_to_latest_idx[alpha] = i
    res += alpha

print("! {}".format(res), flush=True)
response = input()


# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here
sys.exit()
