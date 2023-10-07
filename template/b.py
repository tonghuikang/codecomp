#!/usr/bin/env python3
import sys
import math, random
from functools import cache
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


SIZE_OF_PRIME_ARRAY = 10**6 + 10
largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY)  # take care that it begins with [1,1,2,...]
primes = [x for i, x in enumerate(largest_prime_factors[2:], start=2) if x == i]


def get_prime_factors_with_precomp(num):
    # requires precomputed `largest_prime_factors``
    # for numbers below SIZE_OF_PRIME_ARRAY
    # O(log n)
    factors = []
    lf = largest_prime_factors[num]
    while lf != num:
        factors.append(lf)
        num //= lf
        lf = largest_prime_factors[num]
    if num > 1:
        factors.append(num)
    return factors


def get_prime_factors_with_precomp_sqrt(num):
    limit = int(num**0.5) + 2
    # requires precomputed `primes``
    # for numbers below SIZE_OF_PRIME_ARRAY**2
    # O(sqrt(n) / log(n))

    if num == 1:
        # may need to edit depending on use case
        return []

    factors = []
    for p in primes:
        while num % p == 0:
            factors.append(p)
            num = num // p
        # if num < p:  # remaining factor is a prime?
        #     break
        if p > limit:
            break
    if num > 1:
        # remaining number is a prime
        factors.append(num)

    return factors


# for each multiset of prime factors
# applicable sumval and its corresponding minimum length and array

@cache
def dp(factors):
    # return minimum length array that has product factors and sums to sumval
    log(factors)

    if len(factors) == 1 and factors[0] <= 41:
        return {factors[0]: [factors[0]]}

    res = {}

    for x in factors:
        f2 = list(factors)
        f2.remove(x)
        f2 = tuple(f2)

        r2 = dp(f2)

        for s2, a2 in r2.items():
            # append
            ss = s2 + x
            if ss not in res or len(res[ss]) > len(a2) + 1:
                if ss <= 41:
                    res[ss] = [x for x in a2] + [x]
            
            for i in range(len(a2)):
                s2 -= a2[i]
                a2[i] = a2[i] * x
                s2 += a2[i]

                if s2 not in res or len(res[s2]) > len(a2):
                    if s2 <= 41:
                        res[s2] = [x for x in a2]

                s2 -= a2[i]
                a2[i] = a2[i] // x
                s2 += a2[i]

    log(factors, res)
    return res


# log(dp((2,2,2)))

def solve_(n):
    # your solution here

    factors = get_prime_factors_with_precomp_sqrt(n)

    log(factors)

    if sum(factors) > 41:
        return [-1]
    
    minval = factors + [1] * (41 - sum(factors))
    
    dp_res = dp(tuple(factors))

    log(dp_res)

    for k,val in dp_res.items():
        val = val + [1] * (41 - sum(val))
        if len(val) < len(minval):
            minval = val

    assert sum(minval) == 41
    val = 1
    for x in minval:
        val = val * x
    assert val == n

    return minval


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

    if res != [-1]:
        res = [len(res)] + res

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
