#!/usr/bin/env python3
import sys
from collections import Counter
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
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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

import itertools

def solve_brute_force(arr):
    maxres = 0
    for pdt1 in itertools.product([0,1], repeat=len(arr)):
        if sum(pdt1) == 0:
            continue
        for pdt2 in itertools.product([0,1], repeat=len(arr)):
            if sum(pdt2) == 0:
                continue
            for a,b in zip(pdt1, pdt2):
                if a == b == 1:
                    continue
                xrr = [x for x,y in zip(arr,pdt1) if y == 1]
                yrr = [x for x,y in zip(arr,pdt2) if y == 1]
                zrr = [x for x,y,z in zip(arr,pdt1,pdt2) if y == 0 and z == 0]

                if len(zrr) == 0:
                    continue

                w1 = 10**18
                for x in xrr:
                    for y in yrr:
                        w1 = min(w1, abs(x-y))
                w2 = 10**18
                for x in xrr:
                    for y in zrr:
                        w2 = min(w2, abs(x-y))
                res = w1 + w2
                maxres = max(maxres, res)

    # log(maxres)
    return maxres



def solve_(arr):
    # your solution here

    maxres = 0

    for a,b in zip(arr, arr[1:]):
        res = b-a + arr[-1] - a
        maxres = max(maxres, res)

        res = b-a + b - arr[0]
        maxres = max(maxres, res)

    return maxres


# import random
# while True:
#     arr = [random.randint(1, 10) for x in range(random.randint(3,4))]
#     arr.sort()
#     log(arr, solve_(arr), solve_brute_force(arr))
#     assert solve_(arr) == solve_brute_force(arr)


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
    arr.sort()
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)
    res = solve(arr)  # include input here

    # if OFFLINE_TEST:
    #     assert solve(arr) == solve_brute_force(arr)
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
