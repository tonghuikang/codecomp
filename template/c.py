import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr):  # fix inputs here
    console("----- solving ------")

    c = Counter(arr)

    res = max(c.values())

    for a in range(10):
        a = str(a)

        for b in range(10):
            b = str(b)
            if a == b:
                continue
        
            sets = 0
            expect_b = False
            for x in arr:
                if expect_b and x == b:
                        expect_b = False
                        sets += 1
                elif x == a:
                    expect_b = True

            res = max(res, sets*2)

    return len(arr) - res


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
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
