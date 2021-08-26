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


def solve_(srr, qrr):
    # your solution here

    arr = [1 if x == "+" else -1 for x in srr]
    brr = [x if i%2 else -x for i,x in enumerate(arr)]

    log(brr)
    log(arr)

    psum = [0]
    for x in brr:
        psum.append(psum[-1] + x)

    log(psum)

    g = collections.defaultdict(list)
    for i,a in enumerate(psum):
        mid = a
        g[mid].append(i)

    # log(g)

    allres = []

    for a,b in qrr:
        # log("\n\n")
        a -= 1
        a0, b0 = a,b
        log(srr[a:b])

        res = []
        if psum[a] == psum[b]:
            allres.append(res)
            continue

        if (b-a)%2 == 0:
            res = [a+1]
            a += 1
            continue
        
        if (b-a)%2:
            if psum[b] < psum[a]:
                mid = (psum[a] + psum[b]) // 2
            else:
                mid = (psum[a] + psum[b] + 1) // 2
            idx = bisect.bisect_right(g[mid], b) - 1  # get index
            c = g[mid][idx]
            res.append(c)

            log(g[mid])
            log(a,b,c,mid,idx)
            log(psum[a:b+1])
            log(res)

            assert a < c <= b

        # res.append([-1,-2])

        flag = 1
        cnt = 0
        for i in range(a0,b0):
            if i+1 in res:
                continue
            cnt += arr[i] * flag
            flag = -flag
        assert cnt == 0

        allres.append(res)


    return allres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    _,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    srr = input().strip()

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    qrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, qrr)  # include input here

    # print length if applicable
    # print(len(res))

    strres = []

    for r in res:
        strres.append(str(len(r)))
        if r:
            strres.append(" ".join(str(x) for x in r)) 

    strres = "\n".join(strres)
    print(strres)