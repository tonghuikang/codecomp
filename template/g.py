#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def shortest_path_constant_cost(map_from_node_to_nodes, source, target):
    # to be tested
    # no path is produced here
    d = map_from_node_to_nodes
    stack = deque([source])
    visited = {source: 0}
    while stack:
        cur = stack.popleft()
        for nex in d[cur]:
            if nex in visited:
                continue
            stack.append(nex)
            visited[nex] = visited[cur] + 1
            if nex == target:
                return visited[nex]
    return MAXINT



def solve_(mrr, w, nrows, ncols):
    # your solution here
    
    
    # start from zero
    source = (0,0)
    stack = deque([source])
    dist_from_start = {source:0}
    while stack:
        x,y = stack.popleft()
        for dx,dy in d4:
            xx = x+dx
            yy = y+dy
            if (xx,yy) in dist_from_start:
                continue
            if 0 <= xx < nrows and 0 <= yy < ncols:
                if mrr[xx][yy] == -1:
                    continue
                dist_from_start[xx,yy] = dist_from_start[x,y] + w
                stack.append((xx,yy))
    

    source = (nrows-1,ncols-1)
    stack = deque([source])
    dist_from_end = {source:0}
    while stack:
        x,y = stack.popleft()
        for dx,dy in d4:
            xx = x+dx
            yy = y+dy
            if (xx,yy) in dist_from_end:
                continue
            if 0 <= xx < nrows and 0 <= yy < ncols:
                if mrr[xx][yy] == -1:
                    continue
                dist_from_end[xx,yy] = dist_from_end[x,y] + w
                stack.append((xx,yy))

    minres = MAXINT
    if (nrows-1,ncols-1) in dist_from_start:
        minres = min(minres, dist_from_start[(nrows-1,ncols-1)])
    
    min_tele_from_source = MAXINT//2
    for (x,y), cost in dist_from_start.items():
        if mrr[x][y] > 0:
            min_tele_from_source = min(min_tele_from_source, cost + mrr[x][y])
        
    min_tele_from_dest = MAXINT//2
    for (x,y), cost in dist_from_end.items():
        if mrr[x][y] > 0:
            min_tele_from_dest = min(min_tele_from_dest, cost + mrr[x][y])

    res = min(minres, min_tele_from_dest + min_tele_from_source)
    # log(res, minres, min_tele_from_dest, min_tele_from_source)
    # log(dist_from_end)

    if res > MAXINT//4:
        return -1
    return res


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
    n,m,w = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr, w, n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)