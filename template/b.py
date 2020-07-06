import sys
import heapq, functools, collections, itertools
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid,k):  # fix inputs here
    console(grid)
    grid = [[1 if x == "#" else 0 for x in row] for row in grid]
    console("----- solving ------")
    console(grid)

    res = 0

    for arr in itertools.product([0,1], repeat=len(grid)+len(grid[0])):
        cnt = 0
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if arr[i] == 0 and arr[-j-1] == 0 and cell == 1:
                    cnt += 1
        if cnt == k:
            res += 1
        # print(arr, res, cnt)
    
    return res


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows,_,k = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(input())

    res = solve(grid,k)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
