import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(srr, k):  # fix inputs here
    console("----- solving ------")
    console(srr, k)

    ones = 0
    zeroes = 0

    for i in range(k):
        sett = set(srr[i::k])
        if "1" in sett and "0" in sett:
            return "NO"
        if "1" in sett:
            ones += 1
        if "0" in sett:
            zeroes += 1

    if ones > k // 2 or zeroes > k // 2:
        return "NO"

    return "YES"


def console(*args):  # the judge will not read these print statement
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

    # read one line and parse each word as an integer
    _, k = list(map(int,input().split()))
    srr = input()

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(srr, k)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
