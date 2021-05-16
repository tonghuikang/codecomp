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


def solve_(lst, dir, n, m):
    # your solution here
    zrr = [(pos, d, i) for i, (pos, d) in enumerate(zip(lst, dir))]
    del lst
    del dir

    zrr.sort()
    res = [-1]*len(zrr)

    def proc(val):

        stack2 = deque([])
        for p, d, i in zrr:
            if p&1 == val:
                continue
            if d == -1 and stack2 and stack2[-1][1] == 1:  # forward
                p2, d2, i2 = stack2.pop()
                t = abs(p2-p) >> 1
                res[i] = t
                res[i2] = t
            else:
                stack2.append((p,d,i))

        while len(stack2) >= 2:
            p, d, i = stack2.popleft()
            p2, d2, i2 = stack2.popleft()
            if not (d == d2 == -1):
                stack2.appendleft((p2, d2, i2))
                stack2.appendleft((p, d, i))
                break
            t = (p2+p) >> 1
            res[i] = t
            res[i2] = t
        
        while len(stack2) >= 2:
            p, d, i = stack2.pop()
            p2, d2, i2 = stack2.pop()
            if not (d == d2 == 1):
                stack2.append((p2, d2, i2))
                stack2.append((p, d, i))
                break
            t = (m-p2+m-p) >> 1
            res[i] = t
            res[i2] = t
        
        assert len(stack2) <= 2
        if len(stack2) == 2:
            assert stack2[0][1] == -1 and stack2[1][1] == 1
            p, d, i = stack2.popleft()
            p2, d2, i2 = stack2.pop()
            t = (m + (m-p2) + p) >> 1
            res[i] = t
            res[i2] = t
                

    proc(1)
    proc(0)

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    
    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    lst = list(map(int,input().split()))
    dir = input().split()
    # lst = minus_one(lst)
    dir = [1 if val == "R" else -1 for val in dir]

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(lst, dir, n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)