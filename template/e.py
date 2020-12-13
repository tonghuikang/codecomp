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

sys.setrecursionlimit(10**6)

def solve_(arr,brr):

    @functools.lru_cache(maxsize=None)
    def dp(x,y):
        if x == len(arr) or y == len(brr):
            # delete remaining
            return len(arr) + len(brr) - x - y

        xx = dp(x+1,y)
        yy = dp(x,y+1)
        zz = dp(x+1,y+1)

        # delete either a or b
        cur = min(xx, yy) + 1

        if arr[x] == brr[y]:
            # keep both if equal
            cur = min(cur, zz)
        else:
            # keep both if mismatch
            cur = min(cur, zz+1)
        
        return cur

    return dp(0,0)

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
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    if len(arr) > len(brr):
        arr,brr = brr,arr

    res = solve(arr,brr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list