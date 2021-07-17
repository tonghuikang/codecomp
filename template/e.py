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


def solve_(srr):
    # your solution here
    
    ctr = Counter(list(srr))
    dtr = sorted(ctr.items())

    # if all same, there is nothing to do
    if len(ctr) == 1:
        return srr
    
    # if there is a unique character, smallest unique then sort for score 0
    for k,v in dtr:
        if v == 1:
            res = k
            for k2,v2 in dtr:
                if k2 == k:
                    v2 -=1
                res += k2*v2 
            return res

    # otheriwse need to have score at least 1, should be able to force 1

    a, acnt = dtr[0]
    b, bcnt = dtr[1]
    remainder = []
    for k2,v2 in dtr[2:]:
        for _ in range(v2):
            remainder.append(k2)
    remainder = remainder[::-1]

    log(a,b,acnt,bcnt)
    log(remainder)

    # try force aab(no with no aa, does not work if there is too much a)

    res = a + a
    acnt -= 2
    while acnt or bcnt or remainder:
        if res[-1] != a and acnt:
            res += a
            acnt -= 1
            continue
        if bcnt:
            res += b
            bcnt -= 1
            continue
        if remainder:
            res += remainder.pop()        
            continue
        break

    if len(res) == len(srr):
        return res

    a, acnt = dtr[0]
    b, bcnt = dtr[1]
    remainder = ""
    for k2,v2 in dtr[2:]:
        for _ in range(v2):
            remainder += k2
    # remainder = remainder[::-1]

    # then ab(no consecutive ab)
        # if there is no c
        # a(all the b)(all the remainding a)
        # otherwise you cannot avoid ab

    if len(dtr) == 2:  # only ab
        return a + b*bcnt + a*(acnt-1)

        # if there is a c
        # ab(all the remaining a)(smallest c)(all the remaining b)(remainders)

    return a + b + a*(acnt-1) + remainder[0] + b*(bcnt-1) + remainder[1:]


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)