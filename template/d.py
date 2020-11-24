import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


primes = set(range(2,10**5+10))
for i in range(2,10**5+10):
    for j in range(2*i,10**5+10,i):
        primes.discard(j)

primes = sorted(primes)

# print(primes)

import math

def prime_factors(nr):
    i = 0
    factors = []
    candidate = 2
    while candidate <= nr:
        candidate = primes[i]
        if candidate > math.sqrt(nr):
            factors.append(nr)
            break
        elif (nr % candidate) == 0:
            factors.append(candidate)
            nr = nr // candidate
        else:
            i = i + 1
    return factors


def solve_(x):
    # your solution here

    factors = prime_factors(x)
    console(factors)
    lst = Counter(factors)

    (v,k), = lst.most_common(1)    

    return [v]*(k-1) + [x//v**(k-1)]



def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    if not ONLINE_JUDGE:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    x = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(x)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
    print(len(res))
    print(*res)  # if printing a list