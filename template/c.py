#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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


def solve_(mrr, n):
    # your solution here

    nrr = [[1 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i,n):
            nrr[i][j] = mrr[i][j-i]

    for i in range(n):
        if nrr[i][i] == 2:
            log("edge not 1")
            return 0
        nrr[i][i] = 1

    for i in range(n):
        for j in range(i,n):
            if nrr[i][j] == 1:
                for x in range(i,n):
                    for y in range(j+1):
                        if nrr[x][y] == 2:
                            log("inner not 1")
                            return 0
                        nrr[x][y] = 1

            if nrr[i][j] == 2:
                for x in range(i+1):
                    for y in range(j,n):
                        if nrr[x][y] == 1:
                            log("inner not 2")
                            return 0
                        nrr[x][y] = 2

    # log("\n" + "\n".join("".join(map(str, row)) for row in nrr))
    # log()
    
    for i in range(2,n):
        sx, sy = 0, i
        for j in range(n-i):
            x, y = sx + j, sy + j
            log(x,y)
            if nrr[x+1][y] == 1 and nrr[x][y-1] == 1:
                if nrr[x][y] == 2:
                    log("12")
                    log("01")
                    return 0
                nrr[x][y] = 1

    # log("\n" + "\n".join("".join(map(str, row)) for row in nrr))
    # log()

    dp1 = [[1 for _ in range(n)] for _ in range(n)]  # could be same or different
    dp2 = [[1 for _ in range(n)] for _ in range(n)]  # must be different

    for i in range(n):
        dp1[i][i] = 2
        dp2[i][i] = 0

    # log("\n" + "\n".join("".join(map(str, row)) for row in res))

    for i in range(1,n):
        sx, sy = 0, i
        for j in range(n-i):
            x, y = sx + j, sy + j
            log(x,y)
            # log("\n" + "\n".join("".join(map(str, row)) for row in res))
            log()

            if nrr[x][y] == 1:
                dp1[x][y] = 2
                dp2[x][y] = 0
                continue
            if nrr[x][y] == 2:
                dp2[x][y] = dp2[x+1][y-1] - dp1[x+1][y-1]
                dp1[x][y] = dp2[x][y]  # must be different
                continue
            if nrr[x][y] == 0:
                res[x][y] = res[x+1][y] * res[x][y-1] // res[x+1][y-1]
                continue


    return res[0][-1] % m9


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
