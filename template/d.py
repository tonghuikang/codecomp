#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


k = 2*10**5 + 100

dp_one = [0]*(k+15)
dp_zero = [0]*(k+15)
dp_one[0] = 1
dp_zero[0] = 0

for i in range(k+10):
    dp_one[i+1] = (dp_zero[i] + dp_one[i]) % M9
    dp_zero[i+2] = (dp_zero[i] + dp_one[i]) % M9

cursum = [0]*(k+10)
cursum[0] = 1
for i in range(1, k+5):
    cursum[i] = (dp_one[i] + dp_zero[i] + cursum[i-1]) % M9

# log(dp_one[:10])
# log(dp_zero[:10])
# log(cursum[:10])
# log(dp_one[-10])
# log(dp_zero[-10])



def solve_(arr, p):
    # your solution here

    curset = set(arr)
    newset = []

    for x in arr:
        ox = x
        flag = True
        while x and flag:
            if x%2 == 1:
                x = x // 2
                if x in curset:
                    flag = False
            elif x%4 == 0:
                x = x // 4
                if x in curset:
                    flag = False
            else:
                break
        if flag:
            newset.append(ox)

    # log(newset)

    res = 0

    for x in newset:
        binlen = len(bin(x)) - 2
        if binlen > p:
            continue
        idx = p - binlen
        # log(x, binlen, idx, cursum[idx])
        res += cursum[idx]

    return res%M9

    # number of ways to put one and double zeroes

    # log(newset)


    # stack = arr
    # while stack:
    #     x = stack.pop()
    #     a,b = 2*x + 1, 4*x

    #     if a < limit and a not in curset:
    #         curset.add(a)
    #         stack.append(a)

    #     if b < limit and b not in curset:
    #         curset.add(b)
    #         stack.append(b)

    # if p <= 30:
    #     res = 0
    #     actual_limit = 2**p
    #     for x in curset:
    #         if x < actual_limit:
    #             res += 1
    #     return res


# log(solve_(list(range(1,2*10**5)), 30))


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,p = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, p)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
