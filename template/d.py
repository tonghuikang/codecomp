import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst, k):  # fix inputs here
    console("----- solving ------")


    cost_heap = [(0,k)]
    heapq.heapify(cost_heap)

    lst[0] = 0
    lst[-1] = 0
    lst = [math.inf if x == 0 else x for x in lst]
    console(lst,k)

    for i,stn in enumerate(lst):
        while cost_heap[0][1] < i:
            heapq.heappop(cost_heap)
        min_cost = cost_heap[0][0]
        heapq.heappush(cost_heap, (min_cost + stn, i+k))
        console(cost_heap)

    # console(cost_heap)
    # return a string (i.e. not a list or matrix)

    if cost_heap[0][0] == math.inf:
        return -1
    return cost_heap[0][0]


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
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
    nrows, m = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        # grid.append(list(map(int,input().split())))
        grid.append(int(input()))

    res = solve(grid, m)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)

