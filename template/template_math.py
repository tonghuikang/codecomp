#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------

def ceiling_division(numer, denom):
    return -((-numer)//denom)


def lcm(a,b):
    # lowest common multiple
    return a*b//math.gcd(a,b)


# ------------------------ single prime factorisation ------------------------


def is_prime(n):
    # primality test (not tested)
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


def get_prime_factors(nr):
    # factorise a single number into primes in O(sqrt(n))
    i = 2
    factors = []
    while i <= nr:
        if i > math.sqrt(nr):
            i = nr
        if (nr % i) == 0:
            factors.append(i)
            nr = nr // i
        elif i == 2:
            i = 3
        else:
            i = i + 2
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

    return divs


# ---------------------- multiple prime factorisation ----------------------


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


largest_prime_factors = get_largest_prime_factors(10**6)


def get_prime_factors_with_precomp_largest_factors(num, largest_prime_factors=largest_prime_factors):
    # factorise into prime factors given precomputed largest_prime_factors
    factors = []
    lf = largest_prime_factors[num]
    while lf != num:
        factors.append(lf)
        num //= lf
        lf = largest_prime_factors[num]
    if num > 1:
        factors.append(num)
    return factors


def get_prime_factor_count(num):
    # count how many prime factor
    prime_factor_count = [0] * num
    for i in range(2, num):
        if prime_factor_count[i]:  # not prime
            continue
        for j in range(i, num, i):
            prime_factor_count[j] += 1
    return prime_factor_count


# ----------------------------- modular inverse -----------------------------


# modular inverse
# https://stackoverflow.com/a/29762148/5894029
modinv = lambda A,n,s=1,t=0,N=0: (n < 2 and t%N or modinv(n, A%n, t, s-A//n*t, N or n),-1)[n<1]


def modinv_p(base, p):
    # modular if the modulo is a prime
    return pow(base, p-2, p)


def chinese_remainder_theorem(divisors, remainders):
    sum = 0
    prod = functools.reduce(lambda a, b: a*b, divisors)
    for n_i, a_i in zip(divisors, remainders):
        p = prod // n_i
        sum += a_i * modinv(p, n_i) * p
    return sum % prod


# ----------------------------- combinatorics  -----------------------------


def ncr(n, r):
    # if python version == 3.8+, use comb()
    if r == 0:
        return 1
    return n * ncr(n-1, r-1) // r


def factorial_mod_p(n, p):
    val = 1
    for i in range(1,n+1):
        val = (val*i)%p
    return val


def ncr_mod_p(n, r, p):
    num = factorial_mod_p(n)
    dem = factorial_mod_p(r)*factorial_mod_p(n-r)
    return (num * pow(dem, p-2, p))%p


# ----------------------------- floor sums  -----------------------------


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


# ------------------------- FFT convolution -------------------------


def convolution(a,b):
    # https://atcoder.jp/contests/abc196/submissions/21089133

    ROOT = 3
    MOD = 998244353
    roots  = [pow(ROOT,(MOD-1)>>i,MOD) for i in range(24)] # 1 の 2^i 乗根
    iroots = [pow(x,MOD-2,MOD) for x in roots] # 1 の 2^i 乗根の逆元

    def untt(a,n):
        # inplace modification
        for i in range(n):
            m = 1<<(n-i-1)
            for s in range(1<<i):
                w_N = 1
                s *= m*2
                for p in range(m):
                    a[s+p], a[s+p+m] = (a[s+p]+a[s+p+m])%MOD, (a[s+p]-a[s+p+m])*w_N%MOD
                    w_N = w_N*roots[n-i]%MOD

    def iuntt(a,n):
        # inplace modification
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


def walsh_hadamard(my_freqs):
    # https://en.wikipedia.org/wiki/Fast_Walsh%E2%80%93Hadamard_transform
    # https://leetcode.com/problems/count-pairs-with-xor-in-a-range/discuss/1119975/Python-O(N-log-N)-using-math-(Fourier-transform)
    my_max = len(my_freqs)

    # If our array's length is not a power of 2, 
    # increase its length by padding zeros to the right
    if my_max & (my_max - 1):
        my_max = 2 ** (my_max.bit_length())

    if my_max > len(my_freqs):
        my_freqs.extend([0] * (my_max - len(my_freqs)))

    h = 2
    while h <= my_max:
        hf = h // 2
        for i in range(0, my_max, h):
            for j in range(hf):
                u, v = my_freqs[i + j], my_freqs[i + j + hf]
                my_freqs[i + j], my_freqs[i + j + hf] = u + v, u - v
        h *= 2
    return my_freqs


# ------------------------- other methods -------------------------


# get all combination of factors of an integer
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# https://www.geeksforgeeks.org/print-combinations-factors-ways-factorize/


