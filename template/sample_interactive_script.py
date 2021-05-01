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
# log(p)

for _ in range(t):
    state = []
    building = {pos:b-2 for pos in range(n)}
    waiting = {}
    cur = 0
    limit = 0.05*n*b

    for cnt in range(n*b):
        nex = query()

        for _ in range(1):
            if not building or (nex == 9 and waiting):
                pos = min(waiting, key=waiting.get)
                waiting[pos] -= 1
                if waiting[pos] == 0:
                    del waiting[pos]
                continue

            if (not building or (nex == 8 and waiting)) and cnt > limit:
                pos = max(waiting, key=waiting.get)
                if waiting[pos] == 2 or not building:
                    waiting[pos] -= 1
                    continue

            pos = min(building, key=building.get)
            building[pos] -= 1
            if building[pos] == 0:
                del building[pos]
                waiting[pos] = 2

        alert(pos)

res = int(input())

sys.exit()
