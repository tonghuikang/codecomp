import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid, h, w):  # fix inputs here
    console("----- solving ------")
    console(grid)

    lst = []

    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            lst.append([
                grid[h-i-1][w-j-1],
                grid[h-i-1][j],
                grid[i][w-j-1],
                grid[i][j],
            ])

    res = 0
    for vals in lst:
        vals = sorted(vals)
        median = (vals[1] + vals[2]) // 2
        for v in vals:
            res += abs(v-median)
    # return a string (i.e. not a list or matrix)
    return res//4


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows, w = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid, h=nrows, w=w)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
