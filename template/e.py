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


def solve_(mrr):
    # your solution here

    curptr = -2
    ptr_to_val = {}
    val_to_ptr = {}
    arr = []

    for i,*q in mrr:
        curptr -= 1

        # log(arr)
        # log(ptr_to_val)
        # log(val_to_ptr)
        # log([ptr_to_val[ptr] for ptr in arr])
        # log()
        # assert len(ptr_to_val) == len(val_to_ptr)

        if i == 1:
            x = q[0]

            if x in val_to_ptr:
                ptr = val_to_ptr[x]
                arr.append(ptr)
            else:
                ptr_to_val[curptr] = x
                val_to_ptr[x] = curptr
                arr.append(curptr)

        elif i == 2:
            x,y = q[0],q[1]

            if x == y:
                continue

            if x not in val_to_ptr:
                # nothing to replace
                continue

            if y not in val_to_ptr:
                # relink
                ptr = val_to_ptr[x]
                ptr_to_val[ptr] = y
                val_to_ptr[y] = ptr
                del val_to_ptr[x]

            elif y in val_to_ptr:
                # point to another pointer
                xptr = val_to_ptr[x]
                yptr = val_to_ptr[y]
                ptr_to_val[xptr] = yptr
                del val_to_ptr[x]

        else:
            assert False

    # log(arr)
    # log(ptr_to_val)
    # log(val_to_ptr)
    # log([ptr_to_val[ptr] for ptr in arr])
    # log()

    res = []
    for ptr in arr:
        val = ptr_to_val[ptr]
        while val < 0:
            val = ptr_to_val[val]
        ptr_to_val[ptr] = val
        res.append(val)

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
