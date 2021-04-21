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

def canPartition(nums):
    s, n, memo = sum(nums), len(nums), {0: True}
    if s & 1: return False
    nums.sort(reverse=True)
    def dfs(i, x):
        if x not in memo:
            memo[x] = False
            if x > 0:
                for j in range(i, n):
                    if dfs(j+1, x-nums[j]):
                        memo[x] = True
                        break
        return memo[x]
    return dfs(0, s >> 1)


def solve_(lst):
    # remove gcd
    # if sum is even
    # hypothesis, only need to remove at most one

    gcd = math.gcd(lst[0], lst[1])

    for z in lst:
        gcd = math.gcd(z, gcd)

    lst = [x//gcd for x in lst]  # cant be all even, confirm got odd
    log(lst)

    # if sum(lst)%2 == 1:
    #     return []
    lst_original = [x for x in lst]

    if not canPartition(lst):
        return -1

    # lst = [(i+1,x) for i,x in enumerate(lst_original)]
    # log(lst)

    for i,x in enumerate(lst_original, start=1):
        if x%2 == 1:
            # log(i, x, lst[i])
            return i
    return -1



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
    lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(lst)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    if res == -1:
        print(0)
    else:
        print(1)
        print(res)
    # print(len(res))
    # if res:
    #     print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)