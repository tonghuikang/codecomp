#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
from functools import cache

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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


SIZE_OF_PRIME_ARRAY = 10**7 + 10
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

    if num == 0:
        # may need to edit depending on use case
        return []

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


def generate_partitions(n):
    # https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B2
    # https://code.activestate.com/recipes/218332/

    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return
        
    # modify partitions of n-1 to form partitions of n
    for p in generate_partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]


LARGE = 10**7 + 10
p = m9  # CHANGE WHEN NEEDED

factorial_mod_p = [1]
for i in range(1, LARGE + 1):
    factorial_mod_p.append((factorial_mod_p[-1] * i) % p)

ifactorial_mod_p = [1] * (LARGE + 1)
ifactorial_mod_p[LARGE] = pow(factorial_mod_p[LARGE], p - 2, p)
for i in range(LARGE - 1, 1, -1):
    # actually we can just use modinv(factorial_mod_p[r])
    # but taking modinv only once is faster
    ifactorial_mod_p[i] = ifactorial_mod_p[i + 1] * (i + 1) % p


def ncr_mod_p(n, r, p=p):
    # https://codeforces.com/contest/1785/submission/192389526
    if r < 0 or n < r:
        return 0
    num = factorial_mod_p[n]
    dem = (ifactorial_mod_p[r] * ifactorial_mod_p[n - r]) % p
    # for non-prime p, count the prime factors present in the numerator and denominator
    # https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/
    return (num * dem) % p


@cache
def modinv(base):
    # modular inverse
    # base must be relatively prime to mod
    # https://docs.python.org/3/library/functions.html#pow
    return pow(base, -1, m9)  # for Python 3.8+
    # return pow(base, mod-2, mod)  # if Python version is below 3.8



def ncr_mod_p(n, r, p=p):
    # https://codeforces.com/contest/1785/submission/192389526
    if r < 0 or n < r:
        return 0
    
    res = 1
    for i in range(r):
        res = (res * (n - i)) % m9
        res = (res * modinv(i + 1)) % m9

    # print("ncr", n, r, res)

    # for non-prime p, count the prime factors present in the numerator and denominator
    # https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/
    return res % m9


def solve_(n, a, b):
    # your solution here

    factors = get_prime_factors_with_precomp_sqrt(b)

    divisors = get_all_divisors_given_prime_factorization(factors)

    @cache
    def calculate_placement(value):

        all_count = 1
        factors = get_prime_factors_with_precomp_sqrt(value)
        c = Counter(factors)
        
        for k,v in c.items():
            count = 0  # number of ways to allocate prime k
            partitions = generate_partitions(v)
            for partition in partitions:
                # number of ways to allocate prime k for a given partition
                if len(partition) > n:
                    continue
                permuatations = factorial_mod_p[len(partition)]
                for occurances in Counter(partition).values():
                    permuatations = (permuatations * ifactorial_mod_p[occurances]) % m9

                combinations = ncr_mod_p(n, len(partition), m9)

                count += (combinations * permuatations) % m9
                # print(n, value, partition, combinations, permuatations)
            
            all_count = (all_count * count) % m9

        # print(n, value, count)

        return all_count % m9

    res = 0
    for left in divisors:
        if left > a:
            continue
        right = b // left

        res += calculate_placement(left) * calculate_placement(right)

    # exclude those with greater a
    # N is 1e16
    # A is 1e14

    # consider for each factor of n
    # assign left and assign right    

    # up to 1e7 prime factorization
    # with prime factors
    # how many sequences will be more than A
    # where to allocate each factor

    return res % m9


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,a,b = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,a,b)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
