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

# Dynamic Programming solution to construct Longest
# Increasing Subsequence

# Function to construct and print Longest Increasing
# Subsequence
def constructPrintLIS(nums):
    h = [nums[0]] 
    for i in range(1, len(nums)):
        if nums[i] >= h[-1]:
            h.append(nums[i])
        else:
            j = bisect.bisect_left(h, nums[i]) 
            h[j] = nums[i]
    return h



def solve_(lst):
    # your solution here

    idx = {}

    for i,x in list(enumerate(lst))[::-1]:
        idx[x] = i
    arr = [idx[x] for x in lst]
    log("arr", arr)

    c = Counter(arr)
    blocker = False
    if c[lst[-1]] == 1:
        blocker = True 
    
    arr = [x for x in arr if c[x] > 1]
    log("arr trimmed", arr)

    res = constructPrintLIS(arr)
    lenres = len(res)
    c2 = Counter(res)
    for x in set(res):
        if c2[x] != c[x]:
            lenres -= c2[x]
    log("init", len(res), lenres, res, arr)
    minres = len(lst) - lenres

    if len(idx) == 1:  # if one element
        log("one element")
        return minres

    newres = 0
    # if not blocker:
    #     i = len(lst)-1
    #     while i >= 0:
    #         if lst[i] == lst[-1]:
    #             i -= 1
    #         else:
    #             break
    #     log(lst[:i+1])
    #     rst = [x for x in lst[:i+1] if x != lst[-1]]
    #     log(rst)
    #     arr = [idx[x] for x in rst]
    #     log(arr)

    #     res = constructPrintLIS(arr)
    #     lenres = len(res)
    #     c2 = Counter(res)
    #     for x in set(res):
    #         if c2[x] != c[x]:
    #             lenres -= c2[x]

    #     newres = len(arr) - lenres + len(lst[:i+1]) - len(rst)
    #     log(len(arr), lenres, len(lst[:i+1]), len(rst))
    #     log("newres", newres)

    return max(minres, newres)


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
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)