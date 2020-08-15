import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, brr, crr):  # fix inputs here
    console("----- solving ------")

    a,b,c = len(arr),len(brr),len(crr)
    arr, brr, crr = sorted([arr, brr, crr], key=len)
    # return a string (i.e. not a list or matrix)

    arr = sorted(arr)
    brr = sorted(brr)
    crr = sorted(crr)[::-1]

    console(arr)
    console(brr)
    console(crr)

    if len(arr) + len(brr) <= len(crr):
        drr = sorted(arr + brr)[::-1]
        crr = sorted(crr)[::-1]
        return sum([x*y for x,y in zip(drr,crr)])

    res = [-1 for i in range(600)]

    res[0:3*len(crr):3] = crr
    res[1:3*len(brr):3] = brr
    res[2:3*len(arr):3] = arr

    console(res[:10])

    result = 0
    prev = None
    for a in res:
        if a == -1 and prev == -1:
            return result
        if prev == None:
            prev = a
            continue
        else:
            result += a*prev
            prev = None
        

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
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    crr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(arr, brr, crr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
