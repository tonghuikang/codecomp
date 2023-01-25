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

def query(pos):
    print("- {}".format(pos), flush=True)
    response = int(input())
    return response

def alert(pos):
    print("! {}".format(pos), flush=True)

# -----------------------------------------------------------------------------


def solve(init, query, alert):
    res = 0
    k = init
    for _ in range(30):
        if k == 0:
            break
        val = 2**(k) - 1
        log("-", val)
        res += val
        k = query(val)
        log(k)
    else:
        assert False
    return res


def query2(pos):
    global x
    if x < pos:
        assert False
    x -= pos
    log(bin(x))
    return bin(x).count("1")

def alert2(pos):
    global x
    if x != pos:
        assert False


for x in range(1, 10000):
    log(x)
    solve(bin(x).count("1"), query2, alert2)


# read line as an integer
for case_num in range(int(input())):
    k = int(input())
    res = solve(k, query, alert)
    alert(res)

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here
sys.exit()
