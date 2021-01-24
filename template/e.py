#!/usr/bin/env python3
import sys # , getpass
# import math, random
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
# OFFLINE_TEST = getpass.getuser() == "hkmac"
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

# ---------------------------- template ends here ----------------------------


def solve_(lst):
    # your solution here
    allnums = set(lst)

    if 0 not in allnums:
        return pow(2,len(lst)-1, 10**9+7)
    
    i = 0
    while i in allnums:
        i += 1
    mex = i

    ptr = 0
    c = collections.Counter()
    for ptr,x in enumerate(lst):
        if x < mex:
            c[x] += 1
        # log(len(c), x, c)
        if len(c) == mex:
            break
    
    # ptr += 1
    # mex_pointer = [-1 for _ in range(len(lst) + 1)]
    # mex_pointer[0] = ptr
    mex_pointer = [ptr+1]

    # log(mex, mex_pointer)

    for i,x in enumerate(lst, start=1):
        c[x] -= 1
        while x < mex and c[x] == 0:
            ptr += 1
            if ptr >= len(lst):
                break
            c[lst[ptr]] += 1
            # log(c)
        
        if ptr >= len(lst):
            break
        mex_pointer.append(ptr+1)

    # log(mex_pointer)
    # psum = [0 for _ in range(len(lst) + 1)]

    intervals = [[] for _ in range(len(lst) + 1)]
    
    for i,x in enumerate(mex_pointer):
        intervals[x].append(i)

    # log(intervals)

    psum = [0 for _ in range(len(lst) + 1)]

    for i,lst in enumerate(intervals[1:],start=1):
        psum[i] = psum[i-1]
        for x in lst:
            if x == 0:
                psum[i] += 1
            psum[i] += psum[x]
    
    # log(psum)

    return psum[-1]


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(lst)  # include input here
    
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