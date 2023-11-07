#!/usr/bin/env python3
import sys
from collections import defaultdict

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------


def solve_(lrr, rrr, vrr, crr):
    # iterate from the minimum possible value to the maximum possible value

    minval = sum(lrr)
    maxval = sum(rrr)

    appearances = defaultdict(list)

    for l,r,vr,cr in zip(lrr, rrr, vrr, crr):
        n = sum(cr)
        for v,c in zip(vr, cr):
            appearances[v].append((n,l,r,c))

    mincost = 10**18

    for target in range(minval, maxval+1):
        # go through the appearance of target

        # choose the minimum from each multiset

        # by choosing the minimum do I have enough other elements to make up the count

        required = 0

        all_non_target_chosen = maxval

        for n,l,r,c in appearances[target]:
            all_non_target_chosen -= r
            non_target = n-c
            if non_target < l:
                required += l - non_target
                all_non_target_chosen += non_target
                continue
            all_non_target_chosen += min(non_target, r)

        cost = required

        if all_non_target_chosen + required < target:
            cost = target - all_non_target_chosen

        # log(target, cost, required, all_non_target_chosen)
        mincost = min(mincost, cost) 

    return mincost


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    n = int(input())
    # k = int(input())

    lrr = []
    rrr = []

    vrr = []
    crr = []
    for _ in range(n):
        n,l,r = list(map(int,input().split()))
        lrr.append(l)
        rrr.append(r)

        vrr.append(list(map(int,input().split())))
        crr.append(list(map(int,input().split())))

    res = solve(lrr, rrr, vrr, crr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
