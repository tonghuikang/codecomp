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


def solve_(arr, guards, n, m):
    # your solution here

    psum = [[0 for _ in row] for row in arr]

    for x,y,d in guards:
        for yy in range(max(0, y-d),min(n, y+d+1)):
            xrange = d-abs(yy-y)
            psum[yy][max(0,x-xrange)] += 1
            psum[yy][min(m-1,x+xrange+1)] -= 1

    # for row in psum:
    #     log(" ".join(str(x) for x in row))

    start_point = None
    end_point = None
    for i,prow in enumerate(psum):
        cur = 0
        for j,p in enumerate(prow):
            cur += p
            if arr[i][j] == "E":
                start_point = (i,j)
            elif arr[i][j] == "S":
                end_point = (i,j)
            if cur > 0:
                # log(i,j)
                arr[i][j] = "#"
                # log(arr[i][j])

    log(start_point, end_point)
    for row in arr:
        log("".join(row))

    if arr[start_point[0]][start_point[1]] == "#":
        return IMPOSSIBLE

    if arr[end_point[0]][end_point[1]] == "#":
        return IMPOSSIBLE

    visited = {}
    visited[start_point] = 0
    stack = deque([start_point])
    while stack:
        x,y = stack.popleft()
        for dx,dy in d4:
            xx,yy = x+dx, y+dy
            if (xx,yy) in visited:
                continue
            if arr[xx][yy] == "#":
                continue
            visited[xx,yy] = visited[x,y] + 1
            stack.append((xx,yy))

    if end_point not in visited:
        return IMPOSSIBLE
    return visited[end_point]


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
    n,m,g = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    arr = read_strings(n)  # and return as a list of str
    arr = [list(row) for row in arr]
    guards = read_matrix(g)  # and return as a list of list of int
    guards = [(y-1, x-1, d) for x,y,d in guards]

    res = solve(arr, guards, n, m)  # include input here
    
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