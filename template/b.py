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
d4 = [(0,1),(1,0),(0,-1),(-1,0)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
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


def solve_(n,m):

    # your solution here
    # https://leetcode.com/contest/weekly-contest-300/submissions/detail/737048620/
    matrix = [[-1 for _ in range(m)] for _ in range(n)]
    repeat = [0,1,1,0]

    for i in range(n):
        for j in range(m):
            if n <= m:
                if (j == 0):
                    matrix[i][j] = repeat[(i+j)%4]
            else:
                if (i == 0):
                    matrix[i][j] = repeat[(i+j)%4]

    sequence = []
    if m < n:
        for i in range(n):
            for j in range(m):
                sequence.append((i,j))
    else:
        for j in range(m):
            for i in range(n):
                sequence.append((i,j))

    # log(matrix)

    x,y = 0,0
    dd = 0
    
    visited = set()
    
    for x,y in sequence:
        diff_count = 0
        for dx2,dy2 in d4:
            xxx, yyy = x+dx2, y+dy2
            if not (0 <= xxx < n and 0 <= yyy < m):
                continue
            if matrix[xxx][yyy] != -1:
                if matrix[xxx][yyy] != matrix[x][y]:
                    diff_count += 1

        # log(x,y,diff_count)

        diff_count = int(diff_count < 2)
        for dx2,dy2 in d4:
            xxx, yyy = x+dx2, y+dy2
            if not (0 <= xxx < n and 0 <= yyy < m):
                continue
            if matrix[xxx][yyy] == -1:
                matrix[xxx][yyy] = (matrix[x][y] + diff_count)%2

        visited.add((x,y))
        dx,dy = d4[dd%4]
        xx, yy = x+dx, y+dy
        if ((xx,yy) in visited) or not (0 <= xx < m and 0 <= yy < n):
            dd += 1
            dx,dy = d4[dd%4]
            xx, yy = x+dx, y+dy
        x,y = xx,yy
        
    return matrix


# for n in range(2,50,2):
#     for m in range(2,50,2):
#         res = solve(n,m)
#         for x in range(n):
#             for y in range(m):
#                 count = 0
#                 for dx,dy in d4:
#                     xx, yy = x+dx, y+dy
#                     if not (0 <= xx < n and 0 <= yy < m):
#                         continue
#                     if res[xx][yy] != res[x][y]:
#                         count += 1
#                 assert count == 2, (n,m)


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
    n,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
