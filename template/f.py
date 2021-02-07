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
# from statistics import stdev

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


# ---------------------------- template ends here ----------------------------

# identify the worse, and flip back, and recaluate

def solve_(mrr):
    # your solution here
    middle2both = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int)))))
    middle2left = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    middle2right = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    middle = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    before = defaultdict(lambda: defaultdict(int))
    after = defaultdict(lambda: defaultdict(int))
    before2 = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    after2 = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for line in mrr:
        for a,b,c in zip(line, line[1:], line[2:]):
            if b != -1:
                middle[a][c][b] += 520000
            if c != -1:
                before2[a][b][c] += 5000
            if a != -1:
                after2[b][c][a] += 6000
        for a,b in zip(line, line[1:]):
            if a != -1:
                before[b][a] += 4
            if b != -1:
                after[a][b] += 5
        for a,b,c,d,e in zip(line, line[1:], line[2:], line[3:], line[4:]):
            if c != -1:
                middle2left[a][b][d][c] += 1100000
                middle2right[b][d][e][c] += 1000000
                middle2both[a][b][d][e][c] += 10000000

    res = []
    for line in mrr:
        for x,a,b,c,y in zip(line, line[1:], line[2:], line[3:], line[4:]):
            counter = Counter()
            if b == -1:
                # print(a,b,c)
                # log(before[c], after[a], middle[a][c])
                counter += before[c]
                counter += after[a]
                counter += middle[a][c]
                counter += before2[x][a]
                counter += after2[c][y]
                counter += middle2left[x][a][c]
                counter += middle2right[a][c][y]
                counter += middle2both[x][a][c][y]
                # print(counter.most_common())
                k,v = counter.most_common()[0]
                res.append(k)

    # print(middle[2][5])
    return res


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
    # k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str
    mrr = [[0,0] + line + [0,0] for line in mrr]

    res = solve(mrr)  # include input here
    
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