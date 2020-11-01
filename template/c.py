import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

from functools import reduce

# def all_divisors(n):
#     return set(reduce(list.__add__, 
#     ([i, n//i] for i in 
#     range(1, int(n**0.5) + 1) if n % i == 0)))


import math

def prime_factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if i > math.sqrt(nr):
            i = nr
        if (nr % i) == 0:
            factors.append(int(i))
            nr = nr / i
        elif i == 2:
            i = 3
        else:
            i = i + 2
    return factors


def solve_(p, q):
    if p%q:
        return p
    
    # p_fact = prime_factors(p)
    q_fact = prime_factors(q)
    c_q_fact = Counter(q_fact)

    nr = p
    p_fact = []
    for k,v in c_q_fact.items():
        while nr % k == 0:
            p_fact.append(k)
            nr = nr//k
    if nr > 1:
        p_fact.append(nr)

    console(p_fact)
    console(q_fact)

    c_p_fact = Counter(p_fact)
    maxres = 1

    for k1,v1 in c_q_fact.items():
        res = 1
        for k2,v2 in c_p_fact.items():
            if k2 != k1:
                res *= k2**v2
            else:
                res *= k1**(v1-1)
        maxres = max(maxres, res)

    return maxres

    # lst = all_divisors(p)
    # lst = sorted(lst)

    # # your solution here

    # for x in lst[::-1]:
    #     if x%q:
    #         return x

    # return p


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
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    p,q = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(p,q)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list