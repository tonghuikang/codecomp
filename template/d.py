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
    crr = sorted(crr)

    console(arr)
    console(brr)
    console(crr)

    if len(arr) + len(brr) <= len(crr):
        drr = sorted(arr + brr)[::-1]
        crr = sorted(crr)[::-1]
        return sum([x*y for x,y in zip(drr,crr)])

    maxres = 0

    for i in range(200):  # ac matches
        if i > c or i > a:
            continue
        for j in range(200):  # bc matches
            if j > c or j > b:
                continue
            if i + j > c:
                continue
            k = min(a-i, b-j)  # ab matches
            console("budget", i,j,k)

            ar = [0] + arr.copy()
            br = [0] + brr.copy()
            cr = [0] + crr.copy()

            ax = ar.pop()
            bx = br.pop()
            cx = cr.pop()

            res = 0
            while (ax == 0) + (bx == 0) + (cx == 0) <= 1:
                console(i,j,k,ax,bx,cx)
                if cx == 0 or (min(ax,bx,cx) == cx and k > 0):
                    console("ab")
                    res += ax * bx
                    k -= 1
                    ax = ar.pop()
                    bx = br.pop()                    
                    continue

                if bx == 0 or (min(ax,bx,cx) == bx and i > 0):
                    console("ac")
                    res += ax * cx
                    i -= 1
                    ax = ar.pop()
                    cx = cr.pop()                    
                    continue

                else:
                    console("bc")
                    res += bx * cx
                    j -= 1
                    bx = br.pop()
                    cx = cr.pop()                    
                    continue                    

        console(res)
        maxres = max(maxres, res)
    return maxres


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
