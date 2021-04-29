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


def solve_(mrr):
    # your solution here

    g = defaultdict(set)
    locs = {}

    for i,(a,b,c,d) in enumerate(mrr):
        # left point
        num1 = (a+b)*d
        dem1 = b*c
        gcd = math.gcd(num1, dem1)
        num1 = num1//gcd
        dem1 = dem1//gcd
        g[num1,dem1].add(i)

        # up point
        num2 = a*d
        dem2 = b*(c+d)
        gcd = math.gcd(num2, dem2)
        num2 = num2//gcd
        dem2 = dem2//gcd
        g[num2,dem2].add(i)

        locs[i] = (num1, dem1), (num2, dem2)
    

    taken = set()
    res = []

    for i in range(len(mrr)):
        if i in taken:
            continue
        (num1, dem1), (num2, dem2) = locs[i]

        g[num1,dem1].remove(i)
        g[num2,dem2].remove(i)
        taken.add(i)
        if g[num1,dem1]:
            for nex in g[num1,dem1]:
                break
            g[num1,dem1].remove(nex)
            taken.add(nex)
            res.append((i,nex))
        elif g[num2,dem2]:
            for nex in g[num2,dem2]:
                break
            g[num2,dem2].remove(nex)            
            taken.add(nex)      
            res.append((i,nex))
        else:
            pass




    # no idea how to do downstream

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    print(len(res))
    print("\n".join("{} {}".format(a+1,b+1) for a,b in res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)