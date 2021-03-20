#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
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

# ---------------------------- template ends here ----------------------------



LARGE = int(2*10**7)
# LARGE = int(2*10**3)
count_factors = [0] * LARGE
largest_factor = [1] * LARGE
for i in range(2, LARGE):
    if count_factors[i]:
        continue
    for j in range(i, LARGE, i):
        count_factors[j] += 1
        largest_factor[j] = i


@functools.lru_cache(maxsize=10000)
def prime_factors(nr):
    factors = []
    lf = largest_factor[nr]
    while lf != nr:
        factors.append(lf)
        nr //= lf
        lf = largest_factor[nr]
    if nr > 1:
        factors.append(nr)
    return factors


@functools.lru_cache(maxsize=10000)
def all_divisors(prime_factors):
    divisors = []
    c = Counter(prime_factors)
    pf = c.keys()
    for comb in itertools.product(*[range(count+1) for count in c.values()]):
        div = 1
        for p,pow in zip(pf, comb):
            div *= p**pow
        divisors.append(div)
    return divisors


def solve_(c,d,x):
    # your solution here

    # div = math.gcd(math.gcd(c,d),x)
    # c,d,x = c//div, d//div, x//div

    pfs = prime_factors(x)
    candidate_gcd = all_divisors(pfs)
    # log(x, candidate_gcd)

    res = 0
    for gcd in candidate_gcd:
        rhs = x + d*gcd
        if rhs % c:
            continue
        lcm = rhs // c

        if lcm%gcd:
            continue

        # p1 = Counter(prime_factors(gcd))
        # p2 = Counter(prime_factors(lcm//gcd))

        cnt = count_factors[lcm//gcd]
        # for k in p2:
        #     if p2[k] > p1[k]:
        #         cnt += 1

        res += 1 << cnt

        # log(gcd, lcm, p1, p2, cnt)

    return res
    


def check(c,d,x):
# def solve_(c,d,x):
    res = 0
    for a in range(1,410):
        for b in range(a,410):
            if c*a*b//math.gcd(a,b) - d*math.gcd(a,b) == x:
                lcm = a*b//math.gcd(a,b)
                gc = math.gcd(a,b)
                # log(lcm,gc,lcm/gc)
                cout = [a,b,a*b,lcm,gc,c*a*b//math.gcd(a,b),d*math.gcd(a,b),lcm//gc]
                log("\t".join(str(x) for x in cout))
                if a == b:
                    res += 1
                else:
                    res += 2

    return res

# if True:
#     for c in range(1,10):
#         for d in range(1,10):
#             for x in range(1,10):
#                 if solve_(c,d,x) != check(c,d,x):
#                     log(c,d,x,solve_(c,d,x),check(c,d,x))
#                     assert False

                


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    c,d,x = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(c,d,x)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)