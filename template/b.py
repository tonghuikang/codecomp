#!/usr/bin/env python3
import sys
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

LARGE = 10**19

def solve_(arr,brr,n,m,k):
    # your solution here

    asum = [0]
    for x in arr:
        asum.append(asum[-1] + x)

    bsum = [0]
    for x in brr:
        bsum.append(bsum[-1] + x)

    amin = [LARGE for _ in range(n+1)]
    bmin = [LARGE for _ in range(m+1)]
    amin[0] = 0
    bmin[0] = 0

    for i,x in enumerate(asum):
        for j,y in enumerate(asum[i+1:], start=i+1):
            dist = j-i
            val = y-x
            amin[dist] = min(amin[dist], val)

    for i,x in enumerate(bsum):
        for j,y in enumerate(bsum[i+1:], start=i+1):
            dist = j-i
            val = y-x
            bmin[dist] = min(bmin[dist], val)

    # log(amin)
    # log(bmin)

    minres = 10**18
    for i in range(n+1):
        j = n+m-k-i
        if j > m or j < 0:
            continue
        res = amin[i] + bmin[j]
        # log(i,j,res)
        minres = min(minres, res)

    return sum(arr) + sum(brr) - minres


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
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)
    m = int(input())
    brr = list(map(int,input().split()))
    k = int(input())

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr,brr,n,m,k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
