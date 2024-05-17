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


def query(l, x):
    print(f"? {l} {x}", flush=True)
    response = int(input())
    return response


def alert(m):
    print(f"! {m}", flush=True)
    response = int(input())
    return response


# -----------------------------------------------------------------------------

def solve():
    n,k = list(map(int,input().split()))
    curlen = 1
    curmax = 1
    query_count = 0
    
    while query_count < 2*n and curmax <= n and curlen <= n:
        log(curmax, curlen)
        l = 1
        r = query(l, curlen * curmax)
        if r == n+1:
            curmax += 1
            continue

        for _ in range(k-1):
            l = r+1
            r = query(l, curlen * curmax)
            if r == n+1:
                curlen += 1
                break

        else:
            verdict = alert(curlen * curmax)
            assert verdict == 1
            return

    alert(-1)
    assert verdict == 1
    return




# read line as an integer
t = int(input())

for _ in range(t):
    solve()

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here
