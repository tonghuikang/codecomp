import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst, k, z):  # fix inputs here
    console("----- solving ------")
    console(k,z)
    console("lst", lst)
    lst_rev = lst[::-1]

    arr = []
    cs = 0
    for i in lst:
        cs += i
        arr.append(cs)
    console("arr", arr)

    lst = lst[:k+1]
    maxres = sum(lst)
    
    if z == 0:
        return maxres

    z = min(z, k//2)

    for i in range(z):
        lst.pop()
        # lst.pop()
        # get largest sliding window
        brr = [a+b for a,b in zip(lst,lst[1:])]

        curres = sum(lst[:-1]) + max(brr)*(i+1)
        maxres = max(maxres, curres)

        console()
        console(i)
        console("lst", lst)
        console("brr", brr)
        console(curres)
        console()

        lst.pop()

    # return a string (i.e. not a list or matrix)
    return maxres


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
    _, k, z = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst, k, z)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
