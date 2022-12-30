#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 998244353
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


def solve_(n,arr,brr):
    # your solution here

    cntr = Counter(arr + brr)
    cntr3 = Counter(arr + brr)
    if len(cntr) < n:
        return 0

    wildcards = set()
    idx1 = defaultdict(set)
    idx2 = defaultdict(set)

    xrr = []
    yrr = []

    for i,(a,b) in enumerate(zip(arr,brr)):
        if a == b and a in wildcards:
            return 0
        if a == b:
            wildcards.add(a)
            continue
        if cntr[a] == 1 and cntr[b] == 1:
            return 0
        idx1[a].add(i)
        idx2[b].add(i)

    prune = set()   # force all alternate appearances

    for i,(a,b) in enumerate(zip(arr,brr)):
        if a == b and a in wildcards:
            continue
        if a in wildcards or cntr[b] <= 1:
            if b in prune:
                return 0
            cntr3[b] -= 1
            if cntr3[b] <= 1:
                prune.add(b)
            continue
        if b in wildcards or cntr[a] <= 1:
            if a in prune:
                return 0
            cntr3[a] -= 1
            if cntr3[a] <= 1:
                prune.add(a)
            continue
    # log(arr)
    # log(brr)
    # log(prune)
    stack = list(prune)

    while stack:
        cur = stack.pop()

        for i in idx1[cur]:
            b = brr[i]
            if b in prune:
                return 0
            if b in wildcards:
                continue
            cntr3[b] -= 1
            if cntr3[b] <= 1:
                prune.add(b)
            stack.append(b)

        for i in idx2[cur]:
            a = arr[i]
            if a in prune:
                return 0
            if a in wildcards:
                continue
            cntr3[a] -= 1
            if cntr3[a] <= 1:
                prune.add(a)
            stack.append(a)

    assert not(prune & wildcards)

    # log(wildcards, prune)

    for a,b in zip(arr,brr):
        if a in wildcards or a in prune:
            assert b in wildcards or b in prune
        if a in wildcards or b in wildcards or a in prune or b in prune:
            continue
        if a > b:
            a,b = b,a
        xrr.append(a)
        yrr.append(b)

    pairs = Counter()
    num_cycles = 0

    for a,b in zip(xrr, yrr):
        if a in wildcards and b in wildcards:
            return 0
        if a in wildcards:
            continue
        if b in wildcards:
            continue
        pairs[a,b] += 1
        if pairs[a,b] == 2:
            num_cycles += 1
        if pairs[a,b] > 2:
            return 0

    g = defaultdict(list)

    cntr2 = Counter()

    for a,b in zip(xrr, yrr):
        if a in wildcards:
            continue
        if b in wildcards:
            continue
        if pairs[a,b] == 2:
            continue
        g[a].append(b)
        g[b].append(a)
        cntr2[a] += 1
        cntr2[b] += 1

    paired = set()
    for (a,b),c in pairs.items():
        if c == 2:
            paired.add(a)
            paired.add(b)

    assert len(prune | wildcards | set(cntr2.keys()) | paired) == n
    assert len(prune) + len(wildcards) + len(cntr2.keys()) + len(paired) == n

    # log(g)
    assert all(v == 2 for v in cntr2.values())
    for k,v in g.items():
        assert len(v) == 2
        assert v[0] != v[1]
        assert k != v[0]
        assert k != v[1]
        # assert len(v) == len(set(v))

    visited = set()

    for x in list(g.keys()):
        if x in visited:
            continue
        visited.add(x)
        stack = [x]
        num_cycles += 1
        while stack:
            cur = stack.pop()
            for nex in g[cur]:
                if nex in visited:
                    continue
                visited.add(nex)
                stack.append(nex)

    # (n ** something) * (2 ** something)

    log(len(wildcards), num_cycles, g)
    # log(g)
  
    return (pow(n, len(wildcards), m9) * pow(2, num_cycles, m9)) % m9


# while OFFLINE_TEST:
#     n = random.randint(1,10)
#     arr = [random.randint(1,n) for _ in range(n)]
#     brr = [random.randint(1,n) for _ in range(n)]
#     solve_(n, arr, brr)


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
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,arr,brr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
