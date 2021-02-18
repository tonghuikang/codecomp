#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args, flush=False):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr, flush=flush)

# ---------------------------- template ends here ----------------------------

def query(left, right):
    assert left != right
    # left, right = sorted([left,right])
    print("? {} {}".format(left+1,right+1), flush=True)
    response = int(input())-1
    return response

def alert(pos):
    print("! {}".format(pos+1), flush=True)
    sys.exit()

# -----------------------------------------------------------------------------

# read line as an integer
k = int(input())

upper = k-1
lower = 0
idx_second_largest = query(0, k-1)

if idx_second_largest == 0:
    left_side = False
else:
    log("left or right", flush=True)
    idx_confirm = query(0, idx_second_largest)
    left_side = idx_confirm == idx_second_largest

if left_side:  # confirmed left
    lower = 0
    upper = idx_second_largest - 1

    while lower < upper:
        mid = (upper + lower + 1)//2
        # log(lower, upper, mid, flush=True)
        idx_confirm = query(mid, idx_second_largest)
        # log(idx_confirm==idx_second_largest, flush=True)
        if idx_confirm == idx_second_largest:  # between upper and mid incl
            lower = mid
        else:
            upper = mid-1
    alert(lower)

else:  # confirmed right
    lower = idx_second_largest + 1
    upper = k-1

    while lower < upper:
        mid = (upper + lower)//2
        # log(lower, upper, mid, flush=True)
        idx_confirm = query(idx_second_largest, mid)
        # log(idx_confirm==idx_second_largest, flush=True)
        if idx_confirm == idx_second_largest:  # between lower and mid incl
            upper = mid
        else:
            lower = mid+1
    alert(lower)

