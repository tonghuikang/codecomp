#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
from collections import defaultdict
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
    return [tuple(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(xrr, mrr, h, w):
    # your solution here

    flags = [0 for _ in range(w)]

    for row1,row2 in zip(xrr, xrr[1:]):
        for i,(a,b,c,d) in enumerate(zip(row1, row2, row1[1:], row2[1:]), start=1):
            if b == c == 1:
                flags[i] = 1

    psum = [0]
    for x in flags:
        psum.append(psum[-1] + x)

    log(flags)
    log(psum)

    res = []
    for a,b in mrr:
        val = psum[b] - psum[a]
        log(a,b,val)
        if val != 0:
            res.append("NO")
        else:
            res.append("YES")

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    h,w = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)
    xrr = read_strings(h)
    xrr = [[1 if cell == "X" else 0 for cell in row] for row in xrr]
    k = int(input())
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = [(x-1,y-1) for x,y in mrr]
    # mrr = minus_one_matrix(mrr)

    res = solve(xrr, mrr, h, w)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = "\n".join("NO" if x else "YES" for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
