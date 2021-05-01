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

def query():
    response = int(input())
    return response

def alert(pos):
    print("{}".format(pos+1), flush=True)

# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
t,n,b,p = list(map(int,input().split()))
# lst = list(map(int,input().split()))

for _ in range(t):

    state = []
    building = {pos:b-1 for pos in range(n)}
    waiting = set()
    cur = 0

    for _ in range(n*b):
        nex = query()

        if not building or (nex == 9 and waiting):
            for pos in waiting:
                break
            waiting.remove(pos)
        else:
            pos = min(building, key=building.get)
            building[pos] -= 1
            if building[pos] == 0:
                waiting.add(pos)
                del building[pos]

        alert(pos)

res = int(input())

sys.exit()
