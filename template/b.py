import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst, k, l):  # fix inputs here
    console("----- solving ------")
    lst = [l-x for x in lst]
    console(k, lst)

    # jigsaw = []
    # for _ in range(len(lst) // k + 1):
    #     jigsaw += list(range(k)) + list(range(k,0,-1)) 
    # console(jigsaw)

    def jigsaw(t):
        if t <= k:
            return t
        return (k - (2*k)-t)

    # for i in range(2*k + 1):
    #     for a,b in zip(lst, jigsaw[i:]):
    #         if a+b > 0:
    #             break
    #     else:
    #         return "Yes"

    depth = lst  # more of allowance

    console("check")
    called = set()

    def dfs(x, t):
        if x == len(lst):
            return True

        if x >= 0 and depth[x] - jigsaw(t) < 0:
            return False

        if dfs(x+1, (t+1)%(2*k)):
            return True

        if (x,t) in called:
            return False
        called.add((x,t))

        incr = 1
        if dfs(x, (t+incr)%(2*k)):
            return True
        
        return False

    if dfs(-1,1):
        return "Yes"
    
    return "No"


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
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
    _, k, l = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst, k, l)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
