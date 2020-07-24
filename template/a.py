import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, brr, size):  # fix inputs here
    # console("----- solving ------")
    # console(arr)
    # console(brr)

    crr = []
    drr = []

    for i in range(size):
        cnt = 0
        for a,b in zip(arr[i+1:],brr[i:]):
            if not (a == "Y" and b == "Y"):
                break
            cnt += 1
        crr.append(cnt)

        cnt = 0
        for a,b in zip(arr[::-1][i+1:],brr[::-1][i:]):
            if not (a == "Y" and b == "Y"):
                break
            cnt += 1
        drr.append(cnt)

    drr = drr[::-1]
    # console(crr, drr)

    grid = [["N" for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        grid[i][i] = "Y"

    for i in range(size):
        for k in range(crr[i]):
            grid[i][i+k+1] = "Y"

    for i in range(size):
        for k in range(drr[i]):
            grid[i][i-k-1] = "Y"

    for row in grid:
        print("".join(row))

    return


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as a string
    arr = input()
    brr = input()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    
    # Google - case number required
    print("Case #{}:".format(case_num+1))
    solve(arr, brr, k)  # please change

    # Codeforces - no case number required
    # print(res)
