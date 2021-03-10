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


def solve_(mrr):
    # every thrid row, starting from
        # the second row
        # the first row if if col%3 == 1

    # connect the columns

    row_to_list = defaultdict(list)

    for i,row in enumerate(mrr):
        for j,cell in enumerate(row):
            if cell == "X":
                row_to_list[i].append(j)

    xrr = [list(row) for row in mrr]

    if len(xrr[0]) <= 2 and len(xrr) <= 2:
        return xrr

    offset = 1
    if len(xrr)%3 == 1:
        offset = 0
    allpillars = []

    for i,row in enumerate(xrr):
        if i%3 == offset:
            xrr[i] = ["X"]*len(xrr[0])
            allpillars.append(i)
        else:
            if i == 0 or i == len(xrr)-1:
                continue                

    for a,b in zip(allpillars, allpillars[:-1]):
        if row_to_list[a+1]:
            xrr[a+2][row_to_list[a+1][0]] = "X"
        elif row_to_list[b-1]:
            xrr[b-2][row_to_list[b-1][0]] = "X"
        else:
            xrr[a+1][0] = "X"
            xrr[b-1][0] = "X"

    return xrr


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
    k,_ = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    arr = read_strings(k)  # and return as a list of str

    res = solve(arr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))
    res = "\n".join(["".join(r) for r in res])
    print(res)
    # Other platforms - no case number required
    # print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print("".join(r))