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


def solve_(arr,brr,crr):
    # your solution here

    # last painter color must be in the result
    if crr[-1] not in brr:
        log("last painter not in result")
        return []

    # must be able to paint all
    c_able = Counter(arr) + Counter(crr)
    c_required = Counter(brr)

    for color,required in c_required.items():
        if c_able[color] < required:
            log(color)
            log("not enough painters")
            return []

    # identify difference
    required = defaultdict(list)
    for i,(a,b) in enumerate(zip(arr,brr)):
        if a != b:
            required[b].append(i)
    
    # identify the last fence and stuff all in
    last_color = crr[-1]
    if required[last_color]:
        last_fence = required[last_color].pop()
    else:
        last_fence = brr.index(last_color)

    res = [last_fence]
    for c in crr[:-1][::-1]:
        if required[c]:
            res.append(required[c].pop())
        else:
            res.append(last_fence)

    res = res[::-1]

    for c,r in zip(crr, res):
        arr[r] = c
    assert arr == brr

    for v in required.values():
        assert not v

    return res


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
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    crr = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr,brr,crr)  # include input here
    res = [1+x for x in res]
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    if res:
        print("YES")
        print(*res)
    else:
        print("NO")
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)