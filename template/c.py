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

def solve(n,m,query=query,alert=alert):

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    top_left = query(0,0)

    if m >= n:
        top_right = query(0,m-1)
        if top_left + top_right == m-1:
            # log("y")
            x = query(0,top_left)
            alert(x,top_left)
            return
        bottom_left = query(n-1,0)

    else:
        bottom_left = query(n-1,0)
        if top_left + bottom_left == n-1:
            # log("x")
            x = query(top_left,0)
            alert(top_left,x)
            return
        top_right = query(0,m-1)

    assert top_left + top_right >= m-1
    assert top_left + bottom_left >= n-1

    qrr = []
    for q in [top_left, top_right, bottom_left, m-1-top_right, n-1-bottom_left]:
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
    # log(qrr)

    allcnt = 0
    for x in qrr:
        if not (0 <= x <= n-1):
            continue
        for y in qrr:
            if not (0 <= y <= m-1):
                continue
            if check(x,y,top_left,top_right,bottom_left):
                allcnt += 1
                alert(x,y)
                # return

    # log(allcnt)
    assert allcnt == 1


while OFFLINE_TEST:
    n = random.randint(1,5)
    m = random.randint(1,5)
    a = random.randint(1,n)
    b = random.randint(1,m)

    def query(x,y):
        return dist(a,b,x+1,y+1)

    def alert(x,y):
        log(x,y)
        assert (x+1,y+1) == (a,b)
    
    log()
    log(n,m,a,b)
    solve(n,m,query,alert)



# read line as an integer
for case_num in range(int(input())):

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    n,m = list(map(int,input().split()))

    solve(n,m)





# -----------------------------------------------------------------------------
sys.exit()
# your code here