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


p = 998244353

qrr = [1 for _ in range(2*10**5 + 10)]
val = 1
for i in range(1,2*10**5 + 5):
    val = (val*i)%p
    qrr[i] = val

def factorial_mod_p(n, p):
    return qrr[n]

@functools.lru_cache(maxsize=2*10**5 + 10)
def ncr_mod_p(n, r, p):
    num = factorial_mod_p(n, p)
    dem = factorial_mod_p(r, p)*factorial_mod_p(n-r, p)
    return (num * pow(dem, p-2, p))%p

p = 998244353
factorial_mod_p(2*10**5+1, p)


def solve_(arr):
    # your solution here
    p = 998244353

    if len(arr) == 1:
        return 1

    c = Counter(arr)
    maxarr = max(c)
    if c[maxarr] > 1:
        return factorial_mod_p(len(arr), p)

    if c[maxarr-1] == 0:
        return 0

    k = c[maxarr-1]
    r = len(arr) - k - 1

    # (k+1)! - k!
    # r!
    # r+k+2 C k+1

    a = factorial_mod_p(k+1, p) - factorial_mod_p(k, p)
    b = factorial_mod_p(r, p)
    c = ncr_mod_p(r+k+1, k+1, p)

    log(k,r,a,b,c)

    return (a*b*c)%p


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)