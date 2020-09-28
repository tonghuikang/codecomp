import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid, k):  # fix inputs here
    console("----- solving ------")

    console(grid, k)

    if k%2:
        return "NO"

    # return a string (i.e. not a list or matrix)
    g = set()
    check_1 = False    
    check_2 = False    

    for (a,b),(c,d) in grid:
        if a == d and c == b:
            return "YES"
        if (a,c,b,d) in g:
            check_1 = True
        if c == b:
            check_2 = True
        g.add((a,b,c,d))

    console(g)
    console(k, check_1, check_2)

    if k == 2:
        if check_2:
            return "YES"

    if check_1 and check_2 and k > 2:
        return "YES"

    return "NO"  


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
    nrows, k = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        arr = []
        arr.append(list(map(int,input().split())))
        arr.append(list(map(int,input().split())))
        grid.append(arr)

    res = solve(grid, k)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
