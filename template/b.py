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


def solve_(mrr, n, k):
    # your solution here

    

    pool = []
    for (i,row) in enumerate(mrr):
        for (j,cell) in enumerate(row):
            pool.append((cell,i,j))

    untaken = [set(range(k)) for _ in range(n)]
    pool.sort()

    shortest = pool[:k]
    for cell,i,j in shortest:
        untaken[i].remove(j)

    all_res = []

    for cell,i,j in shortest:
        curres = []
        for x in range(n):
            if i == x:
                curres.append((x,j))
            else:
                for y in untaken[x]:
                    curres.append((x,y))
                    untaken[x].remove(y)
                    break
        # log(curres)
        all_res.append(curres)

    # log(all_res)
    # log(mrr)

    all_res = list(zip(*all_res))
    all_res = "\n".join([" ".join([str(mrr[i][j]) for i,j in curres]) for curres in all_res])
    return all_res


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
    n,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(n)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr,n,k)  # include input here
    
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