#!/usr/bin/env python3
import sys

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


from math import gcd

def compute_mobius(N):
    mu = [1] * (N + 1)
    is_prime = [True] * (N + 1)
    
    mu[1] = 1  # mu(1) = 1
    for i in range(2, N + 1):
        if is_prime[i]:  # i is a prime number
            for j in range(i, N + 1, i):
                is_prime[j] = False
                if (j // i) % i == 0:
                    mu[j] = 0
                else:
                    mu[j] = -mu[j]
    
    # Reset is_prime to True for prime reidentification
    is_prime = [False, False] + [True] * (N - 1)
    for i in range(2, N + 1):
        if mu[i] == 1 or mu[i] == -1:
            for j in range(i, N + 1, i):
                is_prime[j] = False
    
    return mu

mu = compute_mobius(2 * 10 ** 6 + 10)


from functools import cache

@cache
def count_coprime(a, b):
    res = 0
    for d in range(1, min(a,b) + 1):
        res += mu[d] * (a // d) * (b // d)
    return res



def solve_(n, m):
    # your solution here

    if n > 100:
        return

    res = 0
    vals = []
    for a in range(1,n+1):
        for b in range(1,m+1):
            if (b*gcd(a,b))%(a+b) == 0:
                log(a,b,gcd(a,b))
                vals.append((gcd(a,b), a//gcd(a,b), b//gcd(a,b)))
                res += 1
    
    for val in sorted(vals):
        log(val)

    res = 0
    for g in range(2, min(n, m) + 1):
        p = n // g
        q = m // g
        val = count_coprime(p, q)
        log(g, val)
        res += val

    return res


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
    n, m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, m)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)



def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    MAX_N = 2 * 10**6
    
    # Precompute gcd values
    from math import gcd
    from sys import stdout
    
    # For each test case
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        count = 0
        
        # we iterate through all possible gcd values
        for g in range(1, min(n, m) + 1):
            # for each g, we iterate through (i, j) such that gcd(i, j) = 1
            # i and j are coprime, and we actually consider (a, b) = (g*i, g*j)
            max_i = n // g
            max_j = m // g
            for i in range(1, max_i + 1):
                for j in range(1, max_j + 1):
                    if gcd(i, j) == 1:
                        a = g * i
                        b = g * j
                        if (b * g) % (a + b) == 0:
                            count += 1
        
        results.append(str(count))
    
    stdout.write("\n".join(results) + "\n")