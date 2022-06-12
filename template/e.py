#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
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



LARGE = 200
p = 998244353
factorial_mod_p = [1 for _ in range(LARGE)]
for i in range(1,LARGE):
    factorial_mod_p[i] = (factorial_mod_p[i-1]*i)%p


def ncr_mod_p(n, r, p=p):
    num = factorial_mod_p[n]
    dem = factorial_mod_p[r]*factorial_mod_p[n-r]
    return (num * pow(dem, p-2, p))%p


def solve_(mrr):
    n = len(mrr)
    # your solution here

    # count doubles and triplet

    # do math

    dists = {}

    for i,(a,b) in enumerate(mrr):
        for j,(c,d) in enumerate(mrr):
            if i == j:
                continue
            dists[i,j] = abs(a-c) + abs(b-d)

    # log(dist)
    mindist_points = defaultdict(list)
    mindists = {}

    for i in range(n):
        mindist = 10**19
        for j in range(n):
            if i == j:
                continue
            dist = dists[i,j]
            mindist = min(mindist, dist)
    
        for j in range(n):
            if i == j:
                continue
            dist = dists[i,j]
            if dist == mindist:
                mindist_points[i].append(j)
        mindists[i] = mindist

    quartets = set()

    for i in range(n):
        if len(mindist_points[i]) != 3:
            continue
        for j in range(i+1, n):
            if len(mindist_points[j]) != 3:
                continue
            for k in range(j+1, n):
                if len(mindist_points[k]) != 3:
                    continue
                for l in range(k+1, n):
                    if len(mindist_points[k]) != 3:
                        continue
                    ref = dists[i,j]
                    flag = True
                    for a in [i,j,k,l]:
                        for b in [i,j,k,l]:
                            if a == b:
                                continue
                            if mindists[a] != ref:
                                flag = False
                            if dists[a,b] != ref:
                                flag = False
                    if flag:
                        quartets.add((i,j,k))

    triplets = set()

    for i in range(n):
        if len(mindist_points[i]) != 2:
            continue
        for j in range(i+1, n):
            if len(mindist_points[j]) != 2:
                continue
            for k in range(j+1, n):
                if len(mindist_points[k]) != 2:
                    continue
                if dists[i,j] == dists[j,k] == dists[k,i] == mindists[i] == mindists[j] == mindists[k]:
                    triplets.add((i,j,k))

    twins = set()

    for i in range(n):
        if len(mindist_points[i]) != 1:
            continue
        for j in range(i+1, n):
            if len(mindist_points[j]) != 1:
                continue
            if dists[i,j] == dists[j,i] == mindists[i] == mindists[j]:
                twins.add((i,j))

    # log(twins)
    # log(triplets)

    a = len(twins)
    b = len(triplets)
    c = len(quartets)

    log(a,b,c)

    coverage = defaultdict(list)

    res = 0

    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                distinct_colors = n - 1*i - 2*j - 3*k
                choice_of_twins = ncr_mod_p(a, i)
                choice_of_triplets = ncr_mod_p(b, j)
                choice_of_quartets = ncr_mod_p(c, k)
                choice_of_colors = ncr_mod_p(n, distinct_colors)
                permute_colors = factorial_mod_p[distinct_colors]
                res += permute_colors * choice_of_colors * choice_of_quartets * choice_of_triplets * choice_of_twins

    return res%p


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
