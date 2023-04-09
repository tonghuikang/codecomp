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
        " ".join(str(x+1) for x in perm1),
        " ".join(str(x+1) for x in perm2),        
    ), flush=True)
    response = int(input())
    assert response == 1


def get_order(n):
    arr = list(range(n // 2))[::-1]
    brr = list(range(n // 2, n))

    order = []
    while arr or brr:
        if arr:
            order.append(arr.pop())
        if brr:
            order.append(brr.pop())
    return order


# -----------------------------------------------------------------------------

def solve(n, add=add, query=query, alert=alert):
    if n == 2:
        alert([0,1], [1,0])
        return
    # read line as an integer

    order = get_order(n)

    add(n)
    add(n+1)

    dist_from_zero = [0 for _ in range(n)]
    for i in range(1,n):
        dist_from_zero[i] = query(0,i)

    idx = dist_from_zero.index(max(dist_from_zero))
    dist_from_extreme = [0 for _ in range(n)]
    for i in range(n):
        if i == idx:
            continue
        dist_from_extreme[i] = query(idx,i)

    perm_to_order = dist_from_extreme

    log("order", order)
    log("perm_to_order", perm_to_order)

    assert -1 not in perm_to_order
    assert sorted(perm_to_order) == list(range(n))


    perm1 = [-1 for _ in range(n)]
    for i,x in enumerate(perm_to_order):
        perm1[i] = order[x]

    order.reverse()

    perm2 = [-1 for _ in range(n)]
    for i,x in enumerate(perm_to_order):
        perm2[i] = order[x]

    log(perm1)
    log(perm2)

    assert sorted(perm1) == list(range(n))
    assert sorted(perm2) == list(range(n))

    alert(perm1, perm2)


import random
while OFFLINE_TEST and False:

    n = random.randint(2,4)

    perm = list(range(n))
    random.shuffle(perm)
    log(perm)

    order = get_order(n)

    def add2(pos):
        pass

    def query2(a,b):
        aval = perm[a]
        bval = perm[b]
        return abs(order.index(aval) - order.index(bval))

    def alert2(perm1, perm2):
        assert perm1 == perm or perm2 == perm
        pass

    solve(n, add=add2, query=query2, alert=alert2)


for case_num in range(int(input())):
    n = int(input())
    solve(n)

sys.exit()
