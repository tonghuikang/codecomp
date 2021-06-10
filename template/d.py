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

def get_largest_prime_factors(num):
    # get largest prime factor for each number
    # you can use this to obtain primes
    largest_prime_factors = [1] * num
    for i in range(2, num):
        if largest_prime_factors[i] > 1:  # not prime
            continue
        for j in range(i, num, i):
            largest_prime_factors[j] = i
    return largest_prime_factors

LARGE = int(10**5)

largest_prime_factors = get_largest_prime_factors(int(10**5))
primes = [x for i,x in enumerate(largest_prime_factors[2:], start=2) if x == i]


# def is_prime(n):
#     # primality test (not tested)
#     # https://github.com/not522/ac-library-python/blob/master/atcoder/_math.py
#     # http://ceur-ws.org/Vol-1326/020-Forisek.pdf
#     # untested
#     if n <= 1:
#         return False
#     if n > 2**32:
#         primitives = set([2, 325, 9375, 28178, 450775, 9780504, 1795265022])
#         if n == 2:
#             return True
#     else:
#         primitives = set([2, 7, 61])
#         if n in primitives:
#             return True
    
#     if n % 2 == 0:
#         return False

#     d = n - 1
#     while d % 2 == 0:
#         d //= 2

#     for a in primitives:
#         t = d
#         y = pow(a, t, n)
#         while t != n - 1 and y != 1 and y != n - 1:
#             y = y * y % n
#             t <<= 1
#         if y != n - 1 and t % 2 == 0:
#             return False
#     return True
# log(primes[:10])

def get_prime_factors_with_precomp_largest_factors(num):
    if num == 1:
        return []
    factors = []

    # if num >= int(10**4.6):
    #     if is_prime(num):
    #         return [num]
    #     # brute force first 1000
    for p in primes:
        while num%p == 0:
            factors.append(p)
            num = num//p
            # print(num, p)
    if num > 1:
        return factors + [num]
    return factors

    # # factorise into prime factors given precomputed largest_prime_factors
    # lf = largest_prime_factors[num]
    # while lf != num:
    #     factors.append(lf)
    #     num //= lf
    #     lf = largest_prime_factors[num]
    # if num > 1:
    #     factors.append(num)
    # return factors

# log("check")
# log(primes[-19:])

# for i in range(1,100):
#     log(get_prime_factors_with_precomp_largest_factors(i))

# for i in range(10**9-100,10**9):
#     log(get_prime_factors_with_precomp_largest_factors(i))

def solve_(a,b,k):
    a,b = sorted([a,b])
    
    if a == b == 1:
        return no

    if a == 1:
        f = len(get_prime_factors_with_precomp_largest_factors(b))
        if 1 <= k <= f:
            return yes
        return no

    if a == b:
        f = len(get_prime_factors_with_precomp_largest_factors(b))
        if 2 <= k <= 2*f:
            return yes
        return no
        
    gcd = math.gcd(a,b)    
    p = a//gcd
    q = b//gcd

    x = len(get_prime_factors_with_precomp_largest_factors(gcd))
    y = len(get_prime_factors_with_precomp_largest_factors(p))
    z = len(get_prime_factors_with_precomp_largest_factors(q))

    # log(get_prime_factors_with_precomp_largest_factors(gcd))
    # log(x,y,z,p,q)

    if k == 1:
        if p != 1:
            return no
    # if k == 2:
    #     if p == 1:
    #         if z == 1:
    #             return no

    if 1 <= k <= 2*x + y + z:
        return yes
    return no


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
    a,b,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(a,b,k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)