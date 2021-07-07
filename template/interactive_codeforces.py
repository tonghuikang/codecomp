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
    print("{}".format(pos), flush=True)
    # response = 0
    response = int(input())
    return response

# def alert(pos):
#     print("! {}".format(pos), flush=True)
#     sys.exit()

# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

@functools.lru_cache(maxsize=30)
def grayCode(n):
    results = [0]
    for i in range(n):
        results += [x + pow(2, i) for x in reversed(results)]
    return results


k = int(input())
for _ in range(k):
    n,k = list(map(int,input().split()))

    if n == 1:
        res = query(0)
        break

    if n == 2:
        res = query(1)
        if res == 1: break
        res = query(1)
        break

    n -= 1

    # res = query(0)

    while n:
        log(n)
        p = int(math.log2(n))
        # for i in grayCode(p)[1:]:
        for i in list(range(1,2**p//2+1)) + list(range(1,2**p//2+1)):
            res = query(i)
            if res == 1: break
        else:
            res = query(2**p)
            if res == 1: break
            n -= 2**p
            continue
        break

sys.exit()



# -----------------------------------------------------------------------------

# your code here