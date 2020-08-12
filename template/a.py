import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(a,b,c,d):  # fix inputs here
    console("----- solving ------")
    console(a,b,c,d)
    console(a%2 == 1, b%2 == 1, c%2 == 1, d%2 == 1)
    console(a%2 == 1 + b%2 == 1 + c%2 == 1 + d%2 == 1)
    if ((a%2 == 1) + (b%2 == 1) + (c%2 == 1) + (d%2 == 1)) <= 1:
        console("default")
        return "Yes"

    maxx = min(a,b,c)
    
    for val in range(20):
        if val <= maxx:
            if (((a-val)%2 == 1) + ((b-val)%2 == 1) + ((c-val)%2 == 1) + ((d+3*val)%2 == 1)) <= 1:
                console("val", val)
                return "Yes"

    # return a string (i.e. not a list or matrix)
    return "No"  


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
    a,b,c,d = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(a,b,c,d)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
