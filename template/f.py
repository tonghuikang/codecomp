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
from statistics import stdev

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
    return [list(map(float,input().split())) for _ in range(rows)]


# ---------------------------- template ends here ----------------------------

# identify the worse, and flip back, and recaluate

def solve_(mrr, f, b):
    # your solution here

    ff = [b//8, b//8, b//8, b//8, b//8, b//16, b//16, b//16, b//16, b//16, b//16]
    ff.append(b-sum(ff))
    identified = set()
    # log(ff)

    for fff in ff:
        means = []
        sds = []
        for j in range(f):
            lst = [row[j] for row in mrr]
            sds.append(stdev(lst))
            means.append(sum(lst)/len(lst))

        losses = []
        for i,row in enumerate(mrr):
            loss = sum([(x-mean)**2/sd**2 for mean, sd, x in zip(means, sds, row)])
            losses.append((loss,i))
            
        losses = sorted(losses)[::-1]
        for loss,i in losses:
            if fff == 0:
                break
            if i in identified:
                continue
            identified.add(i)
            fff -= 1
            mrr[i] = mrr[i][::-1]

    return [i+1 for i in identified]


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
    n,f,b = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(n)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr, f, b)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print("\n".join(str(x) for x in res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)