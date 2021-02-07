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
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------
counter = 0


@functools.lru_cache(maxsize=100)
def query(pos):
    global counter
    counter += 1
    print("? {}".format(pos+1), flush=True)
    response = int(input())
    return response

def alert(pos):
    print("! {}".format(pos+1), flush=True)
    sys.exit()

# -----------------------------------------------------------------------------


@functools.lru_cache(maxsize=100)
def confirm(pos):
    if pos == 0 or pos >= k-1:
        return False
    a = query(pos-1)
    b = query(pos)
    c = query(pos+1)
    if a > b and b < c:
        alert(pos)
    return False

# read line as an integer
k = int(input())

if k < 3:
    alert(0)

left_idx = 0
right_idx = k-1

left_val = query(left_idx)
right_val = query(right_idx)

left_val_a = query(left_idx+1)
right_val_b = query(right_idx-1)

if left_val_a > left_val:
    alert(0)

if right_val_b > right_val:
    alert(right_idx)

# while True:
#     if left_idx == right_idx:
#         confirm(left_idx)
#         confirm(left_idx+1)
#         confirm(left_idx-1)
#         k -= 1
#         left_idx = 0
#         right_idx = k

#     mid_idx = (left_idx + right_idx) // 2
#     mid_val = query(mid_idx)

#     left_val_diff = abs(left_val - mid_val)
#     left_dist_diff = mid_idx - left_idx

#     right_val_diff = abs(right_val - mid_val)
#     right_dist_diff = right_val - mid_idx

#     if left_val_diff < left_dist_diff:
#         right_idx = mid_idx
#         continue
#     elif right_val_diff < right_dist_diff:
#         left_idx = mid_idx
#         continue
#     else:
#         confirm(mid_idx)

#     if counter > 100:
#         assert 1==2
#         break

left = 0
right = k-1

while left < right:
    mid = (left+right)/2
    confirm(mid)

    if query(mid) > query(mid+1):
        left = mid+1
    else:
        right = mid-1


alert(k//10)

