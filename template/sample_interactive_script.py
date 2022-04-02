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

def walk():
    print("W", flush=True)
    response = list(map(int,input().split()))
    return response

def teleport(pos):
    print("T {}".format(pos+1), flush=True)
    response = list(map(int,input().split()))
    return response

def alert(pos):
    print("E {}".format(pos), flush=True)

# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = v
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here

for case_num in range(int(input())):
    n,k = list(map(int,input().split()))
    k0 = k
    log(n,k)
    lst = list(range(n))
    random.shuffle(lst)

    _,_ = list(map(int,input().split()))

    res = []

    for x in lst:
        # if k == 0:
        #     break
        # k -= 1
        # _, count = walk()

        # res.append(count)

        if k == 0:
            break
        k -= 1

        _, count = teleport(x)

        res.append(count)
        # log(count)
    
    estimate = round(sum(res) / len(res) * n / 2)
    alert(estimate)

sys.exit()
