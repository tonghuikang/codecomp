#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 998244353
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

def inversePermutation(arr):
    # https://www.geeksforgeeks.org/inverse-permutation/
    size = len(arr)
 
    # To store element to index mappings
    arr2 = [0] * (size)
     
    # Inserting position at their
    # respective element in second array
    for i in range(0, size) :
        arr2[arr[i]] = i
     
    return arr2


def solve_(n):
    dp = defaultdict(int)  # how many unswapped
    dp[0] = 1
    
    for i in range(n):
        new_dp = defaultdict(int)
        for k,v in dp.items():
            if k == 0:
                new_dp[k+1] += dp[k]
            else:
                new_dp[k+1] += dp[k]
                new_dp[k-1] += dp[k]*(k)
        dp = new_dp
        log(dp)
            
    return sum(dp.values())


def solve_(n):
    res = 0
    for comb in itertools.permutations(list(range(n))):
        inv = inversePermutation(comb)
        for a,b in zip(inv,comb):
            if abs(a-b) > 1:
                break
        else:
            log(inv, comb)
            res += 1
    return res


def solve_ref(n):
    # your solution here

    dp = [[0, 0], [0, 0]]   # (first_taken, second_taken)
    dp[1][1] = 1

    for i in range(n):
        new_dp = [[0, 0], [0, 0]] 

        # no add
        new_dp[0][0] += dp[0][0] + dp[1][0]
        new_dp[1][0] += dp[0][1] + dp[1][1]

        # right add
        new_dp[1][1] += dp[0][0] + dp[1][0]

        # middle add
        new_dp[0][1] += dp[0][0]
        new_dp[1][1] += dp[0][1]

        dp = [[x%m9 for x in row] for row in new_dp]
        log(dp)

    return sum(sum(x) for x in dp)%m9


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

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
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
