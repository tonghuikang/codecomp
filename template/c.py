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

def query(x,y):
    print("? {} {}".format(x+1,y+1), flush=True)
    response = int(input())
    return response

def alert(x,y):
    print("! {} {}".format(x+1,y+1), flush=True)
    # sys.exit()

# -----------------------------------------------------------------------------

def dist(a,b,x,y):
    return abs(a-x) + abs(b-y) - min(abs(a-x), abs(b-y))


def check(i,j,top_left,top_right,bottom_left):
    if dist(i,j,0,0) == top_left:
        if dist(i,j,0,m-1) == top_right:
            if dist(i,j,n-1,0) == bottom_left:
                return True
    return False

# read line as an integer
for case_num in range(int(input())):

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    top_left = query(0,0)
    top_right = query(0,m-1)

    if top_left + top_right == m-1:
        y = query(top_left,0)
        alert(top_left,y)
        continue

    bottom_left = query(n-1,0)

    qrr = []
    for q in [top_left, top_right, bottom_left]:
        qrr.append(q)

    # xrr = []
    # yrr = []

    # xrr.append(top_left)
    # yrr.append(top_left)

    # xrr.append(top_right)
    # yrr.append(m-1-top_right)

    # xrr.append(n-1-bottom_left)
    # yrr.append(bottom_left)

    qrr = sorted(set(qrr))

    allcnt = 0
    for x in qrr:
        for y in qrr:
            if check(x,y,top_left,top_right,bottom_left):
                allcnt += 1
                alert(x,y)

    assert allcnt == 1

# -----------------------------------------------------------------------------
sys.exit()
# your code here