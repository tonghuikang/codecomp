#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------


def butterfly(arr):
    MOD = 998244353
    sum_e = (911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 
             603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 
             510815449, 503497456, 743006876, 741047443, 56250497, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p] * now
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (l - r) % MOD
            now *= sum_e[(~s & -~s).bit_length() - 1]
            now %= MOD

def butterfly_inv(arr):
    MOD = 998244353
    sum_ie = (86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 
            90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 
            121186627, 608385704, 438932459, 359477183, 824071951, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1)[::-1]:
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p]
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (MOD + l - r) * inow % MOD
            inow *= sum_ie[(~s & -~s).bit_length() - 1]
            inow %= MOD

def convolution(a, b):
    # arrays might be in the wrong direction
    # https://www.hackerrank.com/contests/spring-2021-indeed-programming-challenge/challenges/power-connectors
    MOD = 998244353
    n = len(a)
    m = len(b)
    if not n or not m: return []
    if min(n, m) <= 50:
        if n < m:
            n, m = m, n
            a, b = b, a
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i + j] += a[i] * b[j]
                res[i + j] %= MOD
        return res
    z = 1 << (n + m - 2).bit_length()
    a += [0] * (z - n)
    b += [0] * (z - m)
    butterfly(a)
    butterfly(b)
    for i in range(z):
        a[i] *= b[i]
        a[i] %= MOD
    butterfly_inv(a)
    a = a[:n + m - 1]
    iz = pow(z, MOD - 2, MOD)
    for i in range(n + m - 1):
        a[i] *= iz
        a[i] %= MOD
    return a


def solve_(arr, brr):
    # if len(arr) == len(brr):
    #     return sum(a != b for a,b in zip(arr,brr))
    if len(brr) == 1:
        return 1-int(brr in arr)

    MOD = 998244353
    # your solution here
    arr = [1-2*int(x) for x in arr][::-1]
    brr = [1-2*int(x) for x in brr]

    crr = convolution(arr, brr)
    
    val = 3*10**6
    crr = [x-MOD if x > val else x for x in crr]

    prefix = len(brr) - 1
    relevant = crr[prefix:-prefix]

    best = max(relevant)

    # log(crr)
    # log(relevant)

    return (len(brr)-best)//2


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    arr = input().strip()
    brr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr, brr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)