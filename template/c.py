#!/usr/bin/env python3
import sys
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
# import getpass  # not available on codechef
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


def calc_min_diff(comb):
    res = min(abs(b-a) for a,b in zip(comb, comb[1:]))
    res = min(res, abs(comb[0] - comb[-1]))
    return res


def solve_(arr):
    # your solution here


    idx = (len(arr) + 1) // 2

    left = arr[:idx]
    right = arr[idx:]

    left = left[::-1]
    right = right[::-1]

    # log(left)
    # log(right)

    res = []
    while left or right:
        if left:
            res.append(left.pop())
        if right:
            res.append(right.pop())

    maxval = calc_min_diff(res)
    maxret = res

    if len(arr)%2 == 1:
        return maxret

    k = len(arr) // 2

    mindiff = 10**18
    for a,b in zip(arr, arr[k-1:]):
        mindiff = min(mindiff, b-a)

    for i,(a,b) in enumerate(zip(arr, arr[k-1:])):
        if b-a == mindiff:
            break

    odds = arr[k:i+k] + arr[i:k][::-1]
    evens = [arr[2*k-1]] + arr[1:i] + [arr[0]] + arr[i+k:2*k-1][::-1]

    log(odds)
    log(evens)

    res = []
    for a,b in zip(odds, evens):
        res.append(b)
        res.append(a)

    val = calc_min_diff(res)
    if val > maxval:
        maxval = val
        maxret = res
        
    maxret_prev = maxret
    maxval_prev = maxval

    flag = False
    if len(arr) <= 6:
        for comb in itertools.permutations(arr):
            res = list(comb)

            val = calc_min_diff(res)
            if val > maxval:
                flag = True
                maxval = val
                maxret = res

        # return maxret

    if flag:
        log(maxret_prev)
        log(maxret)
        log(maxval_prev, maxval)
        assert False

    
    assert len(maxret) == len(arr)

    return maxret


if OFFLINE_TEST and False:
    length = random.randint(3,6)
    arr = [random.randint(0,10) for _ in range(length)]
    arr.sort()
    solve(arr)

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)
    arr.sort()

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
