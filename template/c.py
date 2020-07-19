import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid, n):  # fix inputs here
    console("----- solving ------")
    grid = sorted(grid)[::-1]
    console(grid,n)

    baseline = []

    for i,(a,b) in enumerate(grid):
        calc = a+b*(n-1)
        baseline.append(calc)

    # recursive_value = grid[max_idx][1]
    console(baseline)
    # console(max_base, recursive_value, max_idx)


    max_res = 0

    for max_idx,(first,_) in enumerate(sorted(grid)[::-1]):
        res = baseline[max_idx]
        recursive_value = grid[max_idx][1]
        cnt = n-1
        for i,(first,_) in enumerate(sorted(grid)[::-1]):
            if i == max_idx:
                continue
            if first > recursive_value and cnt > 0:
                res += first-recursive_value
                cnt -= 1
        res = max(max_res,res)

    return res


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inn = sys.stdin.readlines()
idx = 1

for case_num in range(int(inn[0])):
    n,nrows = list(map(int,inn[idx].split()))

    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for i in range(nrows):
        grid.append(list(map(int,inn[idx+i+1].split())))

    res = solve(grid, n)  # please change

    idx = idx+nrows+2

    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
