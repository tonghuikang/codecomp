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

def query(pos):
    print("{}".format(pos), flush=True)
    # response = 0
    response = int(input())
    if response == -1:
        assert False
    return response

# def alert(pos):
#     print("! {}".format(pos), flush=True)
#     sys.exit()

# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

@functools.lru_cache(maxsize=30)
def grayCode(n):
    results = [0]
    for i in range(n):
        results += [x + pow(2, i) for x in reversed(results)]
    return results


k = int(input())
for _ in range(k):
    n,k = list(map(int,input().split()))

    for i,x in reversed(list(enumerate(bin(n)[2:][::-1]))):
        log(i,x)
        if x == 1:
            for i in list(range(1,2**i//2+1)) + list(range(1,2**i//2+1)):
                res = query(i)
                if res:
                    break
            else:
                res = query(2**i)
                if res:
                    break
                continue
            break
                    


sys.exit()



# -----------------------------------------------------------------------------

# your code here