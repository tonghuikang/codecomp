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


def solve_(lst, k):
    # your solution here
    k = k-1

    # impose as it progresses
    # check if last element is in the limit

    upper = lst[0]+k
    lower = max(0,lst[0]-k)
    for i,x in enumerate(lst[1:-1], start=1):
        if lower > x+k or upper < x:
            # log("fail", lower, x, upper)
            return "no"
        upper = min(upper, x+k) + k
        lower = max(0,max(lower, x) - k)
        # log(lower, upper)

    if lower <= lst[-1] <= upper:
        return "YES"

    return "NO"


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
    # k = int(input())
    
    # read one line and parse each word as an integer
    _, k = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(lst, k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list