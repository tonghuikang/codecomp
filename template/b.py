import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid):  # fix inputs here
    console("----- solving ------")

    if grid[0][0] > 2 or grid[0][-1] > 2 or grid[-1][0] > 2 or grid[-1][-1] > 2:
        print("NO")
        return
    
    for row in grid:
        if row[0] > 3 or row[-1] > 3:
            print("NO")
            return
        for cell in row:
            if cell > 4:
                print("NO")
                return

    for cell in grid[0]:
        if cell > 3:
            print("NO")
            return    

    for cell in grid[-1]:
        if cell > 3:
            print("NO")
            return

    grid = [[4 for cell in row] for row in grid]
    for i,row in enumerate(grid):
        grid[i][0] = 3
        grid[i][-1] = 3
    grid[0] = [3 for cell in grid[0]]
    grid[-1] = [3 for cell in grid[-1]]

    grid[0][0] = 2
    grid[0][-1] = 2
    grid[-1][0] = 2
    grid[-1][-1] = 2

    print("YES")
    for row in grid:
        print(" ".join([str(cell) for cell in row]))

    # return a string (i.e. not a list or matrix)
    return ""  


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    nrows,_ = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
