#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
# import math, random
# import functools, itertools, collections, heapq, bisect
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



# https://binarysearch.com/problems/K-Largest-Pairs/solutions/5990638

def solve_(arr, mrr):
    # your solution here

    banned_pair = set((a,b) for a,b in mrr) | set((b,a) for a,b in mrr)
    banned_pair |= set((a,a) for a in arr) 

    c = Counter(arr)

    cntrs = sorted(c.items(), key=lambda x:x[1])[::-1]

    populate = defaultdict(list)
    for a,b in cntrs:
        populate[b].append(a)

    for b in populate:
        populate[b].sort()
        populate[b].reverse()

    # log(populate)
    # log(banned_pair)

    def get_biggest_pair_not_banned(arr, brr):
        # log(arr, brr)
        maxres = 0
        for a in arr:
            for b in brr:
                if (a,b) not in banned_pair:
                    maxres = max(maxres, a+b)
                    break

        return maxres


    maxres = 0
    b_vals = list(populate.keys())
    for i,b1 in enumerate(b_vals):
        for b2 in b_vals[i:]:
            maxpairsum = get_biggest_pair_not_banned(populate[b1], populate[b2])
            res = (b1+b2) * maxpairsum
            maxres = max(maxres, res)
                    
    return maxres



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    _,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
