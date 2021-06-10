#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

random.seed(42)

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

print(10**4)
for p in primes[::-1][:10**3]:
    for x in range(10):
        idx = bisect.bisect_left(primes, 10**9/p) - 50 + x
        semiprime = p*primes[idx]
        print("{} {} {}".format(1, 805306368, 2))

