import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(n,a,b,c):  # fix inputs here
    console("----- solving ------")
    console(n, a, b, c)
    console(n, a, c, b)

    assert 1 <= c <= a <= n
    assert 1 <= c <= b <= n

    if a == b == c == n:
        console("a=b=c=n")
        return [1]*n

    if a == b == 1:
        console("a=b=1")
        return ["IMPOSSIBLE"]

    if n == 2:
        console("n=2")
        # a == b == c case covered
        if a == 1 and b == 2 and c == 1:
            return [2, 1]
        if a == 2 and b == 1 and c == 1:
            return [1, 2]
        return ["IMPOSSIBLE"]

    a_only = a-c
    b_only = b-c

    if a_only+b_only+c > n:
        console("a_only+b_only+c > n")
        return ["IMPOSSIBLE"]

    nobody = n - (a_only+b_only+c)


    console(nobody, a_only, c, b_only)
    
    if a_only == 0 and b_only == 0:
        return [2] + [1]*nobody + [2]*(c-2) + [2]
    if a_only > 0:
        return [2]*a_only + [1]*nobody + [3]*c + [2]*b_only
    else:
        return [2]*a_only + [3]*c + [1]*nobody + [2]*b_only


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
    n,a,b,c = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(n,a,b,c)  # please change
    
    if res == ["IMPOSSIBLE"]:
        pass
    else:
        pass

    # Google - case number required
    print("Case #{}: {}".format(case_num+1, " ".join(str(x) for x in res)))

    # Codeforces - no case number required
    # print(res)
