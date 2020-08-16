import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

def solve(arr):  # fix inputs here
    console("----- solving ------")
    minres = 10**9
    for i in range(min(4, len(arr))):
        minres = min(minres, solve2(arr[i:] + arr[:i]))
    return minres

@functools.lru_cache()
def diff(given, desired):
    return sum([a != b for a,b in zip(given, desired)])

def solve2(arr):  # fix inputs here

    # approved patterns
    # RRLL RL RRL RLL

    # assume start starts isolation
    dp = [0] + [10**9 for _ in arr]

    for i in range(len(arr)):
        if i+4 <= len(arr):
            dp[i+4] = min(dp[i+4], dp[i] + diff("RRLL", arr[i:i+4]))
        if i+3 <= len(arr):
            dp[i+3] = min(dp[i+3], dp[i] + diff("RLL", arr[i:i+3]))
            dp[i+3] = min(dp[i+3], dp[i] + diff("RRL", arr[i:i+3]))
        if i+2 <= len(arr):
            dp[i+2] = min(dp[i+2], dp[i] + diff("RL", arr[i:i+2]))

    return dp[-1]


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# lines = sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    _ = input()
    strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(strr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
