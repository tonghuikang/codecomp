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


def solve_(mrr, h, w):
    # your solution here

    up = [[0 for _ in row] for row in mrr]
    down = [[0 for _ in row] for row in mrr]
    left = [[0 for _ in row] for row in mrr]
    right = [[0 for _ in row] for row in mrr]

    for i,row in enumerate(mrr):
        curleft = 0
        for j,cell in enumerate(row):
            if cell:
                curleft += 1
                left[i][j] = curleft
            else:
                curleft = 0

        curright = 0
        for j,cell in list(enumerate(row))[::-1]:
            if cell:
                curright += 1
                right[i][j] = curright
            else:
                curright = 0

    for j in range(w):
        curdown = 0
        for i in range(h):
            if mrr[i][j]:
                curdown += 1
                down[i][j] = curdown
            else:
                curdown = 0

    for j in range(w):
        curup = 0
        for i in range(h-1,-1,-1):
            if mrr[i][j]:
                curup += 1
                up[i][j] = curup
            else:
                curup = 0

    # for row in up:
    #     print(*row)
    # print()

    # for row in down:
    #     print(*row)
    # print()

    # for row in left:
    #     print(*row)
    # print()

    # for row in right:
    #     print(*row)
    # print()

    res = 0
    for i in range(h):
        for j in range(w):
            if not mrr[i][j]:
                continue
            a,b,c,d = up[i][j], left[i][j], down[i][j], right[i][j]
            val = 0
            for x,y in zip([a,b,c,d],[b,c,d,a]):
                p = x//2
                q = y
                val += max(0,min(p,q)-1)
                p = y//2
                q = x
                val += max(0,min(p,q)-1)
            # print(i,j,x,y,val)
            res += val

    return res



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    k,l = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr, k, l)  # include input here
    
    # print result
    # Google and Facebook - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)