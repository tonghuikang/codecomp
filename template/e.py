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

M9 = 998244353 # 10**9 + 7  # 998244353
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

def factorial_mod_p(n, p):
    val = 1
    for i in range(1,n+1):
        val = (val*i)%p
    return val



def solve_(mrr, n, m):
    # your solution here

    fn = factorial_mod_p(n, M9)

    val = 0
    for col in zip(*mrr):
        # for perm in itertools.permutations(range(1,n+1)):
        #     arr = [a+b-1 for a,b in zip(col, perm)]
        #     if min(arr) <= n:
        #         val += 1
    
        col = sorted(col)

        numer = 1
        # demon = 1
        for i,x in enumerate(col):
            dem = n-i
            num = dem - max(0, n-x+1)
            numer *= num
            # demon *= dem

        # log(math.factorial(n)-numer)
        # log(6-numer)
        val += fn-numer



    # vals = []
    # for perm in itertools.permutations(range(1,n+1)):
    #     matrix = [[x+delay-1 for x in row] for row, delay in zip(mrr, perm)]
    #     val = sum(min(col) <= n for col in zip(*matrix))
    #     vals.append(val)
    
    # log(vals)
    # log(sum(vals)/math.factorial(n))

    return (val * pow(factorial_mod_p(n, M9), M9-2, M9)) % M9


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
    n,m = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)