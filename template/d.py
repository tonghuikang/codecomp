#!/usr/bin/env python3
import sys
from collections import Counter, defaultdict
input = sys.stdin.readline  # to read input quickly


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
    if num == 0:
        return []
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
                divs.append(divs[j] * prime_pow)

    # NOT IN SORTED ORDER
    return divs


divisors = [
    sorted(get_all_divisors_given_prime_factorization(get_prime_factors_with_precomp(x)), reverse=True)
    for x in range(1_000_000 + 5)]

for case_num in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    small_to_large = defaultdict(list)

    divisor_count = defaultdict(int)
    cntr = Counter(arr)
    allset = set(arr)

    # log(cntr)

    for k,v in cntr.items():
        for divisor in divisors[k]:
            divisor_count[divisor] += v
            if divisor != k:
                small_to_large[divisor].append(k)
    
    # log(divisor_count)

    allres = 0

    for k,v in cntr.items():
        v0 = v
        cur_counts = defaultdict(int)

        for large in small_to_large[k]:
            v += cntr[large]

        for divisor in divisors[k]:
            cur_counts[divisor] += divisor_count[divisor]
            cur_counts[divisor] -= v

        # log("cur_counts", {k:v for k,v in cur_counts.items() if v != 0})

        for divisor in divisors[k]:
            deductible = cur_counts[divisor]
            flag = False
            for d in divisors[divisor]:
                if d in allset:
                    flag = True
                cur_counts[d] -= deductible
            if flag:
                v += deductible

        res = n - v
        # log(k, v0, v, res)
        # log("cur_counts", {k:v for k,v in cur_counts.items() if v != 0})
        allres += res * v0

    # assert allres%2 == 0
    print(allres // 2)
