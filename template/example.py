import sys
import heapq
import random
import collections

# available on Google, not available on Codeforces
# import numpy as np
# import scipy
from scipy.stats import binom


def solve(*args):
    console("----- solving ------")
    console(*args)
    console("----- ------- ------")
    return solve_(*args)


def solve_(w,h,l,u,r,d):
    res = 0
    # 6,4,1,3,3,4
    if u-2 >= 0 and w > r:
        # binom.cdf(1, 4, 0.5) # 1 = u-2 = 3-2, 4 = r+u-2 = 3+3-2
        res += binom.cdf(u-2, r+u-2, 0.5)
    if l-2 >= 0 and h > d:
        res += binom.cdf(l-2, d+l-2, 0.5)
    
    return res



def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    w,h,l,u,r,d = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(w,h,l,u,r,d)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)


