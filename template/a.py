#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

# input = sys.stdin.readline  # to read input quickly

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


def query(a,b,c,d):
    print("? {} {} {} {}".format(a,b,c,d), flush=True)
    response = input()
    return response


def alert(a,b):
    print("! {} {}".format(a,b), flush=True)


# -----------------------------------------------------------------------------

# read line as an integer
k = int(input())

for _ in range(k):
    n = int(input())
    
    biggest = 0
    for i in range(1,n):
        val = query(biggest, biggest, i, i)
        if val == ">":
            continue
        elif val == "<":
            biggest = i
        else:
            assert False
    
    complement_set = set([0])
    complement_example = 0

    for i in range(1,n):
        val = query(biggest, complement_example, biggest, i)
        if val == ">":
            continue
        elif val == "<":
            complement_set = set([i])
            complement_example = i
        elif val == "=":
            complement_set.add(i)
        else:
            assert False
    
    smallest_complement = complement_example
    for i in complement_set:
        val = query(smallest_complement, smallest_complement, i, i)
        if val == ">":
            smallest_complement = i
        elif val == "<":
            continue
        else:
            pass

    alert(biggest, smallest_complement)


sys.exit()

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here
