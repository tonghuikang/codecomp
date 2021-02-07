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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = True  # quora does not allow getpass
# OFFLINE_TEST = False  # quora does not allow getpass
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
IMPOSSIBLE = "IMPOSSIBLE"


def solve_(arr):
    n = len(arr)
    ways = [[1 if i == 0 or j == 0 else 0 for j,_ in enumerate(row)] for i,row in enumerate(arr)]

    value = [[0 for _ in row] for row in arr]

    cur = 0
    for i in range(n):
        cur += arr[0][i]
        value[0][i] += cur

    cur = 0
    for i in range(n):
        cur += arr[i][0]
        value[i][0] += cur

    # log(value)

    for i in range(1,n):
        for j in range(1,n):
            if value[i-1][j] == value[i][j-1]:
                ways[i][j] = ways[i-1][j] + ways[i][j-1]
                value[i][j] = arr[i][j] + value[i][j-1]

            if value[i-1][j] > value[i][j-1]:
                ways[i][j] = ways[i-1][j]
                value[i][j] = arr[i][j] + value[i-1][j]

            if value[i-1][j] < value[i][j-1]:
                ways[i][j] = ways[i][j-1]
                value[i][j] = arr[i][j] + value[i][j-1]
            ways[i][j] = ways[i][j]%M9

    return value[-1][-1], ways[-1][-1]


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # n,m,g = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # arr = read_strings(n)  # and return as a list of str
    # arr = [list(row) for row in arr]
    guards = read_strings(k)  # and return as a list of list of int
    guards = [[int(x) for x in row] for row in guards]
    # guards = [(y-1, x-1, d) for x,y,d in guards]

    res = solve(guards)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(*res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)