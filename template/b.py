import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

import math

def prime_factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if i > math.sqrt(nr):
            i = nr
        if (nr % i) == 0:
            factors.append(int(i))
            nr = nr / i
        elif i == 2:
            i = 3
        else:
            i = i + 2
    return factors


def solve(k):  # fix inputs here
    console("----- solving ------")

    if k%2 == 0:
        return "{} {}".format(k//2, k//2)

    if k%3 == 0:
        return "{} {}".format(k//3, 2*k//3)

    lst = sorted(list(set(prime_factors(k))))
    console(lst)
    if len(lst) > 1:
        f = lst[0]
        return "{} {}".format(k//f, (f-1)*k//f)

    return "{} {}".format(1, k-1)


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
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

    res = solve(k)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
