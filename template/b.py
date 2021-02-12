#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------


def solve_(lst, qrr, k):
    # your solution here

    lst = [0] + lst + [k+1]

    count = []
    for a,b,c in zip(lst, lst[1:], lst[2:]):
        count.append(c - a - 2)
    
    psum = [0]
    cur = 0
    for a in count:
        cur += a
        psum.append(cur)

    # log(count)
    # log(psum)

    allres = []
    for l,r in qrr:
        x = lst[l+1] - 2
        y = k+1 - lst[r-1] - 2
        z = psum[r-1] - psum[l]
        # log(x,y,z)
        res = x + y + z
        allres.append(res)


    return allres


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
    n,q,k = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read multiple rows
    qrr = read_matrix(q)  # and return as a list of list of int
    # qrr = [(a-1, b-1) for a,b in qrr]
    # arr = read_strings(k)  # and return as a list of str

    res = solve(lst,qrr,k)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    print("\n".join(str(x) for x in res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)