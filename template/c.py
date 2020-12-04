import sys, os, getpass
# import heapq as hq
# import math, random, functools, itertools
# from collections import Counter, defaultdict, deque
from collections import Counter, defaultdict
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(k):
    # your solution here
    
    d = defaultdict(list)

    for i in range(k):
        row = [int(x) for x in input().strip()]
        for j,digit in enumerate(row):
            d[digit].append((i,j))

    # log(d)

    length = k-1

    res = []

    for i in range(10):
        lst = d[i]
        if len(lst) <= 1:
            res.append(0)
            continue

        # log(i, lst)

        cur = 0
        for _ in range(4):  # rotate 4 times
            # get top most and bottom most
            top = max(x[1] for x in lst)
            bottom = min(x[1] for x in lst)
        
            for x,y in lst:
                cur = max(cur, (length - x)*abs(top-y), (length - x)*abs(bottom-y))
            
            lst = [(length-y, x) for x,y in lst]
            # log(i, lst)

        res.append(cur)
    # log(res)

    return res


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# for case_num in [1]:  # no loop over test case
for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))  # if printing length of list
    print(*res)  # if printing a list