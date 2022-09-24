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
        # log(*args)
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

abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}


def solve_(srr, qrr):
    # your solution here

    # srr = [abc_map[x] for x in srr]

    cur = defaultdict(int)
    dp = [tuple(cur)]
    for x in srr:
        cur[x] += 1
        dp.append(tuple(cur))
    
    res = 0
    for a,b in qrr:
        b += 1
        if (b-a)%2 == 0:
            # log(a,b,False)
            continue
        
        midleft = (a+b)//2
        midright = (a+b+1)//2
        # log(a,b,midleft,midright)

        left_count = [(y-x) for x,y in zip(dp[a], dp[midleft])]
        right_count = [(y-x) for x,y in zip(dp[midleft], dp[b])]

        # log(left_count)
        # log(right_count)

        extra_count = 0
        for x,y in zip(left_count, right_count):
            if x+1 == y:
                extra_count += 1
            elif x == y:
                continue
            else:
                break
        else:
            if extra_count == 1:
                res += 1
                continue
        # log(extra_count)

        left_count = [(y-x) for x,y in zip(dp[a], dp[midright])]
        right_count = [(y-x) for x,y in zip(dp[midright], dp[b])]

        # log(left_count)
        # log(right_count)

        extra_count = 0
        for x,y in zip(left_count, right_count):
            if x == y+1:
                extra_count += 1
            elif x == y:
                continue
            else:
                break
        else:
            if extra_count == 1:
                res += 1
                continue
        # log(extra_count)

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    srr = input().strip()

    k = int(input())
    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    qrr = read_matrix(k)  # and return as a list of list of int
    qrr = minus_one_matrix(qrr)
    log(len(srr), k)

    res = solve(srr, qrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
