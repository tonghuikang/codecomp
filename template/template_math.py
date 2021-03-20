#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------

def lcm(a,b): 
    return a*b//math.gcd(a,b)


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


LARGE = int(2*10**7)
count_factors = [0] * LARGE
largest_factor = [1] * LARGE
for i in range(2, LARGE):
    if count_factors[i]:
        continue
    for j in range(i, LARGE, i):
        count_factors[j] += 1
        largest_factor[j] = i


def prime_factors_precomp(num):
    factors = []
    lf = largest_factor[num]
    while lf != num:
        factors.append(lf)
        num //= lf
        lf = largest_factor[num]
    if num > 1:
        factors.append(num)
    return factors


@functools.lru_cache(maxsize=10000)
def all_divisors_precomp(num):
    factors = prime_factors_precomp(num)
    c = Counter(factors)

    divs = [1]
    for prime, count in c.most_common()[::-1]:
        l = len(divs)
        prime_pow = 1
 
        for _ in range(count):
            prime_pow *= prime
            for j in range(l):
                divs.append(divs[j]*prime_pow)

    return divs


modinv = lambda A,n,s=1,t=0,N=0: (n < 2 and t%N or modinv(n, A%n, t, s-A//n*t, N or n),-1)[n<1]


def isprime(n):
    # https://github.com/not522/ac-library-python/blob/master/atcoder/_math.py
    # http://ceur-ws.org/Vol-1326/020-Forisek.pdf
    # untested
    if n <= 1:
        return False
    if n > 2**32:
        primitives = set([2, 325, 9375, 28178, 450775, 9780504, 1795265022])
        if n == 2:
            return True
    else:
        primitives = set([2, 7, 61])
        if n in primitives:
            return True
    
    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in primitives:
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t <<= 1
        if y != n - 1 and t % 2 == 0:
            return False
    return True


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


def butterfly(arr):
    MOD = 998244353
    sum_e = (911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 
             603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 
             510815449, 503497456, 743006876, 741047443, 56250497, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p] * now
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (l - r) % MOD
            now *= sum_e[(~s & -~s).bit_length() - 1]
            now %= MOD

def butterfly_inv(arr):
    MOD = 998244353
    sum_ie = (86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 
            90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 
            121186627, 608385704, 438932459, 359477183, 824071951, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1)[::-1]:
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p]
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (MOD + l - r) * inow % MOD
            inow *= sum_ie[(~s & -~s).bit_length() - 1]
            inow %= MOD

def convolution(a, b):
    # arrays might be in the wrong direction
    # https://www.hackerrank.com/contests/spring-2021-indeed-programming-challenge/challenges/power-connectors
    MOD = 998244353
    n = len(a)
    m = len(b)
    if not n or not m: return []
    if min(n, m) <= 50:
        if n < m:
            n, m = m, n
            a, b = b, a
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i + j] += a[i] * b[j]
                res[i + j] %= MOD
        return res
    z = 1 << (n + m - 2).bit_length()
    a += [0] * (z - n)
    b += [0] * (z - m)
    butterfly(a)
    butterfly(b)
    for i in range(z):
        a[i] *= b[i]
        a[i] %= MOD
    butterfly_inv(a)
    a = a[:n + m - 1]
    iz = pow(z, MOD - 2, MOD)
    for i in range(n + m - 1):
        a[i] *= iz
        a[i] %= MOD
    return a


# get all combination of factors of an integer
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# https://www.geeksforgeeks.org/print-combinations-factors-ways-factorize/


# n factorial modulo p
# # https://www.geeksforgeeks.org/compute-n-under-modulo-p/
