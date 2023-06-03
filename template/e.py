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

# ---------------------------- template ends here ----------------------------

def compute(arr):
    # arr = sorted(arr)
    vals = set([0])
    for x in arr:
        new_vals = set()
        for y in vals:
            new_vals.add(x+y)
            new_vals.add(x-y)
        vals = new_vals
    log(arr, 0 in vals)
    return 0 in vals


def query(pos):
    print("{}".format(pos+1), flush=True)
    response = int(input())
    return response


# def alert(pos):
#     print("! {}".format(pos+1), flush=True)
#     sys.exit()

# -----------------------------------------------------------------------------

# read line as an integer
n = int(input())
arr = list(map(int,input().split()))

if compute(arr):
    print("Second", flush=True)
    while True:
        log(arr)
        response = int(input())
        if response == 0:
            sys.exit()
        idx = response - 1
        assert arr[idx] != 0

        for i in range(n):
            if i == idx:
                continue
            if arr[i] == 0:
                continue
            brr = [x for x in arr]
            brr[i] -= min(arr[i], arr[idx])
            brr[idx] -= min(arr[i], arr[idx])
            if compute(brr):
                arr = brr
                print("{}".format(i+1), flush=True)
                break
        else:
            break

else:
    print("First", flush=True)
