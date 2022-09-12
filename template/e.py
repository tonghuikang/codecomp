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

def query1(x):
    print("? {} {}".format(x+1, x+2), flush=True)
    response = int(input())
    return response

def query2(x):
    print("? {} {}".format(x+2, x+1), flush=True)
    response = int(input())
    return response

def alert(pos):
    print("! {}".format(pos), flush=True)
    sys.exit()

# -----------------------------------------------------------------------------

arr = []
for i in range(50):
    a = query1(i)
    b = query2(i)
    if a != b:
        alert(a + b)
    if a == -1:
        alert(i+1)

