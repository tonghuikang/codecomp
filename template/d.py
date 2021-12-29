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

M9 = 998244353
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

LARGE = 10**4
p = 998244353
factorial_mod_p = [1 for _ in range(LARGE)]
for i in range(1,LARGE):
    factorial_mod_p[i] = (factorial_mod_p[i-1]*i)%p


def ncr_mod_p(n, r, p=p):
    num = factorial_mod_p[n]
    dem = factorial_mod_p[r]*factorial_mod_p[n-r]
    return (num * pow(dem, p-2, p))%p



def solve_(srr, n, k):
    # your solution here

    if k == 0:
        return 1

    if srr.count("1") < k:
        return 1

    if k < 0:
        return 0

    res = 0

    start = [0]
    ends = []

    for i,x in enumerate(srr):
        if x == "1":
            start.append(i+1)
            ends.append(i)

    ends.append(n)

    res = 0

    intervals = []
    starting = True
    for a,b,c in zip(start, ends[k:], ends[k-1:]):
        val = ncr_mod_p(b-a, k) - ncr_mod_p(c-a, k-1)
        if starting:
            val += ncr_mod_p(c-a, k-1)
            starting = False

        log(a,b,val)
        res += val
        intervals.append([a,b])

    log(k, intervals, res)

    return res%998244353

# def solve_(srr, n, k):

#     if k == 0:
#         return 1

#     if srr.count("1") < k:
#         return 1

#     flag = 1
#     res = 0
#     for k2 in range(k,-1,-1):
#         res += flag * solve_two(srr, n, k2)
#         flag = -flag

    # return res



    # for i,(a,b) in enumerate(second_intervals):
    #     for c,d in second_intervals[i+1:]:
    #         # if c >= b:
    #         #     break
    #         overlap_length = b - c
    #         overlap_count = psum[b] - psum[c]
    #         val = ncr_mod_p(overlap_length, overlap_count)
    #         # second_intervals.append([c,b])
    #         log(a,b,c,d, "|", overlap_length, overlap_count, val)
    #         res += val
    psum = [0]
    for x in srr:
        if x == "1":
            psum.append(psum[-1] + 1)
        else:
            psum.append(psum[-1])

    # log(psum)
    # log(intervals)

    # second_intervals = []

    def flag(x):
        if (k-x)%2:
            return -1
        return 1

    for i,(a,b) in enumerate(intervals):
        for c,d in intervals[i+1:]:
            if a == c:
                continue
            # if c >= b:
            #     break
            overlap_length = b - c
            overlap_count = psum[b] - psum[c]
            val = ncr_mod_p(overlap_length, overlap_count)
            # second_intervals.append([c,b])
            log(a,b,c,d, "|", overlap_length, overlap_count, val)

            if overlap_count == 0:
                continue

            res += flag(overlap_count) * val


    log(k, res)
    return res%M9


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    n, k = list(map(int,input().split()))
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, n, k)  # include input here

    # if OFFLINE_TEST:
    #     assert solve_(srr, n, k) == solve_(srr[::-1], n, k)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
