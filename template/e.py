#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def query(groups):
    print("? {}".format(" ".join(" ".join(str(x) for x in group) for group in groups)), flush=True)
    response = int(input())
    return response

def alert(pos):
    print("! {}".format(pos), flush=True)
    sys.exit()


def alert2(pos):
    print("{}".format(pos), flush=True)
    sys.exit()

n,k = list(map(int,input().split()))


# x x x - -
# x x - x -
# x x - - x


group_size = math.gcd(n,k)  # treat them as one

groups = []

for i in range(n//group_size):
    j = i+1
    groups.append(list(range(i*group_size+1,j*group_size+1)))

g = len(groups)
n,k = n//group_size, k//group_size
if k%2 == 0:
    # never possible to break even, where to total count is odd
    alert2(-1)

if n%2 == 1:

    res = 0
    for i in range(n-k+1):
        to_query = []
        for j in range(k-1):
            to_query.append(groups[j])  
        to_query.append(groups[k+i-1])
        # log(to_query)
        val = query(to_query) 
        res = res^val
    
    alert(res)

# x x x -
# x - x x
# x x - x

# alert2(-1)
res = 0
for i in range(n):
    to_query = []
    for j in range(k):
        to_query.append(groups[(g-j-i-1)%g])  
    # to_query.append(groups[(k+i-1)%(g-k+2)])
    # to_query.append(groups[(k+i)%(g-k+2)])
    # log(to_query)
    val = query(to_query) 
    res = res^val

alert(res)