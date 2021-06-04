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


def solve_(srr, qrr, k):
    # your solution here

    mappping = {"?": 2, "1": 1, "0":0}
    status = [mappping[x] for x in srr]
    counts = [1 for _ in srr]  # result at -1
    nextidx = [-1 for _ in srr]
    prevsmall_arr = [-1 for _ in srr]
    prevlarge_arr = [-1 for _ in srr]

    idx = 0
    
    for j in range(k-1,-1,-1):
        prevsize = 2**(j+1)
        startidx = idx
        for i in range(2**j):
            if j == k-1:
                if status[idx] == 2:
                    counts[idx] = 2
            else:
                prevsmall = startidx - prevsize + (idx - startidx)*2
                prevlarge = prevsmall + 1
                nextidx[prevsmall] = idx
                nextidx[prevlarge] = idx
                prevsmall_arr[idx] = prevsmall
                prevlarge_arr[idx] = prevlarge
                # log(idx, prevsmall, prevlarge)

                if status[idx] == 0:
                    counts[idx] = counts[prevsmall]
                if status[idx] == 1:
                    counts[idx] = counts[prevlarge]
                if status[idx] == 2:
                    counts[idx] = counts[prevsmall] + counts[prevlarge]
                
            idx += 1

    # log("chec")
    # log(prevsmall_arr)
    # log(prevlarge_arr)
    # log(nextidx)

    res = []
    for row in qrr:
        idx, op = row.split()
        idx = int(idx)-1
        op = mappping[op]

        status[idx] = op

        if idx < 2**(k-1):
            # log("smaller than 2**k-1", 2**(k-1))
            if status[idx] == 0:
                counts[idx] = 1
            if status[idx] == 1:
                counts[idx] = 1
            if status[idx] == 2:
                counts[idx] = 2
        else:
            prevsmall = prevsmall_arr[idx]
            prevlarge = prevlarge_arr[idx]
            if status[idx] == 0:
                counts[idx] = counts[prevsmall]
            if status[idx] == 1:
                counts[idx] = counts[prevlarge]
            if status[idx] == 2:
                counts[idx] = counts[prevsmall] + counts[prevlarge]

        while nextidx[idx] != -1:
            idx = nextidx[idx]
            prevsmall = prevsmall_arr[idx]
            prevlarge = prevlarge_arr[idx]
            if status[idx] == 0:
                counts[idx] = counts[prevsmall]
            if status[idx] == 1:
                counts[idx] = counts[prevlarge]
            if status[idx] == 2:
                counts[idx] = counts[prevsmall] + counts[prevlarge]
        # log("-")
        # log(status)
        # log(counts)
        res.append(counts[-1])
    
    # log(res)
    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    srr = input().strip()

    q = int(input())

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    qrr = read_strings(q)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, qrr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)