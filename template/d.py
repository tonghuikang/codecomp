import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, brr, burn, width, snipe):  # fix inputs here
    console("----- solving ------")
    console(arr, brr, burn, width, snipe)

    idx = 0
    sub = []
    prev = 0
    for b in brr:
        while idx < len(arr) and arr[idx] != b:
            idx += 1
        if idx == len(arr):
            return -1
        # console(prev, idx)
        sub.append((arr[prev:idx]))
        prev = idx+1
    # console(prev, idx)
    sub.append(arr[prev:])

    console(sub)
    
    brr = [0] + brr + [0]

    sub = [(a,b,c) for a,b,c in zip(brr, sub, brr[1:])]
        
    res = 0
    for a,b,c in sub:
        if len(b) < width:
            if max(b) > a and max(b) > c:
                return -1  # cannot snipe
            res += snipe*len(b)
            continue  # cleared
        # if cheaper to snipe and can snipe all, carry on
        if snipe < burn:
            if not (max(b) > a and max(b) > c):  # if possible to snipe all
                res += snipe*len(b)
                continue
        # burn all necessary
        # cnt = 0
        # for bb in b:
        #     if 

        # remove remaining by sniping or burning

    # return a string (i.e. not a list or matrix)
    return res


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
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
    _ = list(map(int,input().split()))
    burn, width, snipe = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(arr, brr, burn, width, snipe)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
