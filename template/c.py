import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid):  # fix inputs here
    console("----- solving ------")

    target_set = set([tuple(xy) for xy in grid])

    c1 = Counter([x for x,y in grid])
    c2 = Counter([y for x,y in grid])

    cx = sorted(c1.items(), key=lambda x:x[1])[::-1]
    cy = sorted(c2.items(), key=lambda x:x[1])[::-1]

    max_c1 = max(c1.values())
    max_c2 = max(c2.values())

    cxk = [k for k,v in cx if v == max_c1]
    cyk = [k for k,v in cy if v == max_c2]

    if max_c1 == 1:
        return min(len(grid), 1+max(c2.values()))
    if max_c2 == 1:
        return min(len(grid), 1+max(c1.values()))

    console(max(c1), max(c2))
    console(cx)
    console(cy)
    console(cxk)
    console(cyk)
    console(target_set)

    for x in cxk:
        for y in cyk:
            if (x,y) not in target_set:
                console(x,y)
                return max_c1 + max_c2
    return max_c1 + max_c2 - 1


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
    _,_,nrows = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
