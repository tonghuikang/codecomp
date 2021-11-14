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

# https://github.com/cheran-senthil/PyRival/blob/3795f54e42d77f67bf065fd5ca3841da6ab3e4b7/pyrival/graphs/lca.py
class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])


def solve_(arr):
    # your solution here

    arr = [-x if i%2 else x for i,x in enumerate(arr)]
    log(arr)

    minval = 10**18
    cur = 0
    for x in arr:
        x += cur


    count = defaultdict(list)
    count[0].append(0)
    cur = 0
    res = 0
    for i,v in enumerate(arr, start=1):
        cur += v
        res += len(count[cur])
        count[cur].append(i)

    # log(count)

    return res



    arr = [10**17, 2*10**17] + arr + [4*10**17, 8*10**17]

    start_to_end = {}

    left = 1
    right = left+1  # exclusive
    leftover = arr[left]

    while left < len(arr)-1 and right < len(arr):
        if leftover > arr[right]:  # cannot cover
            left = right
            leftover = arr[left]
            right = left+1

        elif leftover == arr[right]:
            start_to_end[left] = right+1   # record jump
            left = right+1
            leftover = arr[left]
            right = left+1

        else:
            leftover = arr[right] - leftover
            right += 1

    log(start_to_end)


    left = 1
    right = left+1  # exclusive
    leftover = arr[left]

    while left < len(arr)-1 and right < len(arr):
        if leftover > arr[right]:  # cannot cover
            left = right
            leftover = arr[left]
            right = left+1

        elif leftover == arr[right]:
            start_to_end[left] = right+1   # record jump
            left = right+1
            leftover = arr[left]
            right = left+1

        else:
            leftover = arr[right] - leftover
            right += 1



    return ""


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
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
