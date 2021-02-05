#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------


def solve_(arr, m):
    # your solution here

    if m%2 == 1:
        return [0,1]*((m+1)//2)

    for i,row in enumerate(arr):
        for j,cell in enumerate(row[:i]):
            if cell == arr[j][i]:
                return [i,j]*(m//2) + [i]
    
    x,y,z = -1,-1,-1
    for i,row in enumerate(arr):
        c = Counter(row)
        if c["a"] and c["b"]:
            x = row.index("a")
            y = row.index("b")
            z = i
            break
    else:
        if len(arr) > 2:
            log("error")
        return []
    
    log(x,y,z)
    if m%4 == 0:
        return [z,x,z,y]*(m//4) + [z]
    
    if m%4 == 2:
        return [y,z]*(m//4) + [x,z,y] + [z,x]*(m//4)

    return []


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    arr = read_strings(n)  # and return as a list of str

    res = solve(arr, m)  # include input here
    res = [1+x for x in res]
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))


    if res:
        assert len(res) == m+1
        print("YES")
        print(*res)
    else:
        print("NO")

