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

all_roaring_years = set()
LIMIT_REF = 10**7

for i in range(1,1000):
    for cnt in range(2,8):
        val = int("".join(str(i+x) for x in range(cnt)))
        if val <= LIMIT_REF:
            all_roaring_years.add(val)
    
all_roaring_years = sorted(all_roaring_years)
all_roaring_years.append(10**19)
log(all_roaring_years[:10])

def solve_ref(k):
    # your solution here
    idx = bisect.bisect_right(all_roaring_years, k)

    return all_roaring_years[idx]


all_roaring_years_copy = [x for x in all_roaring_years[:10]]
all_roaring_years_copy.append(10**19)

LIMIT = 10**19

def solve_(k):
    # your solution here

    minres = all_roaring_years[bisect.bisect_right(all_roaring_years_copy, k)]
    # log(minres)

    for start_length in range(1,min(len(str(k)), 10)):
        start_num = int(str(k)[:start_length])
        for cnt in range(2,19):
            val = int("".join(str(start_num+x) for x in range(cnt)))
            if val >= LIMIT:
                break
            if val > k:
                minres = min(minres, val)
        
        start_num += 1
        for cnt in range(2,19):
            val = int("".join(str(start_num+x) for x in range(cnt)))
            if val >= LIMIT:
                break
            if val > k:
                minres = min(minres, val)   

    return minres


if OFFLINE_TEST:
    i = 0
    while True:
        i += 1
        r1 = solve_ref(i)
        r2 = solve_(i)
        if r1 != r2:
            print(i, r1, r2)
            assert False

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
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(k)  # include input here
    
    # print result
    # Google and Facebook - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)