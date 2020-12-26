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
# OFFLINE_TEST = getpass.getuser() == "hkmac"
OFFLINE_TEST = False
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(mrr, qrr):
    # your solution here

    counters = defaultdict(lambda: defaultdict(int))
    
    for i,row in enumerate(mrr):
        for j,cell in enumerate(row):
            counters[i-j][cell] += 1

    # log(counters)
    accepted = sum(len(c) == 1 for c in counters.values())

    qrr = [(x-1,y-1,z) for x,y,z in qrr]

    for i,j,new in qrr:
        old = mrr[i][j]
        mrr[i][j] = new

        if len(counters[i-j]) == 1:
            accepted -= 1

        counters[i-j][old] -= 1
        if counters[i-j][old] == 0:
            del counters[i-j][old]
        counters[i-j][new] += 1

        if len(counters[i-j]) == 1:
            accepted += 1
        
        # log(counters)
        # log(accepted)
        if accepted == len(counters):
            print("Yes")
        else:
            print("No")


    return ""


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
    n,m = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(n)

    q = int(input())
    qrr = read_matrix(q)
    # arr = read_strings(k)

    solve(mrr, qrr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list