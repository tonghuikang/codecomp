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


SIZE_OF_PRIME_ARRAY = 10**5 + 10
largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY)   # take care that it begins with [1,1,2,...]
primes = [x for i,x in enumerate(largest_prime_factors[2:], start=2) if x == i]


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


def get_all_divisors_given_prime_factorization(factors):
    c = Counter(factors)

    divs = [1]
    for prime, count in c.most_common()[::-1]:
        l = len(divs)
        prime_pow = 1

        for _ in range(count):
            prime_pow *= prime
            for j in range(l):
                divs.append(divs[j]*prime_pow)

    # NOT IN SORTED ORDER
    return divs


def solve_(srr, n):
    # your solution here
    factors = get_prime_factors_with_precomp(n)
    # log(factors)

    for x in sorted(get_all_divisors_given_prime_factorization(factors)):
        ref = srr[:x]
        # log(ref)
        for left in range(0,n,x):
            right = left+x
            compare = srr[left:right]
            if ref != compare:
                break
        else:
            return ref

    return srr

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    srr = input().strip()

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

    res = solve(srr, n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
