import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy



def solve(lst):  # fix inputs here
    # console("----- solving ------")
    console(lst)
    res = 0

    for threshold in list(range(1, min(5000+1, 1+len(lst))))[::-1]:
        height = 1
        cur = 0
        start = 10**4
        for i in range(len(lst)):
            console(threshold, height, cur, i, start, lst, res)
            if lst[i] == threshold:
                if cur == 0:
                    start = i
                cur += 1
            if lst[i] < threshold:
                if cur >= threshold:
                    res += threshold
                    for j in range(start, i):
                        cur = 0
                        lst[j] -= threshold
                        start = 10**4
                else:
                    cur = 0
                    start = 10**4
        if start < 10**4:
            if cur >= threshold:
                console(cur, i, height, res, start)
                res += threshold
                for j in range(start, len(lst)):
                    cur = 0
                    lst[j] -= threshold

    for x in lst:
        if x > 0:
            res += 1

    # return a string (i.e. not a list or matrix)
    return res


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,inp[1].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
