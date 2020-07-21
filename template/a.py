import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

# def longestCommonSubsequence(A, B):
#     n, m = len(A), len(B)
#     dp = [[0] * (m) for i in range(n)]
#     for i in range(n):
#       for j in range(m):
#         # value condition
#         dp[i][j] = int(A[i] == B[j])
#         if i>0 and j>0: 
#           dp[i][j] += max(dp[i - 1][j - 1], 0)
#         if i>0:
#           dp[i][j] = max(dp[i][j], dp[i - 1][j])
#         if j>0:
#           dp[i][j] = max(dp[i][j], dp[i][j - 1])
#     return dp[-1][-1]


def solve(a,b):  # fix inputs here
    console("----- solving ------")

    interset = set(a) & set(b)
    if not interset:
        print("NO")
        return

    if interset:
        print("YES")
        print("1 {}".format(list(interset)[0]))
    # return a string (i.e. not a list or matrix)
    return None


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
    _ = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    _ = solve(arr, brr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
