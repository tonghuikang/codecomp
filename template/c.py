#!/usr/bin/env python3
import sys
import math
from collections import Counter

input = sys.stdin.readline  # to read input quickly

# ---------------------------- template ends here ----------------------------



def get_all_divisors_given_prime_factorization(factors):
    c = Counter(factors)

    divs = [1]
    for prime, count in c.most_common()[::-1]:
        l = len(divs)
        prime_pow = 1

        for _ in range(count):
            prime_pow *= prime
            for j in range(l):
                divs.append(divs[j] * prime_pow)

    # NOT IN SORTED ORDER
    return divs



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



def solve_(n, arr):
    # your solution here

    factors = get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(n))

    res = 0

    for factor in factors:
        flag = True
        diffs = []
        for i in range(n // factor - 1):
            a,b,c = i*factor, (i+1)*factor, (i+2)*factor
            # log(arr[a:b], arr[b:c])
            for x,y in zip(arr[a:b], arr[b:c]):
                if x != y:
                    diffs.append(abs(x-y))
        if diffs:
            gcd = diffs[0]
            # log(factor, diffs)
            for x in diffs:
                gcd = math.gcd(gcd, x)
            if gcd == 1:
                continue

        if flag:
            res += 1

    return res


for case_num in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    res = solve_(n, arr)  # include input here

    print(res)
