#!/usr/bin/env python3
import sys
# import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "htong"
OFFLINE_TEST = False  # codechef does not allow getpass
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


def solve_(arr, n):
    # your solution here

    # arr = [0] + arr + [n+1]
    a = arr[0] - 1
    b = n - arr[-1]
    log(a,b)

    diffs = [b-a-1 for a,b in zip(arr, arr[1:])]
    # diffs[0][0] = diffs[0][2]
    # diffs[-1][0] = diffs[-1][2]
    # diffs[0][1] = 1
    # diffs[-1][1] = 1

    diffs.sort(reverse=True)

    
    ret = []
    log(diffs)
    cur = 0
    for c in diffs:
        c -= cur*2
        if c <= 0:
            continue
        cur += 2
        ret.append(max(1, c-1))

    maxres = sum(ret)

    cur = 1
    res = a
    for c in diffs:
        c -= cur*2
        if c <= 0:
            continue
        cur += 2
        res += max(1, c-1)
    # log(res)
    maxres = max(maxres, res)

    cur = 2
    res = a + b - 1
    for c in diffs:
        c -= cur*2
        if c <= 0:
            continue
        cur += 2
        res += max(1, c-1)
    # log(res)
    maxres = max(maxres, res)
 
    # heap = []
    # heap.append((-diffs[0], 1, -diffs[0]))
    # heap.append((-diffs[0], 1, -diffs[-1]))

    # for x in diffs[1:-1]:
    #     heap.append((2, -x))
    
    # heapq.heapify(heap)

    # cur = 0
    # res = 0
    # while heap:
    #     log(res, heap)
    #     c, nx = heapq.heappop(heap)
    #     x = -nx
    #     x -= cur*c
    #     if x <= 0:
    #         continue
    #     if c == 1:
    #         res += x
    #         cur += 1
    #         continue
    #     res += 1
    #     x -= 1
    #     heapq.heappush(heap, (1, -x))
    #     cur += 1

    return maxres


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
