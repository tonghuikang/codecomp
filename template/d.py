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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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


def solve_(n, arr):
    # your solution here

    if arr == [0]:
        print(1, 1)
        print(1, 1)
        return

    if n == 1:
        print(arr[0], 0)
        return

    dp = [0 for _ in range(n+1)]
    prev = [-1 for _ in range(n+1)]

    # jump one to get value, or jump k to get square

    for cur in range(n):

        nex = cur + 1
        val = dp[cur] + arr[cur]

        if val > dp[nex]:
            dp[nex] = val
            prev[nex] = cur

        for nex in range(cur+1, n+1):
            dist = nex-cur
            val = dp[cur] + dist*dist

            if val > dp[nex]:
                dp[nex] = val
                prev[nex] = cur

    steps = [n]

    while steps[-1] != 0:
        steps.append(prev[steps[-1]])

    steps.reverse()

    def get_mex(l,r):
        mex = 0
        while mex in arr[l:r]:
            mex += 1
        return mex            

    res = []

    def execute(l,r):
        if l == r:
            return
        val = get_mex(l,r)
        for idx in range(l,r):
            arr[idx] = val
        res.append((l,r))
        # log(arr)

    def operate(l,r):
        if l >= r:
            return
        execute(l,r-1)
        operate(l, r-1)
        execute(l,r)
        operate(l, r-1)

    for a,b in zip(steps, steps[1:]):
        if b-a == 1:
            assert arr[a] >= 1
            continue
        else:
            if 0 in arr[a:b]:
                # make all not zero
                execute(a, b)
            # make all zero
            execute(a, b)
            # execute(a, b)
            # log(arr[a:b])
            # log("operate init", a, b)
            operate(a, b)
            execute(a, b)

    # log(dp)
    # log(steps)
    # log(arr)
            
    print(dp[-1], len(res))
    res = "\n".join(" ".join(str(x) for x in row) for row in res)
    print(res)
    assert dp[-1] == sum(arr)
    # return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):
    # read line as an integer
    n = int(input())
    # k = int(input())

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

    res = solve(n, arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
