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


def solve_(srr):
    # your solution here
    z = "Z"

    srr = [(i,x) for i,x in enumerate(srr)]
    res = [-1 for _ in srr]

    def extract(srr, pattern, idx=1):
        if not srr:
            return []

        a,b,c = pattern
        log(a,b,c)
        psum = {0:0}
        ssum = {0:srr[-1][0]}
        bsum = [0]

        left = 0
        right = 0
        mid = 0

        for i,x in srr:
            if x == b:
                mid += 1
            bsum.append(mid)

        for i,x in srr:
            i += 1
            if x == a:
                left += 1
                psum[left] = i

        for i,x in reversed(srr):
            if x == c:
                right += 1
                ssum[right] = i

        allowed = 0
        for k,v1 in sorted(psum.items()):
            if k in ssum:
                v2 = ssum[k]
                # log(k, v1, v2)
                if bsum[v2] - bsum[v1] >= k:
                    allowed = k
                else:
                    break

        allow_a = allowed
        allow_b = allowed
        allow_c = allowed

        new_srr = []
        for i,x in srr:

            # log(i,x,a,b,c)

            if x == a and allow_a > 0:
                res[i] = idx
                allow_a -= 1
                new_srr.append((i,z))

            elif x == b and allow_b > 0:
                res[i] = idx
                allow_b -= 1
                new_srr.append((i,z))

            elif x == c and allow_c > 0:
                res[i] = idx
                allow_c -= 1
                new_srr.append((i,z))

            else:
                new_srr.append((i,x))

        # log(allow_a, allow_b, allow_c)

        assert allow_a + allow_b + allow_c == 0

        # log(psum)
        # log(ssum)
        # log(bsum)
        # log(res)
        log("".join(x for i,x in new_srr if x != z))
        log()

        return new_srr

    srr = extract(srr, "ABC", idx=1)
    srr = extract(srr, "ACB", idx=2)
    srr = extract(srr, "BAC", idx=3)
    srr = extract(srr, "BCA", idx=4)
    srr = extract(srr, "CAB", idx=5)
    srr = extract(srr, "CBA", idx=6)

    # ABC
    # ACB
    # BAC
    # BCA
    # CAB
    # CBA


    return "".join(str(x) for x in res)


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
