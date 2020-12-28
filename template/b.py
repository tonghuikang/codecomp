import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(arr,brr):
    # your solution here

    cur = 0
    maxa = 0
    for a in arr:
        cur += a
        maxa = max(maxa, cur)

    cur = 0
    maxb = 0
    for a in brr:
        cur += a
        maxb = max(maxb, cur)

    return maxa + maxb


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

# for case_num in [1]:  # no loop over test case
for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    
    # read one line and parse each word as an integer
    _ = int(input())
    arr = list(map(int,input().split()))

    _ = int(input())
    brr = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(arr, brr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list