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


def solve_(arr, brr):
    # your solution here

    val = 1
    crr = []
    for a in arr[::-1]:
        crr.append((int(a)*val)%7)
        val = (val*10)%7
    crr = crr[::-1]

    # log(crr)

    crr = crr[::-1]
    brr = brr[::-1]

    twin = set([0])
    awin = set([])
    allset = set(range(7))
    prevt = True
    for b,c in zip(brr, crr):
        # log(b,c)
        if b == "T":
            if not prevt:
                twin = allset - awin
            twin_new = set()
            for x in twin:
                twin_new.add(x)
                twin_new.add((x+c)%7)
            twin = twin_new
            if len(twin) == 7:
                return "Takahashi"
            prevt = True
        else:
            if prevt:
                awin = allset - twin
            awin_new = set()
            for x in awin:
                awin_new.add(x)
                awin_new.add((x+c)%7)
            awin = awin_new
            if len(awin) == 7:
                return "Aoki"
            prevt = False
    #     log(twin)
    #     log(awin)

    # log(twin, awin, prevt)
    if prevt:
        if 0 in twin:
            return "Takahashi"
        return "Aoki"
    if not prevt:
        if 0 in awin:
            return "Aoki"
        return "Takahashi"



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    arr = input().strip()
    brr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr, brr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)