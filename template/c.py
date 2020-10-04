import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


MOD = 10**9 + 7

def solve(arr):  # fix inputs here
    console("----- solving ------")

    values = []
    value = 1
    for a in arr[::-1]:
        values.append(value*int(a))
        value = (value*10)%MOD

    console(values)

    suffix = []
    cumsum = 0
    for a in values:
        cumsum += a
        cumsum = cumsum%MOD
        suffix.append(cumsum)

    suffix = suffix[::-1]
    console(suffix)

    res = 0

    cnt = 0
    i = 1
    for x in suffix[1:]:
        console(i, x)
        res += x*i
        i += 1

    res = res%MOD
    
    i = len(arr)
    for x in suffix[:]:
        console(i, x)
        res -= x*i
        cnt += i
        i -= 1

    res = res%MOD
    console(cnt, suffix[0])
    res += cnt*suffix[0]

    return res%MOD


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(strr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
