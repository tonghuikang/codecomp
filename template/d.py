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


def solve_(num_columns, row_divider, col_divider, employees):  # swapped
    # your solution here
    employee_location = defaultdict(set)

    for row,col in employees:
        employee_location[col].add(row)

    minres = 0
    for comb_row in itertools.product([0,1], repeat=num_columns*2):
        for comb_col in itertools.product([0,1], repeat=(num_columns-1)*3):
            res = 0
            # g = defaultdict(list)
            # for i,x in enumerate(comb_row[0::2]):
            #     if x == 1:
            #         res += col_divider[0][i]
            #         g[i,0].append((i,1))
            #         g[i,1].append((i,0))
            # for i,x in enumerate(comb_row[1::2]):
            #     if x == 1:
            #         res += col_divider[1][i]

            for i,x in enumerate(comb_row[0::3]):
                if x == 1:
                    res += row_divider[0][i]
            for i,x in enumerate(comb_row[1::3]):
                if x == 1:
                    res += row_divider[1][i]
            for i,x in enumerate(comb_row[2::3]):
                if x == 1:
                    res += row_divider[2][i]
        
        pass

    log(employee_location)


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
    num_columns, num_employees = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    col_divider = read_matrix(3)  # and return as a list of list of int
    row_divider = read_matrix(2)  # and return as a list of list of int
    employees = read_matrix(num_employees)  # and return as a list of str
    employees = [(a-1,b-1) for a,b in employees]
    res = solve(num_columns, col_divider, row_divider, employees)  # include input here
    
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