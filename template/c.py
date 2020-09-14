import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    console("----- solving ------")

    if len(lst) <= 2:
        return lst[0]

    dp = [[10**10, 10**10] for _ in lst]

    if lst[0] == 0:
        dp[0][0] = 0
    else:
        dp[0][0] = 1

    if lst[1] == 0:
        dp[1][0] = 0 + dp[0][0]
    else:
        dp[1][0] = 1 + dp[0][0]

    dp[1][1] = dp[0][0]

    for i in range(2,len(lst)):
        dp[i][1] = min(dp[i-1][0], 
                       dp[i-2][0])
        dp[i][0] = min(dp[i-1][1] + lst[i], 
                       dp[i-2][1] + lst[i] + lst[i-1])

    # console(dp)

    return min(dp[-1][1], dp[-1][0])


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()

for case_num in range(int(inp[0])):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,inp[2*case_num+2].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
