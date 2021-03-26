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


def check(L):
    # your solution here

    count = 0
    for i in range(len(L)-1):
        j = L.index(i+1)
        L[i:j+1] = L[i:j+1][::-1]
        cost = j+1-i
        # log(cost, L)
        count += cost
    log(count)
    return count


def solve_(n,target):
    # your solution here
    c = target

    lower = n-1
    upper = (n*(n+1))//2-1
    log(lower, upper)
    if not (lower <= c <= upper):
        return ["IMPOSSIBLE"]

    c -= n-1
    sequence = []
    for limit in range(n-1,0,-1):
        greed = min(limit,c)
        sequence.append(greed)
        c -= greed
    sequence = [x+1 for x in sequence]
    # log(sequence)

    arr = list(range(1,n+1))
    for i,length in enumerate(sequence[::-1], start=2):
        left = n-i
        arr[left:left+length] = arr[left:left+length][::-1]
        # log(left, left+length, arr)

    if OFFLINE_TEST:
        assert target == check([x for x in arr])

    return arr



if OFFLINE_TEST:
    for i in range(2,8):
        for j in range(2,30):
            solve_(i,j)




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
    n,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(n,c)  # include input here
    
    # print result
    # Google and Facebook - case number required
    print("Case #{}: {}".format(case_num+1, " ".join([str(x) for x in res])))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)