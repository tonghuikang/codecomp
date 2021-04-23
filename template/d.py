#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from typing import no_type_check
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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


LARGE = 10**9

def solve_(n,m,k,hrr,vrr):
    # your solution here
    if k%2:
        minedge = [[LARGE for _ in range(m)] for _ in range(n)]
        return "\n".join([" ".join([str(-1) for val in row]) for row in minedge])
 
    k = k//2
 
 
    # g = [[[] for _ in range(m)] for _ in range(n)]
    # for i,row in enumerate(hrr):
    #     for j,cost in enumerate(row):
    #         g[i][j].append((i, j+1, cost))
    #         g[i][j+1].append((i, j, cost))
    #         # edges.append(((i,j), (i,j+1)))
    #         # costs.append(cost)
    #         # minedge[i][j] = min(minedge[i][j], cost)
    #         # minedge[i][j+1] = min(minedge[i][j+1], cost)
 
    # for i,row in enumerate(vrr):
    #     for j,cost in enumerate(row):
    #         g[i][j].append((i+1, j, cost))
    #         g[i+1][j].append((i, j, cost))
            # edges.append(((i,j), (i+1,j)))
            # costs.append(cost)
            # minedge[i][j] = min(minedge[i][j], cost)
            # minedge[i+1][j] = min(minedge[i+1][j], cost)

    # if n*m > 1000:
    #     assert False

    # del hrr
    # del vrr

    # for every node, propagate 10 units
    minedge = [[LARGE for _ in range(m)] for _ in range(n)]
    new_minedge = [[LARGE for _ in range(m)] for _ in range(n)]
    propcost = [[0 for _ in range(m)] for _ in range(n)]
    new_propcost = [[LARGE for _ in _] for _ in propcost]
    all_res = [[val*k for val in row] for row in minedge]

    # greedily propogate min_edge

    for z in range(k):
        for x in range(n):
            for y in range(m):
                if x != 0:
                    xx = x-1
                    yy = y
                    cost = vrr[x-1][y]
                    new_minedge[xx][yy] = min(new_minedge[xx][yy], cost)
                    new_propcost[xx][yy] = min(new_propcost[xx][yy], propcost[x][y]+cost)
                if y != 0:
                    xx = x
                    yy = y-1
                    cost = hrr[x][y-1]
                    new_minedge[xx][yy] = min(new_minedge[xx][yy], cost)
                    new_propcost[xx][yy] = min(new_propcost[xx][yy], propcost[x][y]+cost)
                if x != n-1:
                    xx = x+1
                    yy = y
                    cost = vrr[x][y]
                    new_minedge[xx][yy] = min(new_minedge[xx][yy], cost)
                    new_propcost[xx][yy] = min(new_propcost[xx][yy], propcost[x][y]+cost)
                if y != m-1:
                    xx = x
                    yy = y+1
                    cost = hrr[x][y]
                    new_minedge[xx][yy] = min(new_minedge[xx][yy], cost)
                    new_propcost[xx][yy] = min(new_propcost[xx][yy], propcost[x][y]+cost)
        
        f = k-z-1
        for x in range(n):
            for y in range(m):
                all_res[x][y] = min(all_res[x][y], new_propcost[x][y]+f*new_minedge[x][y])
        minedge, new_minedge = new_minedge, minedge
        propcost, new_propcost = new_propcost, propcost
        for x in range(n):
            for y in range(m):
                new_propcost[x][y] = LARGE

    all_res = "\n".join([" ".join([str(val*2) for val in row]) for row in all_res])
    # log(all_res)
    return all_res
 


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,m,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    hrr = read_matrix(n)  # and return as a list of list of int
    vrr = read_matrix(n-1)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve_(n,m,k,hrr,vrr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # res = "\n".join(res)
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)