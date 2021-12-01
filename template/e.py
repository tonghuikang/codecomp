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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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


def solve_(arr, n, m, i, j, ress):
    # your solution here

    stack = [(i,j)]
    visited = set(stack)

    while stack:
        x,y = stack.pop()
        for dx,dy in d4:
            xx, yy = x+dx, y+dy
            log(xx,yy)
            if not (0 <= xx < n and 0 <= yy < m):
                continue
            if arr[xx][yy] != 0:
                continue
            if (xx,yy) in visited:
                continue
            cnt = 0
            for dx,dy in d4:
                xxx, yyy = xx+dx, yy+dy
                if not (0 <= xxx < n and 0 <= yyy < m):
                    continue
                if arr[xxx][yyy] == 0:
                    cnt += 1
            log(xx,yy,cnt)
            if cnt <= 2:
                stack.append((xx,yy))
                visited.add((xx,yy))
                ress[xx][yy] = "+"

    return ress


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
    n,m = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    mapp = {".":0, "#":1, "L":2}
    ress = []

    p,q = -1,-1
    mrr = []
    for i in range(n):
        row = input().strip()
        ress.append(list(row))
        row = [mapp[c] for c in row]
        for j,x in enumerate(row):
            if x == 2:
                p,q = i,j
                log(row)
                row[j] = 0
        mrr.append(row)

    # read multiple rows
    # arr = read_strings(n)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, n, m, p, q, ress)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join("".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
