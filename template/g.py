#!/usr/bin/env python3
import io
import os
from collections import deque
from math import inf
# input = sys.stdin.readline  # to read input quickly
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = 10**15

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "hkmac"
OFFLINE_TEST = False  # codechef does not allow getpass
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

    size = nrows*ncols
    
    def dfs(source, size):
        # start from zero
        stack = deque([source])
        dist = [MAXINT]*size
        dist[source] = 0
        while stack:
            loc = stack.popleft()
            x,y = divmod(loc, ncols)
            for dx,dy in d4:
                xx = x+dx
                yy = y+dy
                new_loc = xx*ncols+yy
                if 0 <= xx < nrows and 0 <= yy < ncols and dist[new_loc] == MAXINT and mrr[new_loc] >= 0:
                    dist[new_loc] = dist[loc] + 1
                    stack.append(new_loc)
        return dist  

    dist_from_start = dfs(0, size)
    dist_from_dest = dfs(size-1, size)

    # log(dist_from_start)
    # log(dist_from_dest)

    tele_from_start = MAXINT//2
    tele_from_dest = MAXINT//2
 
    for x in range(nrows):
        for y in range(ncols):
            loc = x*ncols + y
            if mrr[loc] > 0:
                tele_from_start = min(tele_from_start, mrr[loc] + w * dist_from_start[loc])
                tele_from_dest = min(tele_from_dest, mrr[loc] + w * dist_from_dest[loc])
        
    minres = min(dist_from_start[size-1]*w, tele_from_start+tele_from_dest)

    if minres == MAXINT:
        return -1
    return minres


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
    mrr = [int(x) for i in range(n) for x in input().split()]
    # mrr = read_matrix(n)  # and return as a list of list of int
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