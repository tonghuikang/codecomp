#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import heapq
import time
from collections import defaultdict
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
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x-1 for x in arr]


def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(arr, target):
    # https://codingcompetitions.withgoogle.com/kickstart/submissions/00000000004362d6/WU1TZWFo

    # your solution here
    b = arr
    k = target

    if k in b:
        return 1

    p = b.copy()
    for i in range(1, n):
        p[i] += p[i-1]

    def getRangeSum(l, r):
        if l-1 >= 0:
            return p[r]-p[l-1]
        else:
            return p[r]

    inf = 10**6
    ans = inf
    # leftMinLen=defaultdict(lambda:inf) # leftMinLen[length]=minimum length on left
    leftMinLen = [inf]*(k+1)

    for r1 in range(n):
        # print('r1:{} leftMinLen:{}'.format(r1,leftMinLen))
        rightSum = 0
        rightLen = 0
        for r2 in range(r1, n):
            rightSum += b[r2]
            rightLen += 1
            leftTarget = k-rightSum
            if leftTarget < 0:
                break
            ans = min(ans, rightLen+leftMinLen[leftTarget])
        l2 = r1
        for l1 in range(l2+1):
            leftLen = l2-l1+1
            leftSum = getRangeSum(l1, l2)
            if leftSum <= k:
                leftMinLen[leftSum] = min(leftMinLen[leftSum], leftLen)

    if ans == inf:
        ans = -1

    return ans


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
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # Google and Facebook - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # print(res)
