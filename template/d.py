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


def solve_(lst):
    prev = 0
    keep = []
    dump = []
    
    for x in lst:
        if x == prev:
            dump.append(x)
            keep.append(0)
        else:
            keep.append(x)
            dump.append(0)
        prev = x

    # log(dump)
    # log(keep)

    # between adjacent same elements in dump, if there are more than one unique element in keep at the same range, migrate
    locations = [(i,x) for i,x in enumerate(dump) if x]
    # log(locations)        

    for (i1,x1),(i2,x2) in zip(locations,locations[1:]):
        if x1 == x2:
            count = set()
            for i in range(i1+1,i2):
                if keep[i]:
                    count.add(keep[i])
            # log(i1,x1,i2,x2,count)
            if len(count) > 1:
                # log("migrate")
                idx = i1+1
                keep[idx],dump[idx] = 0,keep[idx]

    log(dump)
    log(keep)


    res = sum(bool(x) for x in keep)
    prev = -1
    for x in dump:
        if x == 0:
            continue
        if prev != x:
            res += 1
        prev = x

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
    lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(lst)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)