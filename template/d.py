import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst,k):  # fix inputs here
    console("----- solving ------")

    MOD = 10**9 + 7

    lst = lst[:len(lst)//2] + lst[len(lst)//2:]
    lst = sorted(lst, key=lambda x: abs(x))[::-1]
    sign = [0 if x == 0 else x//abs(x) for x in lst]

    console(lst)
    console(sign)

    # no choice negative
    if all([x == -1 for x in sign]) and k%2 == 1:
        res = 1
        for i in lst[::-1][:k]:
            res = (res*i)%MOD 
        return res

    # no choice take all
    if k == len(lst):
        res = 1
        for i in lst:
            res = (res*i)%MOD 
        return res

    # not enough nonzeros
    if lst[k-1] == 0:
        return 0

    # if hangover
    if abs(lst[k]) == abs(lst[k-1]):
        val = abs(lst[k])
        c = Counter(lst)
        if c[val] == 0 or c[-val] == 0:   # no choice anyway
            pass
        else:
            initial_sign = 1
            for i in sign[:k]:
                initial_sign = initial_sign*i
            if initial_sign == 1:
                res = 1
            else:
                res = -1
            for i in lst[:k]:
                res = (res*i)%MOD
            return res


    pos = max(lst[k-1:])
    neg = min(lst[k-1:])

    initial_sign = 1
    for i in sign[:k-1]:
        initial_sign = initial_sign*i

    if initial_sign == 1:
        res = pos
        for i in lst[:k-1]:
            res = (res*i)%MOD
        return res

    if initial_sign == -1:
        res = neg
        for i in lst[:k-1]:
            res = (res*i)%MOD
        return res

    # return a string (i.e. not a list or matrix)
    return 0


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _,k = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst,k)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
