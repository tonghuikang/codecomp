#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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



def binary_search(func_,       # condition function
                  first=True,  # else last
                  target=True, # else False
                  left=0, right=2**31-1) -> int:
    # https://leetcode.com/discuss/general-discussion/786126/
    # ASSUMES THAT THERE IS A TRANSITION
    # MAY HAVE ISSUES AT THE EXTREMES

    def func(val):
        # if first True or last False, assume search space is in form
        # [False, ..., False, True, ..., True]

        # if first False or last True, assume search space is in form
        # [True, ..., True, False, ..., False]
        # for this case, func will now be negated
        if first^target:
            return not func_(val)
        return func_(val)

    while left < right:
        mid = (left + right) // 2
        if func(mid):
            right = mid
        else:
            left = mid + 1
    if first:  # find first True
        return left
    else:      # find last False
        return left-1



def solve_(arr, n, k):
    assert len(arr) == n-1
    # your solution here
    arr = [-1] + [x-1 for x in arr]
    # log(arr)

    depth = [0 for _ in range(n)]
    for cur in range(n-1, 0, -1):
        parent = arr[cur]
        depth[parent] = depth[cur] + 1
                
    log(depth)
    
    def func(h):
        # whether the number of ops needed to achieve h is less than k
        cnt = 0
        depth = [0 for _ in range(n)]
        for cur in range(n-1, 0, -1):
            parent = arr[cur]
            if parent != 0:
                if depth[cur] + 1 >= h:
                    cnt += 1
                else:
                    depth[parent] = depth[cur] + 1
            else:
                depth[parent] = depth[cur] + 1
        assert max(depth) <= h
        log(h, depth, cnt)
        return cnt <= k

    for h in range(1,12):
        log(h, func(h))
        log()

    return binary_search(func, first=True, target=True, left=1, right=n)

# flag = True
# debug = False

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    
    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    # if flag:
    #     flag = False
    #     if n == 2 and k == 1:
    #         debug = True

    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, n, k)  # include input here

    # if case_num == 2062 and debug:
        # 1,2,2,4,2,4,4,3,3,10,8,1,6|1|3
        # strr = str(",".join(str(x) for x in arr) + "|" + str(k) + "|" + str(res)).replace(" ", "")
        # print(strr)

    # strr = str(",".join(str(x) for x in arr) + "|" + str(k) + "|" + str(res)).replace(" ", "")
    # print(strr)
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)