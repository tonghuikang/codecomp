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


def solve_ref(n, drr, crr):
    # your solution here
    minres = 10**18

    for perm in itertools.permutations(list(range(n))):
        res = 0
        current_cars = [0 for _ in range(n)]
        for x in perm:
            res += max(0, crr[x] - current_cars[x])
            current_cars[x] -= crr[x]
            current_cars[drr[x]] += crr[x]
        minres = min(minres, res)

    return minres


def solve_(n, drr, crr):
    # your solution here

    # prune all nodes with no incoming

    g = defaultdict(set)

    for i,x in enumerate(drr):
        g[x].add(i)

    current_cars = [0 for _ in range(n)]
    visited = set()
    prune = []

    res = 0

    for i in range(n):
        if len(g[i]) == 0:
            prune.append(i)

    while prune:
        cur = prune.pop()
        visited.add(cur)
        res += max(0, crr[cur] - current_cars[cur])
        nex = drr[cur]
        current_cars[nex] += crr[cur]
        g[nex].remove(cur)
        if len(g[nex]) == 0:
            prune.append(nex)

    # what remains is cycles

    for cur in range(n):
        minpenalty = 10**18

        if cur in visited:  # pruned
            continue
        visited.add(cur)
        sequence = [cur]
        while True:
            cur = drr[cur]
            if cur in visited:
                break
            visited.add(cur)
            sequence.append(cur)
        
        starting_count = [current_cars[x] for x in sequence]
        ending_count = [x for x in starting_count]

        for i,x in enumerate(sequence):
            ending_count[(i+1)%len(sequence)] += crr[x]

        # log()
        # log(sequence)
        # log(starting_count)
        # log(ending_count)

        for i,x in enumerate(sequence):
            res += max(0, crr[x] - ending_count[i])
            penalty = max(0, crr[x] - starting_count[i]) + max(0, crr[x] - ending_count[i])
            minpenalty = min(minpenalty, penalty)
        
        res += minpenalty

    return res



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    drr = list(map(int,input().split()))
    crr = list(map(int,input().split()))
    drr = minus_one(drr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, drr, crr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
