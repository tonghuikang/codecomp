import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(a,b,cx,cy,x,y):  # fix inputs here
    console("----- solving ------")

    a,b = sorted([a,b])
    if x > y:  # to make x < y
        x,y = y,x
        cx,cy = cy,cx

    maxcnt = 0
    for i in range(cx+1):
        ax = min(a//x, i)
        bx_max = cx - ax
        bx = min(b//x, bx_max)

        a_left = a - ax*x
        b_left = b - bx*x

        ay = min(a_left//y, cy)
        by_max = cy - ay
        by = min(b_left//y, by_max)

        maxcnt = max(maxcnt, ax+bx+ay+by)

    return maxcnt


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
    p,f = list(map(int,input().split()))
    cs,cw = list(map(int,input().split()))
    s,w = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(p,f,cs,cw,s,w)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
