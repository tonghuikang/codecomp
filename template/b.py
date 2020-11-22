import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(strr,k):
    # your solution here
    
    for s in strr:
        if s == "o":
            k += 1
        else:
            k = max(0, k-1)

    return k


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    if not ONLINE_JUDGE:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _,k = list(map(int,input().split()))
    strr = input().strip()

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(strr,k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list