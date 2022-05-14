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

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
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

# https://leetcode.com/problems/spiral-matrix-ii/
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
def generateMatrix(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A


def solve_(n,k):
    # your solution here
 
    if k < n-1:
        return "IMPOSSIBLE"
    if k%2:
        return "IMPOSSIBLE"

    matrix = generateMatrix(n)

    for row in matrix:
        log(row)

    shortcuts = {}
    val_to_xy = {}

    for x in range(n):
        for y in range(n):
            val_to_xy[matrix[x][y]] = (x,y)
            for dx,dy in d4:
                xx = x+dx
                yy = y+dy
                if 0 <= xx < n and 0 <= yy < n:
                    if matrix[xx][yy] - 1 > matrix[x][y]:
                        shortcuts[x,y] = (xx,yy)
                        # log(matrix[xx][yy], matrix[x][y])

    # log(shortcuts)
    res = []
    discount_needed = (n*n-1) - k
    cur = 1

    # log(discount_needed)

    while discount_needed > 0:
        x,y = val_to_xy[cur]
        if (x,y) not in shortcuts:
            # discount_needed -= 1
            cur += 1
            continue
        xx,yy = shortcuts[x,y]
        discount_offered = matrix[xx][yy] - matrix[x][y] - 1
        # log(cur, discount_offered, discount_needed)
        if discount_offered > discount_needed:
            cur += 1
            # discount_needed -= 1
            continue
        discount_needed -= discount_offered 
        res.append((matrix[x][y], matrix[xx][yy]))
        cur = matrix[xx][yy]

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,k)  # include input here

    if res == "IMPOSSIBLE":
        print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required
        continue

    # print length if applicable
    # print(len(res))
    print("Case #{}: {}".format(case_num+1, len(res)))   # Google and Facebook - case number required

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
