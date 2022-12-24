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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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


LARGE = 10**9

def solve_(h,w,mrr):
    # your solution here

    mrr = [[2]*w] + mrr + [[2]*w]

    # log(mrr)

    dp = [[LARGE, LARGE], [0, 1]]  # [p1_swapped][p2_swapped]
    for row1, row2, row3 in zip(mrr, mrr[1:], mrr[2:]):
        new_dp = [[LARGE, LARGE], [LARGE, LARGE]]

        for p1_swapped in [0,1]:
            if p1_swapped:
                arr = [1-x if x != 2 else x for x in row1]
            else:
                arr = [x for x in row1]

            for p2_swapped in [0,1]:
                if p2_swapped:
                    brr = [1-x if x != 2 else x for x in row2]
                else:
                    brr = [x for x in row2]
                
                for p3_swapped in [0,1]:
                    if p3_swapped:
                        crr = [1-x if x != 2 else x for x in row3]
                    else:
                        crr = [x for x in row3]
                        
                    qrr = [arr, brr, crr]
                        
                    # log()
                    # log(p1_swapped, p2_swapped,p3_swapped)
                    # for row in qrr:
                    #     log(row)

                    for j in range(w):
                        x, y = 1,j
                        flag = False
                        for dx,dy in d4:
                            xx = x+dx
                            yy = y+dy
                            if 0 <= yy < w:
                                if qrr[xx][yy] == 2:
                                    continue
                                if qrr[xx][yy] == qrr[x][y]:
                                    flag = True
                        if not flag:
                            break
                    else:
                        # log("ok")
                        new_dp[p2_swapped][p3_swapped] = min(
                            new_dp[p2_swapped][p3_swapped],
                            dp[p1_swapped][p2_swapped] + p3_swapped
                        )

        # log(new_dp)
        dp = new_dp

    res = min(min(row) for row in dp)
    if res == LARGE:
        return -1
    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    h,w = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(h)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(h,w,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
