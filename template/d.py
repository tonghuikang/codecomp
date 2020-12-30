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


def solve_(wrr, edges):
    # your solution here

    # wrr = sorted(wrr)
    g = defaultdict(list)

    for a,b in edges:
        g[a].append(b)
        g[b].append(a)

    # log(g)

    counts = [-1 for _ in wrr]
    for k,v in g.items():
        for x in v:
            counts[x] += 1
    
    log(wrr)
    log(counts)

    arr = []
    for w,c in zip(wrr, counts):
        for _ in range(c):
            arr.append(w)

    arr = sorted(arr)[::-1]
    log(arr)

    res = [sum(wrr)]
    for x in arr:
        res.append(res[-1] + x)

    return res


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
    wrr = list(map(int,input().split()))

    # read multiple rows
    edges = read_matrix(k-1)
    # arr = read_strings(k)

    edges = [(x-1, y-1) for x,y in edges]

    res = solve(wrr, edges)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))  # if printing length of list
    print(*res)  # if printing a list