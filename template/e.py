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


def solve_(anc, qrr, k):
    # your solution here
    
    decs = [[[] for _ in range(18)] for _ in range(k)]
    ancs = [[-1]*18 for _ in range(k)]
    depth = [0]*k

    for i,a in enumerate(anc, start=1):
        d = depth[a] + 1
        depth[i] = d
        ancs[i][0] = a
        decs[a][0].append(i)
        cur = a
        for j in range(1,19):
            cur = ancs[cur][j-1]
            if cur == -1:
                break
            ancs[i][j] = cur
            decs[cur][j].append(i)

    tails = [-1]*k 

    for i in range(k-1,-1,-1):
        if tails[i] != -1:
            continue
        cur = i
        cnt = 0
        while True:
            tails[cur] = cnt
            cnt += 1
            cur = ancs[cur][0]
            if cur == -1:
                break
            if tails[cur] != -1:
                tails[cur] = -2
                break

    # log(tails)

    # log(depth)
    # log(decs)
    # log(ancs)

    res = []

    for u,d in qrr:
        # log()
        # log(u,d)
        u -= 1
        if depth[u] > d:
            # log("-0-")
            res.append(0)
            continue
        if depth[u] == d:
            # log("-1-")
            res.append(1)
            continue
        down = d - depth[u]
        bins = [i for i in range(18) if (1<<i)&down]

        stack = [u]
        remaining = down

        val = 0
        for idx in bins[:-1]:
            remaining -= 2**idx
            new_stack = []
            for node in stack:
                for nex in decs[node][idx]:
                    if tails[nex] > 0:
                        if tails[nex] >= remaining:
                            log("skip")
                            val += 1
                    else:
                        new_stack.append(nex)
            stack = new_stack
            # log(stack)
        final = bins[-1]
        val += sum([len(decs[node][final]) for node in stack])
        res.append(val)


    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    anc = list(map(int,input().split()))
    anc = minus_one(anc)

    # read multiple rows
    q = int(input())
    # arr = read_strings(k)  # and return as a list of str
    qrr = read_matrix(q)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(anc, qrr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)