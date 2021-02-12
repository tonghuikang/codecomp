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

def floor_sum_over_divisor_(n,k,j):
    return sum(n//d for d in range(j+1, k+1))

def floor_sum_over_divisor(n,k,j):
    # https://math.stackexchange.com/questions/384520/efficient-computation-of-sum-k-1n-lfloor-fracnk-rfloor
    # https://mathoverflow.net/questions/48357/summation-of-a-series-of-floor-functions       
    return floor_sum_over_divisor_(n, n//j, n//k) + k*(n//k) - j*(n//j)

# log(floor_sum_over_divisor(5,5))


def solve_(a,b):
    # your solution here

    # a > b
    # a < b**2
    res = 0

    transfer = 10**5
    for y in range(2, min(transfer, b+1)):
        cnt = min(y-1, a // (y + 1))
        # log(y,cnt)
        res += cnt
    log(res)

    if transfer < b+1:
        addn_sum = floor_sum_over_divisor(a, b+1, transfer)
        log(addn_sum)
        res += addn_sum


    # res2 = floor_sum_over_divisor(a,b)

    # check_res = 0
    # for i in range(1,a+1):
    #     for j in range(1,b+1):
    #         if i//j == i%j:
    #             check_res += 1

    # log(res, check_res)
    # assert res == check_res

    return res

# print(solve(10**9, 10**9))
# print(solve(10**9, int(10**4.5)))
# print(solve(10**9, int(10**5)))
# print(solve(10**9, int(10**6)))

# for p in range(1,1000):
#     for q in range(1,1000):
#         solve(q,p)
# solve(10**9, 10**9)

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
    a,b = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(a,b)  # include input here
    
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