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


LARGE = 110
p = 10**9 + 7
factorial_mod_p = [1 for _ in range(LARGE)]
for i in range(1,LARGE):
    factorial_mod_p[i] = (factorial_mod_p[i-1]*i)%p


def ncr_mod_p(n, r, p=p):
    if r < 0:
        return 0
    num = factorial_mod_p[n]
    dem = factorial_mod_p[r]*factorial_mod_p[n-r]
    return (num * pow(dem, p-2, p))%p



def solve_(n,i,j,x,y):
    # your solution here
    
    if x > y:
        x, y = y, x
        i,j = n-j-1, n-i-1
        assert i < j
        log(n,i,j,x,y)

    diff = abs(x-y) - 1
    peak_count = n - y - 1
    base_count = x

    # assume N is in the middle of i and j
    left_arm = j - i - 1 - peak_count
    right_arm = diff - left_arm
    # log("mid left_arm", left_arm)
    # log("mid right_arm", right_arm)

    res = 0
    if peak_count >= 1 and left_arm >= 0 and right_arm >= 0 and base_count >= i:
        peak_res = pow(2, peak_count-1, p)
        arm_res = ncr_mod_p(diff, left_arm)
        side_res = ncr_mod_p(base_count, i)
        val = peak_res * side_res * arm_res
        log(val)
        res += val

    # assume N is in the right of j
    new_res = 0
    left_arm = j - i - 1
    right_arm = diff - left_arm
    # log("side left_arm", left_arm)
    # log("side right_arm", right_arm)

    if peak_count >= 1 and left_arm >= 0 and right_arm >= 0 and base_count >= i:
        peak_res = pow(2, peak_count-1, p)
        arm_res = ncr_mod_p(diff, left_arm)
        side_res = ncr_mod_p(base_count, i)
        val = peak_res * side_res * arm_res
        log(val)
        res += val

    # Y is peak
    if y == n-1:
        left_arm = j - i - 1
        right_arm = diff - left_arm
        # log("peak left_arm", left_arm)
        # log("peak right_arm", right_arm)
        if left_arm >= 0 and right_arm >= 0 and base_count >= i:
            peak_res = 1
            arm_res = ncr_mod_p(diff, left_arm)
            side_res = ncr_mod_p(base_count, i)
            val = peak_res * side_res * arm_res
            log(val)
            res += val

    # log(res)

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,i,j,x,y = list(map(int,input().split()))
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,i,j,x,y)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
