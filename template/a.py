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


def solve_(given):
    # your solution here
    given = [list(x) for x in given]
    arr = [sorted(list(x)) for x in given]
    log(arr)
    allres = [arr[0]]

    prev = arr[0]
    for xrr in arr[1:]:
        if prev > xrr[::-1]:
            return []

        res = []
        flag = False
        for x in prev:
            for y in xrr:
                if y >= x:
                    xrr.remove(y)
                    res.append(y)
                    if y != x:
                        res.extend(sorted(xrr))
                        flag = True
                    break
            if flag:
                break

        allres.append(res)
        log(prev, res)
        prev = res

    log()
    log(allres)
    log(given)
    assert len(given) == len(allres)
    for a,b in zip(given, allres):
        assert sorted(a) == sorted(b)
    for a,b in zip(allres, allres[1:]):
        assert a <= b

    return allres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here
    if res == []:
        print("Case #{}: {}".format(case_num+1, "IMPOSSIBLE"))   # Google and Facebook - case number required
        continue
    # print length if applicable
    # print(len(res))

    print("Case #{}: {}".format(case_num+1, "POSSIBLE"))   # Google and Facebook - case number required

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = " ".join("".join(str(x) for x in row) for row in res)

    # print result

    print(res)
