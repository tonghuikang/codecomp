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

query_cache = []

def query_method(arr):
    print("? {}".format(" ".join(str(pos+1) for pos in arr)), flush=True)
    response = int(input())-1
    query_cache.append([arr.copy(), response])
    return response

def alert_method(arr):
    print("! {}".format(" ".join(str(pos+1) for pos in arr)), flush=True)
    sys.exit()

# -----------------------------------------------------------------------------


# read line as an integer
size = int(input())

# find the one
# find the rest

count = 0
for i in range(size):
    # test value of final position
    query = [i for _ in range(size)]
    query[-1] = 0
    k = query_method(query)
    if k != -1:
        count += 1

last_number = count

log(last_number)

res = [0 for _ in range(size)]
res[-1] = last_number

for i in range(size):
    if i == last_number:
        continue
    # test value of final position
    query = [last_number for _ in range(size)]
    query[-1] = i
    k = query_method(query)
    res[k] = i

assert sorted(set(res)) == list(range(size))

# for query, result in query_cache:
#     sumarr = [a+b for a,b in zip(query, res)]
#     seen = {}
#     for i,x in enumerate(sumarr):
#         if x in seen:
#             assert seen[x] == result
#             break
#         seen[x] = i
#     else:
#         assert result == -1

alert_method(res)
# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here