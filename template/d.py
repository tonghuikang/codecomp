#!/usr/bin/env python3
import sys
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
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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


def count_sum(x):
    return x * (x+1) // 2


def count_interval_inclusive(a,b):
    return count_sum(b) - count_sum(a-1)


def solve_(n):
    # your solution here

    if n > 10:
        return

    if n == 2:
        return [3,1]


    res = list(range(3*n,3*n-(n-2),-1))

    for diff in range(10**6):
        if count_interval_inclusive(diff,diff+n) > (n-1)**2:
            break

    # LARGE = n//2
    # if n == 5:
    #     return [20, 29, 18, 26, 28]
    # if n == 4:
    #     return [25, 21, 23, 31]

    LARGE = 10**9
    for left in range(1,n-1):
        right = n-left
        allsum = count_interval_inclusive(1,left) + count_interval_inclusive(LARGE-right+1, LARGE)
        # log(allsum)
        # log(n**2)
        if allsum > (LARGE-1)**2:
            break

    res = list(range(1,left+1)) + list(range(LARGE-right+1,LARGE+1))
    log(res)
    log(left, right)
    log(allsum - n**2)
    log((LARGE-1)**2)



    
    # res = list(range(diff+1,diff+n+2))

    # maxres = max(res)
    # minres = min(res)
    # sumres = sum(res)

    # log("max", maxres)
    # log("min", minres)
    # log("mm2", (maxres - minres)**2)
    # log("sum", sumres)
    # log("sum2", sumres**0.5)

    # for i in range(1,2*n):
    #     if (maxres-i)**2 < sumres:
    #         break
    # # i -= 1
    
    # res.append(i-1)

    # maxres = max(res)
    # minres = min(res)
    # sumres = sum(res)

    # log(len(res))
    # log("max", maxres)
    # log("min", minres)
    # log("mm2", (maxres - minres)**2)
    # log("sum", sumres)
    # log("sum2", sumres**0.5)

    # log()

    # res.append((maxres-minres)**2 - sumres)
    # log(res[-1])

    # maxres = max(res)
    # minres = min(res)
    # sumres = sum(res)

    # log(len(res))
    # log(maxres)
    # log(minres)
    # log(sumres**0.5)
    # log(sumres)
    # log((maxres - minres)**2)

    # assert maxres - minres == sumres**0.5
    # assert len(res) == n

    return ""


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

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

    res = solve(n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
