#!/usr/bin/env python3
import sys
import functools
from collections import Counter
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

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


LARGE = 2**20
p = 998244353  # CHANGE WHEN NEEDED



def modinv_p(base, p=p):
    
    # modular inverse if the modulo is a prime
    return pow(base, -1, p)  # for Python 3.8+
    # return pow(base, p-2, p)  # if Python version is below 3.8


factorial_mod_p = [1]
for i in range(1, LARGE+1):
    factorial_mod_p.append((factorial_mod_p[-1]*i)%p)

ifactorial_mod_p = [1]*(LARGE+1)
ifactorial_mod_p[LARGE] = pow(factorial_mod_p[LARGE], p-2, p)
for i in range(LARGE-1, 1, -1):
    ifactorial_mod_p[i] = ifactorial_mod_p[i+1]*(i+1)%p

def ncr_mod_p(n, r, p=p):
    # https://codeforces.com/contest/1785/submission/192389526
    if r < 0 or n < r: return 0
    num = factorial_mod_p[n]
    dem = (ifactorial_mod_p[r]*ifactorial_mod_p[n-r])%p
    return (num * dem)%p 


SIZE_OF_PRIME_ARRAY = 10**6 + 10
largest_prime_factors = get_largest_prime_factors(SIZE_OF_PRIME_ARRAY)   # take care that it begins with [1,1,2,...]
primes = [x for i,x in enumerate(largest_prime_factors[2:], start=2) if x == i]
primes_set = set(primes)



def solve_(n, arr):
    # your solution here
    n = len(arr) // 2

    c = Counter(arr)

    arr = []
    brr = []
    for k,v in c.items():
        if k in primes_set:
            arr.append(v)
        else:
            brr.append(v)

    arr.sort()
    brr.sort()

    log(arr)
    log(brr)

    if len(arr) < n:
        return 0

    common_factor = factorial_mod_p[n]
    for x in brr:
        common_factor = (common_factor * ifactorial_mod_p[x])%p

    dp = [[0 for _ in range(2*n+1)] for _ in range(2*n+1)]

    for x in range(len(arr),-1,-1):
        for y in range(n+1):
            # log(x,y,n)
            if x == len(arr) and y == 0:
                dp[x][y] = 1
                continue
            if x == len(arr):
                continue
            if y < 0:
                continue
            val = ifactorial_mod_p[arr[x]] * dp[x+1][y] + ifactorial_mod_p[arr[x]-1] * dp[x+1][y-1]
            # log(x,y,val)
            dp[x][y] = val%p

    log(common_factor)

    # res = dp[n - len(brr)]

    # val = factorial_mod_p[len(brr)]
    # q = len(brr)
    # for x in brr:
    #     val = (val*ncr_mod_p(q, x))%p
    #     q -= x
    # res = (res*val)%p
    # res = res*ncr_mod_p(n, len(brr))

    # return res%p

    return (common_factor * dp[0][n])%p


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
