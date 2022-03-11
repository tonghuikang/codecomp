#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
from collections import Counter
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
OFFLINE_TEST = getpass.getuser() == "htong"
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


largest_prime_factors = get_largest_prime_factors(int(10**5))   # take care that it begins with [1,1,2,...]
primes = [x for i,x in enumerate(largest_prime_factors[2:], start=2) if x == i][::-1]

log(primes[-10:])

def get_prime_factors_with_precomp_largest_factors(num, largest_prime_factors=largest_prime_factors):
    onum = num

    if num == 1:
        return [1]

    factors = []

    for p in primes:
        while num%p == 0:
            factors.append(p)
            num = num // p
    if num > 1:
        factors.append(num)

    log(onum, factors)
    return factors

    #     log(onum, factors)
    #     return factors
            
    # # factorise into prime factors given precomputed largest_prime_factors
    # lf = largest_prime_factors[num]
    # while lf != num:
    #     factors.append(lf)
    #     num //= lf
    #     lf = largest_prime_factors[num]
    # if num > 1:
    #     factors.append(num)
    # return sorted(factors)


def solve_(x,d):
    # your solution here

    factors_x = get_prime_factors_with_precomp_largest_factors(x)
    counter_x = Counter(factors_x)

    factors_d = get_prime_factors_with_precomp_largest_factors(d)
    d_is_prime = len(factors_d) == 1
    # c = Counter(factors)

    count_d = 0
    remainder = x
    while remainder%d == 0:
        remainder = remainder//d
        count_d += 1

    factors_r = get_prime_factors_with_precomp_largest_factors(remainder)
    r_is_prime = len(factors_r) == 1

    log(factors_x)
    log(factors_d)
    log(factors_r)

    if count_d == 1:
        # only one representation
        return no

    if r_is_prime and count_d == 2:
        # only one representation
        return no

    if r_is_prime and d_is_prime:
        return no

    if r_is_prime and remainder * remainder == d:  # [2,1] = [1,2]
        return no
    
    return yes


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    x,d = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(x,d)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
