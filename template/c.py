import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(grid):
    if len(grid) == 1:
        return 0

    median = sorted([y for x,y in grid])[len(grid)//2]

    cost = sum([abs(median - y) for x,y in grid])

    arr = sorted([x for x,y in grid])


    brr = sorted([(x-i,x) for i,x in enumerate(arr)])   

    start,_ = brr[len(grid)//2]
    console(brr, start)

    mincost = 0
    for a,c in zip(arr, range(start, start+len(grid))):
        mincost += abs(a-c)
        # mincost = min(mincost, check_median_x((len(grid)+1)//2, offset))
    
    console(cost, mincost)

    return cost+mincost


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    # if not ONLINE_JUDGE:
    #     console("----- solving ------")
    #     console(*args)
    #     console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    nrows = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid)  # please change
    
    # print result
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
    # print(*res)  # if printing a list