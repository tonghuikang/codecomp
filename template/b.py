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

def add(pos):
    print("+ {}".format(pos+1), flush=True)
    response = int(input())
    assert response == 1
    return response

def query(a,b):
    print("? {} {}".format(a+1, b+1), flush=True)
    response = int(input())
    return response

def alert(perm1, perm2):
    print("! {} {}".format(
        " ".join(str(x) for x in perm1),
        " ".join(str(x) for x in perm2),        
    ), flush=True)
    response = int(input())
    assert response == 1


# -----------------------------------------------------------------------------

for case_num in range(int(input())):
    # read line as an integer
    n = int(input())

    add(n)
    add(n+1)

    dist = query(0,1)
    dist_from_zero = [-1,-1]
    dist_from_one = [-1,-1]

    for i in range(2,n):   # 2n-4
        d0 = query(0,i)
        d1 = query(1,i)
        dist_from_zero.append(d0)
        dist_from_one.append(d1)
    
    del d0
    del d1
    
    p0 = max(dist_from_zero)
    p1 = max(dist_from_one)
    p1 = n-1-p1

    arr = list(range(n // 2))[::-1]
    brr = list(range(n // 2, n))

    perm_to_order = [-1 for _ in range(n)]
    perm_to_order[0] = p0
    perm_to_order[1] = p1

    for i in range(2, n):
        # find where the item on position i of perm is on the order
        d0 = dist_from_zero[i]
        d1 = dist_from_one[i]

        if d0 + d1 == dist:
            # in the middle
            perm_to_order[i] = p1 + d1  # p0 - d0
            assert p0 - d0 == p1 + d1
            continue
        
        if d0 > d1:
            # on the p1 side
            perm_to_order[i] = p0 - d0  # or p1 - d1
            assert p0 - d0 == p1 - d1
            continue

        if d0 < d1:
            # on the p0 side
            perm_to_order[i] = p0 + d0  # or p1 + d1
            assert p0 + d0 == p1 + d1
            continue

    assert -1 not in perm_to_order
    assert sorted(perm_to_order) == list(range(n))

    order = []
    while arr or brr:
        if arr:
            order.append(arr.pop())
        if brr:
            order.append(brr.pop())
    # print(order)

    perm1 = [-1 for _ in range(n)]
    for i,x in enumerate(perm_to_order):
        perm1[x] = order[i]

    order.reverse()

    perm2 = [-1 for _ in range(n)]
    for i,x in enumerate(perm_to_order):
        perm1[x] = order[i]

    alert(perm1, perm2)



sys.exit()
