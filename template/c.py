import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

MOD = 998244353

def solve(k, grid):  # fix inputs here
    console("----- solving ------")
    console(grid)
    ways = [1]
    psum = [0,1]
    ps = 1

    for i in range(1,k):
        cur = 0
        for a,b in grid:
            if a > i:
                continue
            if b > i:
                b = i
            console(i-a+1,i-b,i)
            cur += psum[i-a+1] - psum[i-b]

        console()
        console(i, cur, ways, psum)
        console()
         
        ways.append(cur%MOD)
        ps += cur
        psum.append(ps%MOD)


    # return a string (i.e. not a list or matrix)
    return ways[-1]%MOD


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    k, nrows = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(k, grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
