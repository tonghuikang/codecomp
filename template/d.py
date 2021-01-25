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


def solve_(arr,brr,c):
    # your solution here
    sumarr = sum(arr)
    if sumarr < c:
        return -1

    if sum(arr) == c:
        return sum(brr)
    
    # important = []
    # unimportant = []
    # for a,b in zip(arr,brr):
    #     if b == 1:
    #         unimportant.append(a)
    #     else:
    #         important.append(a)

    # important.sort()
    # unimportant.sort()

    # log(important)
    # log(unimportant)
    # log()

    # c = c*2
    order = sorted([(a/b,b,a) for a,b in zip(arr,brr)])[::-1]
    
    # order = [(a,b,c) for a,b,c in order]
    
    log(order)

    mem = 0
    cost = 0
    limit_single = 0
    limit_double = 0
    max_single = False
    max_double = False
    for _,b,a in order:
        mem += a
        cost += b
        if b == 1:
            max_single = True
            limit_single += 1
        else:
            limit_double += 1
            max_double = True
        if mem >= c:
            break

    limit_single -= 1
    limit_double -= 1
    res = cost
    log(cost)

    if max_single:
        num_single = 0
        mem = 0
        cost = 0
        for _,b,a in order:
            log(num_single, limit_single)
            if b == 1:
                if num_single == limit_single:
                    continue
                num_single += 1
            mem += a
            cost += b
            if mem >= c:
                res = min(res, cost)
                break
        else:
            pass

    if max_double:
        num_double = 0
        mem = 0
        cost = 0
        for _,b,a in order:
            log(num_double, limit_double)
            if b == 2:
                if num_double == limit_double:
                    continue
                num_double += 1
            mem += a
            cost += b
            if mem >= c:
                res = min(res, cost)
                break
        else:
            pass

    return res # - max_single


all_res = []
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
    _,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    # if case_num+1 == 105:
    #     print(arr,brr,c)
    #     exit()

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr,brr,c)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    all_res.append(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)
print("\n".join(str(r) for r in all_res))