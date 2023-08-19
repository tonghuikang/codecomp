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
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
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


def extended_gcd(a, b):
    # Extended Euclidean Algorithm
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def solve_diophantine(a, b, n):
    # Make sure that a and b are not both zero
    assert not (a == 0 and b == 0), "Both a and b cannot be zero"

    gcd, x, y = extended_gcd(a, b)

    # The equation has a solution only if n is a multiple of the gcd of a and b
    if n % gcd != 0:
        return None

    # Scale x and y by n/gcd
    x *= n // gcd
    y *= n // gcd

    # Check if the solution is correct
    assert a * x + b * y == n

    x2 = b // math.gcd(a,b)
    y2 = a // math.gcd(a,b)

    assert a * (x + x2) + b * (y - y2) == n

    return x, y


def ceiling_division(numer, denom):
    return -((-numer)//denom)


def solve_(n,a,b,c,x):
    # your solution here

    res = 0

    for k in range(1, n+1):
        m = x - c*k

        if a + b > m:
            continue

        # count number of solutions
        # b*j + c*k == m

        ret = solve_diophantine(a,b,m)
        if ret is None:
            continue

        i,j = ret

        assert a*i + b*j == m

        i2 = b // math.gcd(a,b)
        j2 = a // math.gcd(a,b)

        assert a*(i + i2) + b*(j - j2) == m

        small_i = max((m - b*n) // a, i % i2)
        small_i = ((small_i // i2) * i2) + i%i2
        big_i = min(n, (m - b) // a)
        big_i = ((big_i // i2) * i2) + i%i2

        if small_i > big_i:
            continue

        vals = (big_i - small_i) // i2 + 1

        if small_i <= (m - b*n) / a:
            vals -= 1
        if a*big_i == m:
            vals -= 1

        res += vals

        # log(a,b,m)
        # log(small_i,big_i,i2)
        # log(vals)
        # log()

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,a,b,c,x = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,a,b,c,x)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
