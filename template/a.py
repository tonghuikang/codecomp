import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(x):  # fix inputs here
    console("----- solving ------")

    res = defaultdict(set)
    for a in range(1, int(math.sqrt(x))):
        for b in range(1, int(math.sqrt(x - a*a))):
            for c in range(1, int(math.sqrt(x - a*a - b*b))):
                total = a**2 + b**2 + c**2 + a*b + b*c + a*c
                res[total].add(tuple(sorted([a,b,c])))

    for i in range(1,x+1):
        console(i, res[i])
        cnt = 0
        for a,b,c in res[i]:
            if a == b == c:
                cnt += 1
            elif a == b:
                cnt += 3
            elif b == c:
                cnt += 3
            else:
                cnt += 6
        print(cnt)
    return None


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
k = int(input())
    
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

solve(k)
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
