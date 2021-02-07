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
    return [[x-1 for x in list(map(int,input().split()))] for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# ---------------------------- template ends here ----------------------------


def solve_(arr):
    # your solution here

    board = [[] for _ in range(7)]        

    def check(board):
        board = [col + [2]*(6-len(col)) for col in board]
        log(board)
        for col in board:
            for a,b,c,d in zip(col, col[1:], col[2:], col[3:]):
                if a == b == c == d != 2:
                    return a
        
        board_t = zip(*board)
        for row in board_t:
            for a,b,c,d in zip(row, row[1:], row[2:], row[3:]):
                if a == b == c == d != 2:
                    return a

        for row1,row2,row3,row4 in zip(board, board[1:], board[2:], board[3:]):
            for a,b,c,d in zip(row1, row2[1:], row3[2:], row4[3:]):
                if a == b == c == d != 2:
                    return a

        for row1,row2,row3,row4 in zip(board, board[1:], board[2:], board[3:]):
            for a,b,c,d in zip(row4, row3[1:], row2[2:], row1[3:]):
                if a == b == c == d != 2:
                    return a
        return 2

    current = 0
    for i,x in enumerate(arr):
        board[x].append(current)
        current = 1-current
        res = check(board)
        log(res)
        if res < 2:
            if res == 0:
                return "RED {}".format(i+1)
            return "YELLOW {}".format(i+1)

    return "DRAW"


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    arr = []
    for i in range(42):
        arr.append(int(input())-1)
    
    # read one line and parse each word as an integer
    # n,m = list(map(int,input().split()))
    # story_creator = []
    # for i in range(n):
    #     story_creator.append(int(input())-1)

    # p,q = list(map(int,input().split()))
    # user_follow_user = read_matrix(p)  # and return as a list of list of int
    # user_follow_story = read_matrix(q)  # and return as a list of list of int

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr)  # include input here
    
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