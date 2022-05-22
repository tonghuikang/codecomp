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

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

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


def solve_(srr, n):
    # your solution here

    arr = [int(x) for x in srr]
    degrees = sum(arr)

    if degrees%2 == 1:
        # pairity not possible
        return []

    if arr.count(1) < 2:
        # a tree has at least two leaves
        return []

    # for i,x in enumerate(arr):

    # there is always an even number of odds
    # if all are odd, just connect all to one
    if degrees == k:
        res = []
        for i in range(1,k):
            res.append((0,i))
        return res

    iteration = list(range(k)) + list(range(k)) + list(range(k))

    for i,j in zip(iteration, iteration[1:]):
        i = i%n
        j = j%n
        if arr[i] == 0 and arr[j] == 1:
            break

    even_idx = i

    assignment = [-1 for _ in range(k)]
    assignment[even_idx] = -2

    for i,x in enumerate(arr):
        if x == 1:
            assignment[i] = even_idx

    for i in iteration[even_idx+1:]:
        if assignment[i] != -1:
            continue
        if assignment[i] == -2:
            break
        assert assignment[i-1] == even_idx
        assignment[i-1] = i
        assignment[i] = even_idx

    assert -1 not in assignment
    assert assignment.count(-2) == 1

    res = []
    for i,x in enumerate(assignment):
        if x == -2:
            continue
        res.append((i,x))

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, k)  # include input here

    if res == []:
        print(no)
        continue

    print(yes)
    # print length if applicable
    # print(len(res))

    res = [(x+1, y+1) for x,y in res]

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
