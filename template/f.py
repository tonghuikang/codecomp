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


def solve_(h,w,mrr):
    # your solution here

    mindown = [h for _ in range(w)]
    minhori = [w for _ in range(h)]

    for x,y in mrr:
        mindown[y] = min(mindown[y], x)
        minhori[x] = min(minhori[x], y)

    double_min = minhori[0]
    double1 = 0
    for x in minhori:
        double_min = min(double_min, x)
        double1 += double_min

    double_min = mindown[0]
    double2 = 0
    for x in mindown:
        double_min = min(double_min, x)
        double2 += double_min

    log(mindown)
    log(minhori)
    log(double1)
    log(double2)

    assert double1 == double2

    return sum(mindown[:minhori[0]]) + sum(minhori[:mindown[0]]) - double1


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

for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    h,w,k = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)
    # arr = read_strings(k)
    mrr = [(x-1,y-1) for x,y in mrr]
    res = solve(h,w,mrr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list