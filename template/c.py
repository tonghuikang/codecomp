#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly


# custom imports
# import pandas
# from sklearn.model_selection import train_test_split

# from scipy.optimize import linear_sum_assignment

# import torch
# import keras
# import tensorflow

# import lightgbm
# import xgboost


# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = True  # quora does not allow getpass
OFFLINE_TEST = False  # quora does not allow getpass
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

# hypothesis - checkboard is ok

def solve_(mrr, n):
    # your solution here
    mrr = [(a-1,b-1,c-1,d-1) for a,b,c,d in mrr]

    d = defaultdict(list)
    for x1,y1,x2,y2 in mrr:
        d[x1,y1].append((x2,y2))
        d[x2,y2].append((x1,y1))
    
    res = 0
    visited = set()

    for i in range(n):
        for j in range(n):
            if (i,j) in visited:
                continue
            odds = 0
            evens = 0
            stack = [(i,j)]
            visited.add((i,j))
            while stack:
                ci,cj = stack.pop()

                if (ci+cj) % 2 == 0:
                    evens += 1
                else:
                    odds += 1
                
                for ni,nj in d[ci,cj]:
                    if (ni,nj) in visited:
                        continue
                    visited.add((ni,nj))
                    stack.append((ni,nj))
            res += max(odds,evens)
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
    n,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr, n)  # include input here
    
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