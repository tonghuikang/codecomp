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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


# ---------------------------- template ends here ----------------------------


def query(i, j):
    print("? {} {}".format(i+1, j+1), flush=True)
    response = input().strip()
    return response


def alert(arr):
    arr = " ".join(str(x) for x in arr)
    print("! {}".format(arr), flush=True)


# -----------------------------------------------------------------------------

# read line as an integer
t = int(input())

for _ in range(t):
    n = int(input())

    arr = [1 for _ in range(n)]

    # those not reachable by curhead will be 0

    curhead = n-1
    curquery = n-2

    while curquery >= 0:
        response = query(curquery, curhead)
        if response == "NO":
            arr[curquery] = 0
        else:
            curhead = curquery
        curquery -= 1

    alert(arr)


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
