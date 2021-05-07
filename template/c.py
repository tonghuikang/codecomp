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

@functools.lru_cache(maxsize=2*10**4)
def query(t,i,j,x):
    print("? {} {} {} {}".format(t,i+1,j+1,x), flush=True)
    response = int(input())
    return response

def alert(arr):
    print("! {}".format(" ".join(str(x) for x in arr)), flush=True)

# -----------------------------------------------------------------------------

# read line as an integer
num_cases = int(input())

for _ in range(num_cases):
    n = int(input())

    res = [0 for _ in range(n)]

    i,j = 0,1
    a01 = max(query(1,i,j,n-1), query(1,j,i,n-1))
    b01 = min(query(2,i,j,1), query(2,j,i,1))

    i,j = 0,2
    a02 = max(query(1,i,j,n-1), query(1,j,i,n-1))
    b02 = min(query(2,i,j,1), query(2,j,i,1))

    i,j = 0,2
    a12 = max(query(1,i,j,n-1), query(1,j,i,n-1))
    b12 = min(query(2,i,j,1), query(2,j,i,1))

    res[0] = set([a01, b01]) & set([a02, b02])
    res[1] = set([a01, b01]) & set([a12, b12])
    res[2] = set([a02, b02]) & set([a12, b12])

    # res[:3] = [3,1,4]

    assert len(set(res[:3])) == 3

    order = list(range(3,n))
    random.shuffle(order)

    maxidx = res.index(max(res[:3]))

    for idx in order:
        log(res, idx, maxidx)
        p = query(2, idx, maxidx, 1)
        if p == res[maxidx]:
            p = query(1, maxidx, idx, n-1)
            maxidx = idx
            res[idx] = p
        else:
            res[idx] = p

    assert len(set(res)) == n

    alert(res)


sys.exit()