import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid_original):  # fix inputs here
    console("----- solving ------")

    # INDEFINITE CHECK, order does not matter, starting point does not matter
    grid = [[e,e+r] for e,r in grid_original]  # copy
    if len(grid) == 1:
        return [0, grid[0][0]]

    grid = sorted(grid, key = lambda x:x[1])[::-1]
    summ = sum(e for e,r in grid)

    for i,(e,r) in enumerate(grid):
        if r <= summ:
            console(r, summ)
            return [i, "INDEFINITELY"]
        summ = summ - e
    # INDEFINITE CHECK OVER

    # standard variables
    grid = [[e,e+r] for e,r in grid_original]  # copy
    err, rrr = zip(*grid)
    err, rrr = list(err), list(rrr)
    summ = sum(err)
    console(grid)
    console(err)
    console(rrr)

    maxres = summ
    min_elim_for_maxres = 0

    # NO ELIMINATE
    for e,r in grid:
        if r <= summ:
            maxres += e
        else:
            break
            
    # return [maxres, min_elim_for_maxres]


    cur_time = summ
    cur_elim = 0

    heap = []
    heapq.heapify(heap)

    for e,r in grid:
        if r <= summ:
            cur_time += e
            heapq.heappush(heap, (-r, e))
            if cur_time > maxres:
                maxres = cur_time
                min_elim_for_maxres = cur_elim
        else:  # r > summ:
            cur_time = cur_time - e  # delete this cycle and previous cycle
            summ = summ - e  # now the threshold is lower
            cur_elim = cur_elim + 1

            while heap and -heap[0][0] > summ:  # need to delete the past
                r_neg, e = heapq.heappop(heap)
                r = -r_neg
                cur_time = cur_time - 2*e
                summ = summ - e            
                cur_elim = cur_elim + 1

        console(maxres, min_elim_for_maxres, "|", cur_time, cur_elim, "|", heap)

    # # return a string (i.e. not a list or matrix)
    return [maxres, min_elim_for_maxres]


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

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
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, " ".join(str(x) for x in res)))

    # Codeforces - no case number required
    # print(res)
