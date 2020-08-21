import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(a,b,c,x,y,z):  # fix inputs here
    console("----- solving ------")

    score = min(c,y)

    # we want 2-1 and don't want 1-2

    # remaining 1-2 we are forced to make
    remaining_non_1b = a+c-score
    remaining_non_2c = x+y-score
    remaining = a+b+c - score

    forced = remaining - remaining_non_1b - remaining_non_2c
    if forced <= 0:
        forced = 0

    console(remaining_non_1b,remaining_non_2c,remaining)
    console(score,forced)
    return (score-forced)*2
    # return a string (i.e. not a list or matrix)
    # return ""  


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
    a,b,c = list(map(int,input().split()))
    x,y,z = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(a,b,c,x,y,z)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
