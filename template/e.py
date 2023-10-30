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
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------


def ceiling_division(numer, denom):
    return -((-numer) // denom)


def solve_(n,k,arr):
    # your solution here

    if n == 1:
        return 0

    def gcd(a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        return math.gcd(a,b)

    brr = [1 if gcd(a,b) == 1 else 0 for a,b in zip(arr, arr[1:])]
    cursad = brr.count(1)
    log(brr)

    cur = []
    orr = []  # lengths of consecutive ones
    oorr = []  # both sides are ones
    oxrr = []  # one side is one
    xxrr = []  # both sides are not ones
    
    started_with_one = False
    prev = arr[0]

    if arr[0] == 1:
        one_count = 1
        curlen = 0
    else:
        one_count = 0
        curlen = 1

    for a,b in zip(arr, arr[1:]):

        if b == 1:
            if a == 1:
                one_count += 1
                continue
            else:
                if started_with_one:
                    oorr.append(curlen)
                else:
                    oxrr.append(curlen)
                one_count = 1
                curlen = 0
                continue

        if a == 1:
            started_with_one = True
            orr.append(one_count)
            one_count = 0
            curlen = 1
            continue
                
        if gcd(a,b) == 1:
            curlen += 1
        else:
            if started_with_one:
                oxrr.append(curlen)
            else:
                xxrr.append(curlen)
            started_with_one = False
            curlen = 1
    
    if curlen > 0:
        if started_with_one:
            oxrr.append(curlen)
        else:
            xxrr.append(curlen)
    
    if one_count > 0:
        orr.append(one_count)

    log(orr)
    log(oorr)
    log(oxrr)
    log(xxrr)

    avail = 0
    for x in xxrr:
        avail += ceiling_division(x, 2)

    k_used = min(avail, k)
    k -= k_used

    cursad -= k_used * 2

    return cursad


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
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

    res = solve(n,k,arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
