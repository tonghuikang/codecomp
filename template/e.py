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


def solve_(arr,roads,queries):  # tourism
    # your solution here

    d = defaultdict(list)
    for a,b,c in roads:
        d[a].append((b,c))
        d[b].append((a,c))

    for start,end in queries:
        result = [0 for _ in arr]
        visited = set([start])
        stack = [(arr[start],start)]
        while stack:
            # log(stack)
            holding,cur = stack.pop()
            for nex,toll in d[cur]:
                if nex in visited:
                    continue
                visited.add(nex)
                stack.append((holding - toll + arr[nex], nex))
                result[nex] = max(0, result[cur], toll-holding)
        # log(start, result)
        print(result[end])

    return ""


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
    n,q = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    # read multiple rows
    roads = read_matrix(n-1)  # and return as a list of list of int
    queries = read_matrix(q)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str
    roads = [(a-1,b-1,c) for a,b,c in roads]
    queries = [(a-1,b-1) for a,b in queries]
    res = solve(arr,roads,queries)  # include input here
    
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