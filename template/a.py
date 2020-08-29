import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# plotting = False
debugging = False
# debugging = True

def solve(srr, xrr, yrr):  # fix inputs here
    console("----- solving ------")
    console(srr, sum(srr))
    console(xrr, sum(xrr))
    console(yrr, sum(yrr))

    if sum(srr) > sum(xrr) + sum(yrr) or sum(srr) < sum(xrr):
        return -1

    res_1 = 0
    res_2 = 0
    for s,x,y in zip(srr, xrr, yrr):
        if s < x:
            res_1 += x-s
        if s > x+y:
            res_2 += s-(x+y)

    return max(res_1, res_2)


def console(*args):  # the judge will not read these print statement
    if debugging:
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
    srr = list(map(int,input().split()))
    a_s, b_s, c_s, d_s = list(map(int,input().split()))
    xrr = list(map(int,input().split()))
    a_x, b_x, c_x, d_x = list(map(int,input().split()))
    yrr = list(map(int,input().split()))
    a_y, b_y, c_y, d_y = list(map(int,input().split()))


    for _ in range(k, n):
        srr.append(((a_s * srr[-2] + b_s * srr[-1] + c_s) % d_s))
        xrr.append(((a_x * xrr[-2] + b_x * xrr[-1] + c_x) % d_x))
        yrr.append(((a_y * yrr[-2] + b_y * yrr[-1] + c_y) % d_y))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(srr, xrr, yrr)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)


