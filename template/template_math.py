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


# FFT convolution
# https://atcoder.jp/contests/abc196/submissions/21089133
ROOT = 3
MOD = 998244353
roots  = [pow(ROOT,(MOD-1)>>i,MOD) for i in range(24)] # 1 の 2^i 乗根
iroots = [pow(x,MOD-2,MOD) for x in roots] # 1 の 2^i 乗根の逆元

def untt(a,n):
    for i in range(n):
        m = 1<<(n-i-1)
        for s in range(1<<i):
            w_N = 1
            s *= m*2
            for p in range(m):
                a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m])%MOD, (a[s+p]-a[s+p+m])*w_N%MOD
                w_N = w_N*roots[n-i]%MOD
 
def iuntt(a,n):
    for i in range(n):
        m = 1<<i
        for s in range(1<<(n-i-1)):
            w_N = 1
            s *= m*2
            for p in range(m):
                a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m]*w_N)%MOD, (a[s+p]-a[s+p+m]*w_N)%MOD
                w_N = w_N*iroots[i+1]%MOD
            
    inv = pow((MOD+1)//2,n,MOD)
    for i in range(1<<n):
        a[i] = a[i]*inv%MOD
 
def convolution(a,b):
    la = len(a)
    lb = len(b)
    if min(la, lb) <= 50:
        if la < lb:
            la,lb = lb,la
            a,b = b,a
        res = [0]*(la+lb-1)
        for i in range(la):
            for j in range(lb):
                res[i+j] += a[i]*b[j]
                res[i+j] %= MOD
        return res
 
    deg = la+lb-2
    n = deg.bit_length()
    N = 1<<n
    a += [0]*(N-len(a))
    b += [0]*(N-len(b))
    untt(a,n)
    untt(b,n)
    for i in range(N):
      a[i] = a[i]*b[i]%MOD
    iuntt(a,n)
    return a[:deg+1]


# get all combination of factors of an integer
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# https://www.geeksforgeeks.org/print-combinations-factors-ways-factorize/


# n factorial modulo p
# # https://www.geeksforgeeks.org/compute-n-under-modulo-p/
