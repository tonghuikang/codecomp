import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grids, numcol):  # fix inputs here
    console("----- solving ------")
    console(grids)
    # return a string (i.e. not a list or matrix)
    res = 0
    while grids:
        curs = []
        for i in range(numcol):
            cnt = 0
            for grid in grids:
                for a,b in grid:
                    if a <= i <= b:
                        cnt += 1
            curs.append((cnt, i))
        console(max(curs))
        cnt, i = max(curs)
        new_grids = []
        for grid in grids:
            new_grid = []
            for a,b in grid:
                if a <= i <= b:
                    pass
                else:
                    new_grid.append((a,b))
            if new_grid:
                new_grids.append(new_grid)
        grids = new_grids
        res += cnt**2
        # break

    console(grids)
    return res


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
nrows, numcol = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
grids = []
for _ in range(nrows):
    k = int(input())
    grid = []
    for _ in range(k):
        grid.append(list(map(int,input().split())))
    grids.append([(a-1, b-1) for a,b in grid])

res = solve(grids, numcol)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
print(res)
