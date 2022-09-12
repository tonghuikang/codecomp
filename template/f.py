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


def solve_(srr, w, m, mrr):
    # your solution here

    psum = [0]
    for x in srr:
        psum.append(psum[-1] + x)
    
    res = defaultdict(list)
    for i,(a,b) in enumerate(zip(psum, psum[w:])):
        res[(b-a)%9].append(i+1)

    for x in res:
        res[x] = res[x][:2]
    
    # log(res)

    ret = []
    for l,r,k in mrr:
        x = (psum[r] - psum[l-1])%9
        # ix + j = k (mod 9)
        candidates = []
        for i in range(9):
            if i not in res:
                continue
            l1 = res[i][0]
            for j in range(9):
                if j not in res:
                    continue
                if (i*x + j)%9 == k:
                    if i == j:
                        if len(res[j]) == 1:
                            continue
                        l2 = res[j][1]
                    else:
                        l2 = res[j][0]
                    candidates.append((l1,l2))
        if not candidates:
            ret.append((-1,-1))
        else:
            ret.append(min(candidates))

    return ret


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    srr = input().strip()
    srr = [int(x) for x in srr]

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    w,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, w, m, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
