import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(n,x,m):  # fix inputs here
    console("----- solving ------")
    if m == 1:
        return 0

    arr = [x]
    pos = {}

    for i in range(min(n-1, 2*m)):
        x = arr[-1]
        new = (x*x)%m
        if new in pos:
            break
        pos[new] = i           
        arr.append(new)

    sumarr = sum(arr)
    lenarr = len(arr)

    if len(arr) == n:
        console(arr)
        return sumarr

    m = len(arr) - pos[new] - 1

    cycles = (n-lenarr) // (m)
    remainder = (n-lenarr) % (m)

    console(m, cycles, remainder)
    sumarr += cycles*sum(arr[-m:])
    sumarr += sum(arr[-m:-m+remainder])

    console(492443256176507 - sumarr)
    # return a string (i.e. not a list or matrix)
    return sumarr 


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
    n,x,m = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(n,x,m)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
