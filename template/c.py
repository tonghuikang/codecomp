import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, end):  # fix inputs here
    console("----- solving ------")

    arr = [0] + arr + [end]
    brr = [end - x for x in arr[::-1]]

    xrr = [(b-a)/i for i,(a,b) in enumerate(zip(arr, arr[1:]), start=1)]
    yrr = [(b-a)/i for i,(a,b) in enumerate(zip(brr, brr[1:]), start=1)]

    cur = 0
    crr = [0]
    for x in xrr:
        cur += x
        crr.append(cur)

    dur = 0
    drr = [0]
    for y in yrr:
        dur += y
        drr.append(dur)
    drr = drr[::-1]

    del cur, dur

    console(arr)
    console(brr)
    console(xrr)
    console(yrr)
    console(crr)
    console(drr)


    for i,(c,d) in enumerate(zip(crr,drr)):
        if c == d or abs(c-d) < 10**-7:
            return c
        if c > d:
            p = crr[i-1]
            q = drr[i]
            x = i
            y = len(arr)-i
            a = arr[i-1]
            b = arr[i]
            console(p,q,x,y,a,b)
            return (b-a + x*p+y*q)/(x+y)

    # for x in xrr:


    # return a string (i.e. not a list or matrix)
    return ""  


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
    _, end = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst, end)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
