import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    console("----- solving ------")

    if 1 not in lst:
        return [-1, -1]

    max_height = 0
    max_idxs = []
    prev = 0

    for i,x in enumerate(lst):
        if x - prev == 1:
            prev = x
            if x > max_height:
                max_height = x
                max_idxs = [i]
            elif x == max_height:
                max_idxs.append(i)
        else:
            prev = 0

    max_height1 = max_height
    max_idxs1 = [x for x in max_idxs]
    console(max_height, max_idxs)

    max_height = 0
    max_idxs = []
    prev = 0

    for i,x in enumerate(lst[::-1]):
        if x - prev == 1:
            prev = x
            if x > max_height:
                max_height = x
                max_idxs = [len(lst)-i-1]
            elif x == max_height:
                max_idxs.append(len(lst)-i-1)
        else:
            prev = 0

    max_height2 = max_height
    max_idxs2 = [x for x in max_idxs]
    console(max_height, max_idxs)

    if max_height2 > max_height1:
        return [max_height2, min(max_idxs2)]
    else:
        return [max_height1, min(max_idxs1)]
    # return a string (i.e. not a list or matrix)
    # return [0, 0]


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    _ = input()
    _ = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, "{} {}".format(*res)))

    # Codeforces - no case number required
    # print(res)
