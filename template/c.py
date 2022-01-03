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

def query(pos):
    print("? {}".format(pos+1), flush=True)
    response = int(input()) - 1
    return response

def alert(arr):
    print("! {}".format(" ".join(str(x+1) for x in arr)), flush=True)
    sys.exit()

# -----------------------------------------------------------------------------

for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    results = []
    visited = set()

    cur = 0
    idx = 0
    while cur < n:
        if cur in visited:
            cur += 1
            continue

        start = query(cur)
        start_idx = idx
        visited.add(start)
        idx += 1

        cycle = [start]
        while True:
            q = query(cur)
            idx += 1
            cycle.append(q)
            visited.add(q)

            # print(cycle)

            if q == start:
                break

        results.append((start_idx, cycle))
        cur += 1

    res = [-1] * n

    for _, cycle in results:
        for prev, nex in zip(cycle, cycle[1:]):
            res[prev] = nex

    alert(res)

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