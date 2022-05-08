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

def minus_one(xrr):
    return [x-1 for x in xrr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(arr, brr, n):
    # your solution here

    seen = set()

    g = defaultdict(list)

    val_to_arr = {x:i for i,x in enumerate(arr)}
    val_to_brr = {x:i for i,x in enumerate(brr)}

    # log(val_to_brr)

    for i,x in enumerate(arr):
        x = val_to_brr[x]
        g[2,x].append((1,i))
        g[1,i].append((2,x))

    for i,x in enumerate(brr):
        x = val_to_arr[x]
        g[1,x].append((2,i))
        g[2,i].append((1,x))

    for i in range(n):
        g[1,i].append((2,i))
        g[2,i].append((1,i))


    # log(g)

    visited = set()
    res = 0
    for x in range(n):
        cur = (1,x)
        if cur in visited:
            continue
        # log()
        
        size = 1
        stack = [cur]
        visited.add(cur)
        while stack:
            cur = stack.pop()
            # log(cur)
            for nex in g[cur]:
                if nex in visited:
                    continue
                size += 1
                stack.append(nex)
                visited.add(nex)

        # log(x, size)
        res += size // 4

    # log("--")
    # log(res)

    ret = 0
    val = n-1
    for i in range(res):
        ret += val*2
        # log(val)
        val -= 2

    return ret


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    arr = minus_one(arr)
    brr = minus_one(brr)

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, brr, n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
