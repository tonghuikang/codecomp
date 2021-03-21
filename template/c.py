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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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


def solve_(mrr,h,w):
    # your solution here

    heap = []

    mrr = [[-1]*len(mrr[0])] + mrr + [[-1]*len(mrr[0])]
    mrr = [[-1] + row + [-1] for row in mrr]
    # log(mrr)

    for i,row in enumerate(mrr):
        for j,height in enumerate(row):
            heapq.heappush(heap, (-height,i,j))

    res = 0
    while heap:
        height,x,y = heapq.heappop(heap)
        height = -height
        if mrr[x][y] == -1:
            continue
        if mrr[x][y] != height:  # already addressed
            continue
        # log(height,x,y)
        for dx,dy in d4:
            xx = x+dx
            yy = y+dy
            adj = mrr[xx][yy]
            if adj == -1:
                continue
            if adj > height:
                continue
            if abs(height - adj) <= 1:
                continue
            adjnew = height - 1
            res += adjnew - adj
            heapq.heappush(heap, (-adjnew,xx,yy))
            mrr[xx][yy] = adjnew

        # log(mrr)

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
    h,w = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(h)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr,h,w)  # include input here
    
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