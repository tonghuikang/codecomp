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
CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
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


def solve_(r,c,mrr):
    # your solution here

    zero_trees = sum(row.count("^") for row in mrr) == 0

    if zero_trees:
        return True, mrr

    if r == 1 or c == 1:
        return False, []

    mrr = [list(row) for row in mrr]

    visited = set()  # stoned
    stones = []
    for x in range(r):
        for y in range(c):
            if mrr[x][y] == "#":
                stones.append((x,y))
                visited.add((x,y))
    
    while stones:
        x,y = stones.pop()
        for dx,dy in d4:
            xx = x+dx
            yy = y+dy
            if 0 <= xx < r and 0 <= yy < c:
                if (xx,yy) in visited:
                    continue
                count = 0
                for dx2, dy2 in d4:
                    xx2 = xx+dx2
                    yy2 = yy+dy2
                    if 0 <= xx2 < r and 0 <= yy2 < c:
                        if not (mrr[xx2][yy2] == "#" or mrr[xx2][yy2] == "x"):
                            count += 1
                if count < 2:
                    stones.append((xx,yy))
                    visited.add((xx,yy))
                    if mrr[xx][yy] == "^":
                        return False, []
                    mrr[xx][yy] = "x"
                    
        
    mrr = ["".join(row).replace(".", "^").replace("x", ".") for row in mrr]
    return True, mrr


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
    r,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    mrr = read_strings(r)  # and return as a list of str
    # mrr = read_matrix(r)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    boo, res = solve(r,c,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    if boo:
        print("Case #{}: {}".format(case_num+1, "Possible"))   # Google and Facebook - case number required
    else:
        print("Case #{}: {}".format(case_num+1, "Impossible"))   # Google and Facebook - case number required
        continue

    print(res)
