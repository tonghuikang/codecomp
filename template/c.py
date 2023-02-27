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


def solve_(srr):
    # your solution here
    n = len(srr)

    srr = sorted(list(srr), reverse=True)

    c = sorted(Counter(list(srr)).items())

    # log(c)

    left = []
    right = []
    allres = []
    hold = None

    for i,(k,v) in enumerate(c):
        num_pairs = v // 2
        for _ in range(num_pairs):
            left.append(k)
            right.append(k)

        # log(left)
        # log(right)
        # log()

        if v%2 and hold is not None:
            # log("check")
            left.append(k)
            for (k2,v2) in (c[i+1:]):
                for _ in range(v2):
                    left.append(k2)
            right.append(hold)
            # log(left)
            # log(right)
            # log()
            break

        if v%2 and hold is None:
            hold = k
            # for (_,v2) in (c[i+1:]):
            #     if v2%2:
            #         break
            # else:
            #     for (k2,v2) in (c[i+1:]):
            #         for _ in range(v2//2):
            #             left2.append(k2)
            #             right2.append(k2)
            #     right2.append(k)
            #     res2 = left2 + right2[::-1]

        if hold is not None:
            left2 = [x for x in left]
            right2 = [x for x in right]
            for (k,v) in (c[i+1:]):
                for _ in range(v):
                    left2.append(k)
            right2.append(hold)
            res2 = left2 + right2[::-1]
            # log("check", res2, left2, right2, len(res2), n)
            assert len(res2) == n
            allres.append(res2)

    else:
        if hold is not None:
            right.append(hold)

    res2 = left + right[::-1]
    # log(res2)
    assert len(res2) == n
    allres.append(res2)
    return "".join(min(allres))


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
