#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------

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

# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    if stack:
                        stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

LARGE = 10**6+10


visited = set()

@bootstrap
def dfs(cur, csum, res):
    csum = csum + cur
    res = res + 1

    if csum >= LARGE:
        return
    if (cur, csum) in visited:
        return
    
    visited.add((cur, csum))
    
    result[csum] = max(result[csum], res)

    for i in range(24,2,-1):
        if i*cur+csum >= LARGE:
            break
        dfs(i*cur, csum, res)


for i in range(4,25):
    log(i)
    dfs(i, 0, 0)       
    if i < 1000:  
        with open("b_dump.out", "w") as f:
            f.write(str(result))

# log(result[:10])
print(result)

# def solve_(k):
#     return result[k]



# # def solve_slow(k):
# #     g = [[] for _ in range(1000+1)]
# #     for x in range(2,1001):
# #         factors = get_all_divisors_given_prime_factorization(get_prime_factors(x))
# #         for k in factors:
# #             g[k].append(x)
    
#     # dp = [1 for _ in range(1000+1)]
#     # for i in range(1001):
#     #     for nex in g[i]:
#     #         dp[nex] = max(dp[nex], )

        
    


# # for case_num in [0]:  # no loop over test case
# # for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

#     # read line as an integer
#     k = int(input())

#     # read line as a string
#     # srr = input().strip()

#     # read one line and parse each word as a string
#     # lst = input().split()
    
#     # read one line and parse each word as an integer
#     # a,b,c = list(map(int,input().split()))
#     # lst = list(map(int,input().split()))
#     # lst = minus_one(lst)

#     # read multiple rows
#     # arr = read_strings(k)  # and return as a list of str
#     # mrr = read_matrix(k)  # and return as a list of list of int
#     # mrr = minus_one_matrix(mrr)

#     res = solve(k)  # include input here

#     # print length if applicable
#     # print(len(res))

#     # parse result
#     # res = " ".join(str(x) for x in res)
#     # res = "\n".join(str(x) for x in res)
#     # res = "\n".join(" ".join(str(x) for x in row) for row in res)

#     # print result
#     print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

#     # print(res)