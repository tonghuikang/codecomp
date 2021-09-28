#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(mrr, d):
    # your solution here
    h,w = len(mrr), len(mrr[0])
    mrr = [[int(cell == "*") for cell in row] for row in mrr]


    for i in range(h):
        for j in range(w):
            # check for candidature
            if mrr[i][j] > 0:

                x,y = i-1,j-1
                c = 0
                while x >= 0 and y >= 0:
                    if mrr[x][y] == 0:
                        break
                    c += 1
                    x -= 1
                    y -= 1
                if c < d:
                    continue

                x,y = i-1,j+1
                c = 0
                while x >= 0 and y < w:
                    if mrr[x][y] == 0:
                        break
                    c += 1
                    x -= 1
                    y += 1
                if c < d:
                    continue

                mrr[i][j] = 2

                x,y = i-1,j-1
                while x >= 0 and y >= 0:
                    if mrr[x][y] == 0:
                        break
                    mrr[x][y] = 2
                    x -= 1
                    y -= 1

                x,y = i-1,j+1
                while x >= 0 and y < w:
                    if mrr[x][y] == 0:
                        break
                    mrr[x][y] = 2
                    x -= 1
                    y += 1

    # for row in mrr:
    #     log(row)

    if sum(row.count(1) for row in mrr) == 0:
        return yes

    return no


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
    a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    mrr = read_strings(a)  # and return as a list of str
    # mrr = read_matrix(a)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, c)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
