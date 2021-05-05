#!/usr/bin/env python3
import io
import os
from collections import deque
# input = sys.stdin.readline  # to read input quickly
from math import inf
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = inf

# ---------------------------- template ends here ----------------------------


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
                if 0 <= xx < nrows and 0 <= yy < ncols:
                    new_loc = xx*ncols+yy
                    if dist[new_loc] == MAXINT and mrr[new_loc] >= 0:
                        dist[new_loc] = dist[loc] + w
                        stack.append(new_loc)
        return dist  

    dist_from_start = dfs(0, size)
    dist_from_dest = dfs(size-1, size)

    # log(dist_from_start)
    # log(dist_from_dest)

    tele_from_start = inf
    tele_from_dest = inf
 
    for x in range(nrows):
        for y in range(ncols):
            loc = x*ncols + y
            if mrr[loc] > 0:
                tele_from_start = min(tele_from_start, mrr[loc] + dist_from_start[loc])
                tele_from_dest = min(tele_from_dest, mrr[loc] + dist_from_dest[loc])
        
    minres = min(dist_from_start[size-1], tele_from_start+tele_from_dest)

    if minres == inf:
        return -1
    return minres


for case_num in [0]:  # no loop over test case

    
    # read one line and parse each word as an integer
    n,m,w = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)
    w = float(w)


    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = [float(x) for i in range(n) for x in input().split()]
    # mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve_(mrr, w, n, m)  # include input here

    print(int(res))