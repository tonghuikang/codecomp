#!/usr/bin/env python3
import sys, os, getpass
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

def ceiling_division(numer, denom):
    return -((-numer)//denom)

# ---------------------------- template ends here ----------------------------

n,k = list(map(int,input().split()))

if False:
# if True:
    # testing
    # conclusion
    # minimum is always on the left of impostor
    # impostor always have k
    # minimum is always on the right of impostor
    vals = [k for _ in range(n)]
    impostor = 100
    for z in range(1000):
        new1 = [x//2 for x in vals]
        new2 = [ceiling_division(x,2) for x in vals]
        new2[impostor] += new1[impostor]
        new1[impostor] = 0
        vals = [0 for _ in range(n)]
        for i,x in enumerate(new1):
            vals[(i-1)%n] += x
        for i,x in enumerate(new2):
            vals[(i+1)%n] += x
        # log(new1)
        # log(new2)
        log(*vals)
        minval = min(vals)
        c = Counter(vals)
        log(z, vals.index(minval), c[k], minval)
        # log(Counter(vals))

# helper functions

def inc(x):
    return (x+1)%n

def dec(x):
    return (x-1)%n

records = []

def query(pos):
    print("? {}".format(pos+1), flush=True)
    response = int(input())
    records.append(response)
    return response

def alert(pos):
    print("! {}".format(pos+1), flush=True)
    sys.exit()


# brute force if under 400

# if n < 400:
#     for i in range(n//2 + 1):
#         query(0)

#     log("querying all")
#     # should stablilise by now
#     records = []

#     for i in range(n):
#         query(i)
    
#     log(records)
#     response = records + records
#     for i,(a,b,c) in enumerate(zip(response, response[1:], response[2:])):
#         if a < b < c and b == k:
#             alert((i+1)%n)
#     log("error")
#     alert(0)

# random sampling

spacing = int(math.sqrt(n))
pos = random.randint(0,n-1)

response = 0
while len(records) < 999:
    pos = (pos+spacing+random.randint(0, 1))%n
    response = query(pos)
    if response != k:
        break
    
log("breaking".format(pos))

if response > k:  # search for k by decreasing index
    log("decr")
    while len(records) < 999:
        pos = dec(pos)  # decrease
        response = query(pos)
        if response == k:
            alert(pos)
else:  # search for k by increasing index
    log("incr")
    while len(records) < 999:
        pos = inc(pos)  # increase
        response = query(pos)
        if response == k:
            alert(pos)
alert(pos)