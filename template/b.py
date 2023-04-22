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


def solve_ref(w,n,d,arr):
    # your solution here

    seen = set()
    idx_to_series = {}
    series_sequence = {}
    series_sequence_index = {}

    for i in range(n):
        i0 = i

        if i in seen:
            continue
        seen.add(i)
        sequence = [i]
        idx_to_series[i] = i
        i = (i+d)%n

        while i not in seen:
            seen.add(i)
            sequence.append(i)
            idx_to_series[i] = i0
            i = (i+d)%n

        series_sequence[i0] = sequence

        mapping = {}
        for i,x in enumerate(sequence):
            mapping[x] = i
        series_sequence_index[i0] = mapping

    log(series_sequence)
    log(idx_to_series)
    log(series_sequence_index)

    log("n", n)
    log("d", d)
    res = 0

    for a,b in zip(arr[::-1], arr[:w//2]):
        log(a,b)

        if idx_to_series[a] != idx_to_series[b]:
            return -1

        series_idx = idx_to_series[a]
        log(series_sequence_index[series_idx])

        p1 = series_sequence_index[series_idx][a]
        p2 = series_sequence_index[series_idx][b]
        k = len(series_sequence_index[series_idx])

        minval = abs(p1 - p2)
        for a1 in range(-2, 2):
            val = abs(p1 + a1*k - p2)
            minval = min(minval, val)
        res += minval

    return res


# modular inverse
# https://stackoverflow.com/a/29762148/5894029
modinv = lambda A,n,s=1,t=0,N=0: (
    n < 2 and t%N or modinv(
        n, A%n, t, s-A//n*t, N or n), -1
    )[n<1]


def solve_(w,n,d,arr):
    # your solution here

    log("n", n)
    log("d", d)
    res = 0
    gcd = math.gcd(n,d)
    d2 = d // gcd
    n2 = n // gcd
    dinv1 = modinv(d2, n2)
    dinv2 = modinv(n2-d2, n2)

    assert dinv1 != -1
    assert dinv2 != -1

    for a,b in zip(arr[::-1], arr[:w//2]):
        # log(a,b)

        if gcd != 1:
            if a%gcd != b%gcd:
                return -1
            
            a = a // gcd
            b = b // gcd
        
        q1 = (a*dinv1-b*dinv1)%n2
        q2 = (a*dinv2-b*dinv2)%n2

        # log(n2, d2, dinv1, dinv2, "|", a, b)
        # log(q1, q2)
        if a != b:
            assert q1 + q2 == n2
        # log()

        res += min(q1, q2)

    return res


# while True:
#     w = random.randint(2,2)
#     n = random.randint(2,6)
#     d = random.randint(1,n-1)
#     arr = [random.randint(1,n) for x in range(w)]
#     arr = minus_one(arr)
#     solve(w,n,d,arr)
#     assert solve(w,n,d,arr) == solve_ref(w,n,d,arr)

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
    w,n,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = minus_one(arr)
    
    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(w,n,d,arr)  # include input here
    if res == -1:
        res = "IMPOSSIBLE"


    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
