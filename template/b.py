import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(l,r,m):  # fix inputs here
    console("----- solving ------")

    d = r-l

    for i in range(l,r+1):  # guess a
        remainder = m%i
        # console(m//i)
        if m//i != 0:  # n is non-zero
            # continue
            if 0 <= remainder <= d:  # positive remainder
                return [i,l+remainder,l]
            # if 0 <= i-remainder <= d:
            #     return [i,l,l+remainder]

        # if i == r:
        #     continue
        # console(m//i + 1)
        remainder = i-m%i
        # console(remainder)
        # if remainder == m:
        #     continue
        if 0 <= remainder <= d:
            return [i,l,l+remainder]
        
    # console("no guess")


    # console("guess n")
    # for i in range(1,500001):  # guess n
    #     quotient, remainder = m//i, m%i
    #     if l <= quotient <= r:
    #         if 0 <= remainder <= d:
    #             return [quotient,l+remainder,l]
    #         if 0 <= i-remainder <= d:
    #             return [quotient,l,l+remainder]
    
    # return a string (i.e. not a list or matrix)
    return []


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
    l,r,m = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(l,r,m)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(" ".join([str(x) for x in res]))
