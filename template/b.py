import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid,k):  # fix inputs here
    console("----- solving ------")
    console(grid,k)
    # return a string (i.e. not a list or matrix)
    grid = sorted(grid)
    
    curextent = -1
    res = 0

    for a,b in grid:
        if b > curextent:
            covered_until = max(curextent, a)
            need_to_cover = b - covered_until
            robots_to_cover = -((-need_to_cover)//k)
            curextent = covered_until + k*robots_to_cover
            console(covered_until, need_to_cover, robots_to_cover, curextent, res)
            res += robots_to_cover
    
    return res


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()
currow = 0

for case_num in range(int(inp[currow])):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()
    currow += 1
    # read one line and parse each word as an integer
    nrows,k = list(map(int,inp[currow].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        currow += 1
        grid.append(list(map(int,inp[currow].split())))

    res = solve(grid,k)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
