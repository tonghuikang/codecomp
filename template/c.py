import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

OFFLINE_TEST = getpass.getuser() == "hkmac"
def console(*args):  # print on terminal in different color
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(arr,n,p,k,x,y):
    # your solution here
    p = p-1

    minres = 10**9
    for i in range(k):
        lst = arr[p+i::k]

        if not lst:
            continue

        curres = res = i*y + sum(lst)*x
        console(res)

        for z in lst:
            res += k*y
            if z == 1:
                res -= z
            console(res)
            curres = min(res, curres)

        console(i, lst, curres)

        minres = min(curres, minres)

    return minres


# print(getpass.getuser())

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
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
    # k = int(input())
    
    # read one line and parse each word as an integer
    n,p,k = list(map(int,input().split()))
    strr = [1-int(x) for x in input().strip()]
    x,y = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(strr,n,p,k,x,y)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list