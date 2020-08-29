import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

# import matplotlib.pyplot as plt
# import matplotlib.patches as patches

# plotting = False
debugging = False
debugging = True

def solve(n, p_elim):  # fix inputs here
    console("--- solving ---")
    console(n,p_elim)

    standing = [1 for _ in range(n)]
    res = [0 for _ in range(n)]

    for i in range(n-1):
        # console()

        cs = 0
        # psum = [0]
        total_prob = sum(standing)

        # for s in standing:
        #     cs += s/total_prob
        #     psum.append(cs)
        # p_win = [psum[i]/(1-standing[i]/total_prob) for i,x in enumerate(standing)]  # ???

        p_win = [sum(standing[:i])/(total_prob-standing[i]) for i,x in enumerate(standing)]  # ???

        console("standing", standing)
        console("standing", p_win)
        # console("average_win_rate", sum([p*(total_prob-s)/total_prob for p,s in zip(p_win,standing)]))
        # console(psum)
        # console(res)

        res = [r+s for r,s in zip(res,standing)]
        # p_select = 2/total_prob
        p_select = 2/(n-i)
        standing = [s - p_select*s*(1-p)*(p_elim) - p_select*s*(p)*(1-p_elim) for s,p in zip(standing, p_win)]
        console("sum(standing)", sum(standing))

    console("sum(res)", sum(res), n*(n+1)/2 - 1)
    return res


def console(*args):  # the judge will not read these print statement
    if debugging:
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

    # read matrix and parse as integers (after reading read nrows)
    n, p = list(map(float,input().split()))
    n = int(n)
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(n,p)  # please change
    
    # Google - case number required
    print("Case #{}:".format(case_num+1))
    for r in res:
        print("{:.8f}".format(r))

    # Codeforces - no case number required
    # print(res)


