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

def all_divisors(n):
    return set(functools.reduce(list.__add__, 
    ([i, n//i] for i in 
    range(1, int(n**0.5) + 1) if n % i == 0)))


def solve_(k):
    # your solution here
    # for a in range(int(math.sqrt(k+1))):
    k = 8*k
    limit = k**0.5

    all_div = all_divisors(k)
    res = 0
    for d in all_div:
        if d > limit:
           continue
        p = k//d
        q = d

        if (p+q)%2 == 0:
            y = (p+q)//2
            x = (p-q)//2
            # log(p,q,x,y,x**2 + k - y**2)
            # if x**2 + k - y**2 == 0:
            #     res += 1
            if x&1:
                res += 1


    # log(all_div)
    # for a in range(k+1):
    #     x = (2*a-1)**2 + 8*k 
    #     if int(x**0.5)**2 == x:
    #         print(a)
    return res*2


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # n,m = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # arr = read_matrix(m)  # and return as a list of list of int
    k = int(input())
    # brr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(k)  # include input here
    
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