import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(n,k,a,b,c,d):  # fix inputs here
    console("----- solving ------")
    (a,b), (c,d) = sorted([(a,b),(c,d)])  # so that a < c
    console(n,k,a,b,c,d)

    # outer range
    outer_range = max(b,d) - min(a,c)
    console("outer_range", outer_range)

    # overlapping extent (if there is)
    overlapping = (b-a) + (d-c) - outer_range
    console("overlapping", overlapping)

    # get stage 1 and stage 2 sets
    stage_1 = 0
    stage_2 = outer_range
    if overlapping < 0:
        overlapping = 0
        stage_1 = c-b
    else:
        k = k - overlapping*n
        stage_2 = outer_range - overlapping

    if k < 0:
        return 0
        
    if stage_2 == 0:
        return k*2

    console("stage_1, stage_2, k", stage_1, stage_2, k)

    complete_sets = min(n, k // stage_2)

    console("complete_sets", complete_sets)

    required = complete_sets * (stage_2 + stage_1)
    console("required (1)", required)

    remaining = k - complete_sets*stage_2
    console("remaining", remaining)
    if complete_sets == n:
        required += remaining * 2
    else:
        if complete_sets > 0:  
            required += min(remaining * 2, 
                            stage_1 + remaining)
            required = min(required, stage_1 + stage_2 + (k - stage_2) * 2)
        else:
            required += stage_1 + remaining

    return required


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
    n,k = list(map(int,input().split()))
    a,b = list(map(int,input().split()))
    c,d = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(n,k,a,b,c,d)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
