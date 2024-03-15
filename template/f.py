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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------



LARGE = 2**20
p = 998244353  # CHANGE WHEN NEEDED

factorial_mod_p = [1]
for i in range(1, LARGE + 1):
    factorial_mod_p.append((factorial_mod_p[-1] * i) % p)

ifactorial_mod_p = [1] * (LARGE + 1)
ifactorial_mod_p[LARGE] = pow(factorial_mod_p[LARGE], p - 2, p)
for i in range(LARGE - 1, 1, -1):
    ifactorial_mod_p[i] = ifactorial_mod_p[i + 1] * (i + 1) % p


def ncr_mod_p(n, r, p=p):
    # https://codeforces.com/contest/1785/submission/192389526
    if r < 0 or n < r:
        return 0
    num = factorial_mod_p[n]
    dem = (ifactorial_mod_p[r] * ifactorial_mod_p[n - r]) % p
    return (num * dem) % p



def modinv_p(base, p=998244353):
    # modular inverse if the modulo is a prime
    return pow(base, -1, p)  # for Python 3.8+
    # return pow(base, p-2, p)  # if Python version is below 3.8



def prob(n,k):
    # P(X > k) where X ~ B(N, 1/2) 
    return ncr_mod_p(n, k)


def solve_(n, q, arr, brr, qrr):
    # your solution here

    psum_a = [0]
    psum_b = [0]

    for a,b in zip(arr, brr):
        psum_a.append(psum_a[-1] + a)
        psum_b.append(psum_b[-1] + b)

    n = psum_b[-1]  # total silver coins
    
    moddy = modinv_p(pow(2, n, p))

    p_x_equal_k = [(ncr_mod_p(n, k) * moddy) % m9 for k in range(n+1)]
    psum = [0]
    for x in p_x_equal_k:
        psum.append((psum[-1] + x) % m9)
    
    # log(psum)

    res = []

    for l,r in qrr:
        a = psum_a[r] - psum_a[l-1]
        b = psum_b[r] - psum_b[l-1]

        x = psum_a[-1] - a
        y = psum_b[-1] - b

        log(a,b,x,y)

        if b + y < x - a:
            res.append(0)
            continue

        if x - a < 0:
            res.append(1)
            continue

        # X   ~ a + B(b, 1/2)
        # Y   ~ x + B(y, 1/2)
        # X-Y ~ a - x + B(b+y, 1/2)
        # We want P(X-Y) > 0
        # a - x + B(b+y, 1/2) > 0
        # B(b+y, 1/2) > x - a

        res.append(psum[x-a])

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
    n,q = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    qrr = read_matrix(q)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, q, arr, brr, qrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
