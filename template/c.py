import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(n,a,b):  # fix inputs here
    console("----- solving ------")

    b,a = sorted([a,b])

    '''
    sum of matrix of size ?
    1 2 3 4 5
    2 3 4 5 6
    3 4 5 6 7
    4 5 6 7 8
    5 6 7 8 9
    '''

    '''
    sum of matrix of size ?
    1 2 3 4 5
    1 2 3 4 5
    '''

    # possible start points of A * possible start points of B
    unrestricted = (n-b-a+1)*(n-b-a+1)*(a+b-1)*(a+b-1)

    one_restricted = (n-b-a+1)*(a+b-1)*(b)*(a + a+b-1)//2

    two_restricted = 0

    res = unrestricted + one_restricted + two_restricted

    # return a string (i.e. not a list or matrix)
    return res%(10**9+7)


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

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(a,b,c)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
