import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid):  # fix inputs here
    console("----- solving ------")
    console(grid)

    grid = [[0 if cell == "#" else 1 for cell in list(row[0])] for row in grid]

    console(grid)

    grid = [[0]*len(grid[0])] + grid + [[0]*len(grid[0])]
    grid = [[0] + row + [0] for row in grid]
    
    diff = [(0,1), (0,-1), (1,0), (-1,0)]
    res = 0
    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            if grid[i][j] == 1:
                for dx,dy in diff:
                    if grid[i+dx][j+dy] == 1:
                        res += 1

    console(res)

    # return a string (i.e. not a list or matrix)
    return res//2


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows, _ = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(input().split()))

    res = solve(grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
