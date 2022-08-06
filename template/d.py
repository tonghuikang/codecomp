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

def query(a,b):
    print("? {} {}".format(a+1,b+1), flush=True)
    response = int(input())
    return response

def alert(pos):
    print("! {}".format(pos+1), flush=True)

# -----------------------------------------------------------------------------

# read line as an integer
cases = int(input())

import random

for _ in range(cases):

    k = int(input())
    arr = list(range(2**k))

    # log(2/3 * 2**k)

    pool = set()
    random.shuffle(arr)
    if len(arr)%2:
        pool.add(arr[-1])
    for a,b in zip(arr[0::2], arr[1::2]):
        x = query(a,b)
        if x == 1:
            pool.add(a)
        if x == 2:
            pool.add(b)
        else:
            pass

    while len(pool) > 1:
        log(pool)
        arr = list(pool)

        pool = set()
        random.shuffle(arr)
        if len(arr)%2:
            pool.add(arr[-1])
        for a,b in zip(arr[0::2], arr[1::2]):
            x = query(a,b)
            if x == 1:
                pool.add(a)
            if x == 2:
                pool.add(b)
            else:
                pass

    alert(list(pool)[0])

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