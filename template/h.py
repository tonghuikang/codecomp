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
LARGE = 10**13

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


def solve_(mrr):
    # your solution here

    g = defaultdict(list)
    res = [LARGE for _ in range(k)]

    for i,(a,b,c) in enumerate(mrr):
        total = a+b-c

        # for min a
        xa = min(a,c)
        xb = c - xa
        maxdiff = (b-xb) - (a-xa)

        # for min b
        xb = min(b,c)
        xa = c - xb
        mindiff = (b-xb) - (a-xa)

        g[total].append((mindiff, maxdiff, i))

    for total in g.keys():
        g[total].sort()

    log(g)

    cnt = 0
    for total in g.keys():

        curlimit = -LARGE
        curpool = []

        for left,right,i in g[total]:
            if left > curlimit:
                if curpool:
                    cnt += 1
                for j in curpool:
                    res[j] = curlimit
                curpool = []
                curlimit = right
            curlimit = min(curlimit, right)
            curpool.append(i)

        cnt += 1
        for j in curpool:
            res[j] = curlimit

    log(res)
    allset = set()
    allres = []

    for (a,b,c), diff in zip(mrr, res):
        total = a+b-c
        assert (total-diff)%2 == 0
        target_a = (total-diff)//2
        target_b = (total+diff)//2

        assert 0 <= target_a <= a
        assert 0 <= target_b <= b
        assert target_a + target_b + c == a + b

        allset.add((target_a, target_b))
        allres.append((a-target_a, b-target_b))

    assert len(allset) == cnt

    return cnt, allres



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer

    # read line as a string
    _ = input().strip()
    k = int(input())

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    cnt, res = solve(mrr)  # include input here
    print(cnt)
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
