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
# MAXINT = sys.maxsize

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

# def sieve_of_eratosthenes(n):
#     # primarity test and prime factor listing for all numbers less than n
#     prime = [True for _ in range(n)] 
#     prime[0], prime[1] = False, False
#     factors = [[] for _ in range(n)]

#     for i in range(2,n):
#         factors[i].append(i)
#         for j in range(i*2, n, i):
#             prime[j] = False
#             factors[j].append(i)
#     return prime, factors

# prime, factors = sieve_of_eratosthenes(2*10**5 + 10)


# tree of factors
# path with greatest value
LARGE = 2*10**5 + 5

def solve_(mrr):
    mrr = [x for x in mrr if x > 1]
    if not mrr:
        return 0
    
    # c = [0]*LARGE
    dp = [0]*LARGE

    for x in mrr:
        # c[x] += 1
        dp[x] += 1
    
    c = Counter(mrr)
    # dp = Counter(mrr)
    # for k,v in c.items():
    #     dp[k] = v
    # log(arr)
    # log(brr)

    for a in range(1, LARGE-1):
        for j in range(2*a, LARGE, a):
            dp[j] = max(dp[j], dp[a] + c[j])
        # dp[a] = max(dp[factor] for factor in factors[a]) + b

    # print(dp)

    return len(mrr) - max(dp)

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
    lst = list(map(int,input().split()))


    res = solve(lst)  # include input here
    
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