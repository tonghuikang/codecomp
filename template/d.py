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
        return [[-1 for _ in range(m)] for _ in range(n)]

    k = k//2

    # for every node, propagate 10 units
    minedge = [[LARGE for _ in range(m)] for _ in range(n)]
    # edges = []
    # costs = []

    g = defaultdict(set)
    for i,row in enumerate(hrr):
        for j,cost in enumerate(row):
            g[i, j].add((i, j+1, cost))
            g[i, j+1].add((i, j, cost))
            # edges.append(((i,j), (i,j+1)))
            # costs.append(cost)
            minedge[i][j] = min(minedge[i][j], cost)
            minedge[i][j+1] = min(minedge[i][j+1], cost)

    for i,row in enumerate(vrr):
        for j,cost in enumerate(row):
            g[i, j].add((i+1, j, cost))
            g[i+1, j].add((i, j, cost))
            # edges.append(((i,j), (i+1,j)))
            # costs.append(cost)
            minedge[i][j] = min(minedge[i][j], cost)
            minedge[i+1][j] = min(minedge[i+1][j], cost)

    # total_tree_cost, tree_edges = minimum_spanning_tree(edges, costs)
    # log(total_tree_cost)
    # log(tree_edges)

    # log(g)
    # log(minedge)

    all_res = [[LARGE for _ in range(m)] for _ in range(n)]
    for sx in range(n):
        for sy in range(m):
            minres = LARGE
            dist = {}
            small_edge = {}
            dist[sx,sy] = minedge[sx][sy]*k
            small_edge[sx,sy] = minedge[sx][sy]
            for z in range(k):
                new_dist = {}
                new_small_edge = {}
                for (cx, cy), (prev_cost) in dist.items():
                    for xx, yy, cost in g[cx, cy]:
                        if cost > small_edge[cx,cy]:
                            new_cost = prev_cost - small_edge[cx,cy] + cost
                        else:
                            new_cost = prev_cost - small_edge[cx,cy]*(k-z) + cost*(k-z)
                        if (xx,yy) in new_dist:
                            new_dist[xx,yy] = min(new_dist[xx,yy], new_cost)
                            new_small_edge[xx,yy] = min(new_small_edge[xx,yy], small_edge[cx,cy], cost)
                        else:
                            new_dist[xx,yy] = new_cost
                            new_small_edge[xx,yy] = min(small_edge[cx,cy], cost)
                        minres = min(minres, new_cost)
                dist = new_dist
                small_edge = new_small_edge
                # log(sx, sy, dist)
            all_res[sx][sy] = minres*2

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

    res = solve(n,m,k,hrr,vrr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    res = "\n".join(" ".join([str(r) for r in rr]) for rr in res)
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)