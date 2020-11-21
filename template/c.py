import sys, os
# import heapq, functools, collections
# import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(arr,brr,k):
    # your solution here

    x = Counter(arr)
    y = Counter(brr)

    for bef,aft in zip("abcdefghijklmnopqrstuvwxy", "bcdefghijklmnopqrstuvwxyz"):
        if y[bef] > x[bef]:
            return "No"
        deductible = x[bef] - y[bef]
        if deductible == 0:
            continue
        if deductible%k != 0:
            return "No"
        x[bef] -= deductible
        x[aft] += deductible

    return "Yes"


# def console(*args):  
#     # print on terminal in different color
#     print('\033[36m', *args, '\033[0m', file=sys.stderr)
#     pass


# ONLINE_JUDGE = False

# if Codeforces environment
# if os.path.exists('input.txt'):
#     ONLINE_JUDGE = True

# if ONLINE_JUDGE:
#     sys.stdin = open("input.txt","r")
#     sys.stdout = open("output.txt","w")

#     def console(*args):
#         pass


def solve(*args):
    # screen input
    # if not ONLINE_JUDGE:
    #     console("----- solving ------")
    #     console(*args)
    #     console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.readline


for case_num in range(int(input())):

    _,k = list(map(int,input().split()))
    # read line as a string
    arr = input()
    brr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    # print(arr)
    res = solve(arr,brr,k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list