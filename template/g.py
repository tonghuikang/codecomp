#!/usr/bin/env python3
import sys
import functools
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


def solve_(srr, trr):
    # your solution here

    s = len(srr)
    t = len(trr)

    pos = []
    for i in range(s-t+1):
        if srr[i:i+t] == trr:
            pos.append(i)

    @functools.lru_cache(maxsize=510*510)
    def dp(l,r):
        breakpoints = []
        for x in pos:
            if x >= l and x + t <= r:
                breakpoints.append(x)
        if not breakpoints:
            return 0, 1  # num step, num way
        nexres = []
        minval = s
        for x in breakpoints:
            n1, w1 = dp(l,x)
            if n1 != 0:
                continue
            n2, w2 = dp(x+t,r)
            n = n1 + n2 + 1
            w = (w1 * w2)%m9
            nexres.append((n,w))
            minval = min(minval, n)

        way = 0
        for n,w in nexres:
            if n == minval:
                way += w
        # log(l,r,breakpoints,minval, way)
        return minval, way

    return dp(0, s)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    srr = input().strip()
    trr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, trr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x%m9) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
