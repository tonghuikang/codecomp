#!/usr/bin/env python3
import sys
input = sys.stdin.readline  # to read input quickly
import math

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


def solve_(n,arr,brr):
    # your solution here

    # crr = [abs(a-b) for a,b in zip(arr, brr)]
    # arr, brr = brr, crr

    # crr = [abs(a-b) for a,b in zip(arr, brr)]
    # arr, brr = brr, crr

    # log(arr)
    # log(brr)

    idxs = [0,0,0]

    for a,b in zip(arr, brr):
        if a == b == 0:
            continue
        if a == 0:
            idxs[0] += 1
            continue
        if b == 0:
            idxs[1] += 1
            continue
        
        a,b = a/math.gcd(a,b), b/math.gcd(a,b)
        if a%2 == 0:
            idxs[0] += 1
            continue
        if b%2 == 0:
            idxs[1] += 1
            continue
        idxs[2] += 1
            
    if (idxs[0] > 0) + (idxs[1] > 0) + (idxs[2] > 0) > 1:
        return no
    
    return yes
        
    #     q = math.gcd(a,b)

    # for _ in range(30):
    #     crr = [abs(a-b) for a,b in zip(arr, brr)]
    #     arr, brr = brr, crr
    #     log(arr)

    # if arr.count(0) == n:
    #     return yes
    # if brr.count(0) == n:
    #     return yes
    # if crr.count(0) == n:
    #     return yes

    return no


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
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,arr,brr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)