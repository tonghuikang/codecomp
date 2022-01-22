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

# average of all next outcomes

LARGE = 2010
dp = {}
for n in range(LARGE):
    for m in range(n+1):
        assert m <= n
        if n == m:
            dp[n,m] = m
            continue
        if m == 0:
            dp[n,m] = 0
            continue
        dp[n,m] = (dp[n-1,m-1] + dp[n-1,m])%M9

# log(dp[2,1])
# log(dp[3,2])
# log(dp[3,1])
# log(dp[6,3])
# log(dp[6,4])

def modinv_p(base, p=M9):
    # modular if the modulo is a prime
    return pow(base, p-2, p)

# log(modinv_p(pow(2,98,M9)))
# log(modinv_p(pow(2,99,M9)))
# log(modinv_p(pow(2,100,M9)))
# log(modinv_p(pow(2,101,M9)))

two_inv = modinv_p(2)
# log((pow(two_inv,98,M9)))
# log((pow(two_inv,99,M9)))
# log((pow(two_inv,100,M9)))
# log((pow(two_inv,101,M9)))

def solve_(n,m,k):
    # your solution here
    if n == m:
        return (n*k)%M9
    if k == 0:
        return 0
    res = k * pow(two_inv,n-1,M9) * dp[n,m]

    return res%M9


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
    n,m,k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
