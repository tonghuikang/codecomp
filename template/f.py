#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# import io, os  # if all integers, otherwise need to post process
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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

def read_matrix(nrows):
    return [list(map(int,input().split())) for _ in range(nrows)]

def read_matrix_and_flatten(nrows):
    return [int(x) for i in range(nrows) for x in input().split()]

def read_strings(nrows):
    return [input().strip() for _ in range(nrows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------

def isBipartite(edges) -> bool:
    g = defaultdict(set)
    for cur,nex in edges:
        g[cur].add(nex)
        g[nex].add(cur)

    colored = {}  # and visited

    for start in g:
        if start in colored:
            continue
        stack = [(start,True)]
        colored[start] = True

        while stack:
            cur, color = stack.pop()
            for nex in g[cur]:
                if nex in colored:
                    if colored[nex] == color:
                        return False
                    continue
                stack.append((nex, not color))
                colored[nex] = not color

    return True

def solve_(arr,h,w):
    # your solution here
    res = [[0 for _ in row] for row in arr]

    edges = []
    diamonds = []

    for x,row in enumerate(arr):
        for y,cell in enumerate(row):
            if cell == 1:
                adj = []
                for dx,dy in d4:
                    xx,yy = x+dx, y+dy
                    if 0 <= xx < h and 0 <= yy < w:
                        if arr[xx][yy] == 0:
                            adj.append((xx,yy))
                if len(adj)%2 != 0:
                    return -1
                if len(adj) == 2:
                    edges.append(adj)
                if len(adj) == 4:
                    diamonds.append(adj)
                res[x][y] = len(adj)//2 * 5

    if not isBipartite(edges):
        return -1

    log(edges)
    log(diamonds)

    return res


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
    h,w = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    arr = read_strings(h)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    arr = [[1 if c == "X" else 0 for c in row] for row in arr]

    res = solve(arr,h,w)  # include input here

    # print length if applicable
    # print(len(res))
    log("res", res)

    if res == -1:
        print(no)
        continue
    print(yes)

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)