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

m1 = 10**6

@functools.lru_cache(maxsize=10**6+10)
def inv(base, p=M9):
    # modular if the modulo is a prime
    return pow(base, p-2, p)


def depth(exponent, b=m1, p=M9):
    # modular if the modulo is a prime
    return pow(inv(b), exponent, p)


def solve_(n,k,mrr,qrr):

    # log((3*inv(10))%M9)
    # log((1*inv(10))%M9)
    # log((10*inv(100))%M9)
    # log((3*inv(100))%M9)
    # log((30*inv(1000))%M9)
    # your solution here


    # independent if not parent and child

    # otherwise recalculate

    g = defaultdict(list)
    for i,(p,a,b) in enumerate(mrr, start=1):
        g[p].append((i,a,b))

    # log(g)

    p_depth = [-1 for _ in range(n)]
    p_happen = [-1 for _ in range(n)]
    p_no_happen = [-1 for _ in range(n)]
    p_happen_float = [-1 for _ in range(n)]

    p_depth[0] = 1
    p_happen[0] = k
    p_no_happen[0] = m1-k
    p_happen_float[0] = k/m1

    for p in range(n):
        for i,a,b in g[p]:
            happen    = a*p_happen[p]      + b*p_no_happen[p]
            no_happen = (m1-a)*p_happen[p] + (m1-b)*p_no_happen[p]
            # happen = happen%M9
            # no_happen = no_happen%M9
            happen_float = a/m1 * p_happen_float[p] + b/m1 * (1-p_happen_float[p])

            p_depth[i] = p_depth[p] + 1
            p_happen[i] = happen
            p_no_happen[i] = no_happen
            p_happen_float[i] = happen_float

    # log(p_depth)
    # log([x/m1**y for x,y in zip(p_no_happen, p_depth)])
    # log([x/m1**y for x,y in zip(p_happen, p_depth)])
    log(p_happen_float)

    res = []
    for a,b in qrr:
        pa = (p_happen[a]*depth(p_depth[a]))%M9
        pb = (p_happen[b]*depth(p_depth[b]))%M9
        val = pa*pb
        # log(pa,pb,p_happen[a],p_happen[b])
        log(p_happen_float[a]*p_happen_float[b])
        res.append(val%M9)

    return res


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
    n,q = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    k = int(input())

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n-1)  # and return as a list of list of int
    mrr = [(x-1,y,z) for x,y,z in mrr]

    qrr = read_matrix(q)  # and return as a list of list of int
    qrr = minus_one_matrix(qrr)

    res = solve(n,k,mrr,qrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
