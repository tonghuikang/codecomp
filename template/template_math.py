#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------


def all_divisors(n):
    return set(functools.reduce(list.__add__, 
    ([i, n//i] for i in 
    range(1, int(n**0.5) + 1) if n % i == 0)))


def prime_factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if i > math.sqrt(nr):
            i = nr
        if (nr % i) == 0:
            factors.append(int(i))
            nr = nr / i
        elif i == 2:
            i = 3
        else:
            i = i + 2
    return factors


modinv = lambda A,n,s=1,t=0,N=0: (n < 2 and t%N or modinv(n, A%n, t, s-A//n*t, N or n),-1)[n<1]


def is_prime(x):
    # primarity test
    raise NotImplementedError


def modinvp(base, p):
    return pow(base, p-2, p)


def ceiling_division(numer, denom):
    return -((-numer)//denom)


def chinese_remainder_theorem(divisors, remainders):
    sum = 0
    prod = functools.reduce(lambda a, b: a*b, divisors)
    for n_i, a_i in zip(divisors, remainders):
        p = prod // n_i
        sum += a_i * modinv(p, n_i) * p
    return sum % prod


def ncr(n, r):
    # if python version == 3.8+, use comb()
    if r == 0:
        return 1
    return n * ncr(n-1, r-1) // r


@functools.lru_cache(maxsize=None)
def choose(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def sieve_of_eratosthenes(n):
    # primarity test and prime factor listing for all numbers less than n
    prime = [True for _ in range(n)] 
    prime[0], prime[1] = False, False
    factors = [[] for _ in range(n)]

    for i in range(2,n):
        factors[i].append(i)
        for j in range(i*2, n, i):
            prime[j] = False
            factors[j].append(i)
    return prime, factors


def floor_sum_over_divisor(n,k,j):
    # https://math.stackexchange.com/questions/384520/efficient-computation-of-sum-k-1n-lfloor-fracnk-rfloor
    # https://mathoverflow.net/questions/48357/summation-of-a-series-of-floor-functions       
    def floor_sum_over_divisor_(n,k,j):
        return sum(n//d for d in range(j+1, k+1))
    return floor_sum_over_divisor_(n, n//j, n//k) + k*(n//k) - j*(n//j)


def floor_sum_over_numerator(n: int, m: int, a: int, b: int) -> int:
    # https://atcoder.jp/contests/practice2/tasks/practice2_c
    # https://atcoder.github.io/ac-library/master/document_en/math.html
    # https://github.com/not522/ac-library-python/blob/master/atcoder/math.py

    assert 1 <= n
    assert 1 <= m

    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum_over_numerator(y_max, a, m, (a - x_max % a) % a)

    return ans


# get all combination of factors of an integer
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# https://www.geeksforgeeks.org/print-combinations-factors-ways-factorize/


# n factorial modulo p
# # https://www.geeksforgeeks.org/compute-n-under-modulo-p/
