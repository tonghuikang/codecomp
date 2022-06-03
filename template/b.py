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
# OFFLINE_TEST = getpass.getuser() == "htong"
OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------

def query(arr):
    print("? {}".format("".join(str(x) for x in arr)), flush=True)
    response = int(input())
    return response

def alert(pos):
    print("! {}".format(pos), flush=True)

# -----------------------------------------------------------------------------

# read line as an integer
_, m = list(map(int,input().split()))

costs = [-1]*m

for i in range(m):
    arr = [0]*m
    arr[i] = 1
    cost = query(arr)
    costs[i] = (cost, i)

state = [1]*m
value = query(state)
costs = sorted(costs, reverse=True)

state = [1]*m
for cost, i in costs[:-1]:
    state[i] = 0
    a = query(state)
    if a == value - cost:  # important, put back
        state[i] = 1
    else:  # not important
        value = a

alert(value)
sys.exit()

# query only for each railway

# start from the largest, query to see if drop

