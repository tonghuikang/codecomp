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
OFFLINE_TEST = getpass.getuser() == "hkmac"
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


def solve_(arr):
    # your solution here

    if sum(arr) == 0:
        return []

    if arr.count(0) == 0:
        return -1

    if sum(arr)%2 == 1:
        return -1

    left_ones = 0
    res = []

    for i in range(len(arr)):
        x = arr[i]
        log(i, x, left_ones)
        log(arr)
        if x == 0:
            if left_ones == 0:
                continue

            if left_ones%2 == 0:
                j = i-2
                while j >= 0 and arr[j] == 1:
                    assert arr[j] == 1
                    assert arr[j+1] == 1
                    assert arr[j+2] == 0
                    arr[j], arr[j+1], arr[j+2] = 0,0,0
                    res.append(j)
                    j -= 2

            else:
                # delete 101

                # cannot pair
                if i + 1 == len(arr):
                    return -1
                if arr[i+1] != 1:
                    return -1

                assert arr[i-1] == 1
                assert arr[i] == 0
                assert arr[i+1] == 1
                arr[i-1], arr[i], arr[i+1] = 0,0,0
                res.append(i-1)

                j = i-3
                while j >= 0 and arr[j] == 1:
                    assert arr[j] == 1
                    assert arr[j+1] == 1
                    assert arr[j+2] == 0
                    arr[j], arr[j+1], arr[j+2] = 0,0,0
                    res.append(j)
                    j -= 2

            left_ones = 0

        else:
            left_ones += 1

    log(arr)
    sumarr = sum(arr)

    if sumarr == 0:
        return res

    if sumarr%2 == 1:
        return -1

    assert arr[0] == 0
    for i in range(len(arr)):
        if arr[i] == 1:
            assert arr[i-1] == 0
            assert arr[i] == 1
            assert arr[i+1] == 1
            arr[i-1], arr[i], arr[i+1] = 0,0,0
            res.append(i-1)

    assert sum(arr) == 0

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(lst)  # include input here

    if res == -1:
        print("NO")
        continue

    print("YES")
    print(len(res))
    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x + 1) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
