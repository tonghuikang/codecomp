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


def solve_(arr, k):
    # your solution here
    # arr2 = tuple(arr)
    # arr = [min(x,y) for x,y in zip(arr,arr[::-1])]
    brr = arr[(len(arr))//2:]
    # log(s)
    arr = arr[:(len(arr)+1)//2]

    # log(arr)

    
    cnt = 0
    for x in arr:
        cnt = (cnt*k + x)%M9
        # log(x, cnt)

    # cnt += 1brr[(len(brr)+1)//2:])
    if brr > arr[::-1]:
        # log(brr, arr)
        cnt += 1

    return cnt%M9


def solve_small(arr, k):

    arr = tuple(arr)

    cnt = 0
    for comb in itertools.product(range(k), repeat=len(arr)):
        if comb < arr and comb[::-1] == comb:
            cnt += 1
    
    return cnt%M9


if OFFLINE_TEST and False:

    k = 5
    for comb in itertools.product(range(k), repeat=7):
        res1 = solve_(comb, k)
        res2 = solve_small(comb, k)
        if res1 != res2:
            log(comb, res1, res2)
            assert False

    k = 5
    for comb in itertools.product(range(k), repeat=8):
        res1 = solve_(comb, k)
        res2 = solve_small(comb, k)
        assert res1 == res2




# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    n,k = list(map(int,input().split()))
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)
    abc = {x:i for i,x in enumerate("abcdefghijklmnopqrstuvwxyz", start=0)}
    arr = [abc[c] for c in srr]

    res = solve(arr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)