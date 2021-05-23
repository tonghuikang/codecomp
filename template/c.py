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


def solve_(a,b):  # win, draw
    # your solution here

    if b == 0:
        return gen((0, 1, 9, 27, 23))
    if a/b == 10:
        return gen((1, 4, 15, 25, 15))
    if a/b == 2:
        return gen((1, 3, 8, 17, 20, 11))
    if a/b == 1:
        return "RPS"*20

    assert False

def gen(arr):
    rps = "RSP"
    srr = ""
    for i,x in enumerate(arr):
        srr += rps[i%3]*x
    return srr


def evaluate_2(res, frac):
    assert len(res) == 60
    score = 1/3 + frac/3
    rcount = 0
    pcount = 0
    scount = 0
    
    allcount = 1
    if res[0] == "R":
        pcount += 1
    if res[0] == "S":
        rcount += 1
    if res[0] == "P":
        scount += 1

    for x in res[1:]:
        if x == "R":
            score += (scount/allcount) + (rcount/allcount)*frac
            pcount += 1
        if x == "S":
            score += (pcount/allcount) + (scount/allcount)*frac
            rcount += 1
        if x == "P":
            score += (rcount/allcount) + (pcount/allcount)*frac
            scount += 1
        allcount += 1
    
    return score


if OFFLINE_TEST:
    best = 0
    best_idx = 0
    for i in range(60):
        for j in range(60-i):
            if j < i:
                continue
            for k in range(60-i-j):
                if k < j:
                    continue
                for l in range(60-i-j-k):
                    if l < k:
                        continue
                    for m in range(60-i-j-k-l):
                        for n in range(60-i-j-k-l-m):
                            o = 60-i-j-k-l-m-n
                            r00 = evaluate_2(gen((i, j, k, l, m, n, o)), 1)
                            if r00 > best:
                                best_idx = (i,j,k,l,m,n)
                                best = r00




cases = int(input())
target = int(input())
# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(cases):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    a,b = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(a,b)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)