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
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

M9 = 10**9+7

def solve_(lst):
    # your solution here

    count = [0 for _ in range(60)]
    value = [(2**i)%M9 for i in range(60)]

    arr = [bin(a)[2:].zfill(60)[::-1] for a in lst]
    for br in arr:
        for i,b in enumerate(br):
            if b == "1":
                count[i] += 1
    
    # log(count)
    res = 0

    for br in arr:
        # and calculation
        AND = 0
        for i,x in enumerate(br):
            if x == "1":
                AND += count[i]*value[i]
        OR = 0
        for i,x in enumerate(br):
            if x == "1":
                OR += len(lst)*value[i]
            else:
                OR += count[i]*value[i]
        # log(br, AND, OR)
        res += AND * OR
        res = res%M9
        
    return res%M9


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
    k = int(input())
    
    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(lst)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list