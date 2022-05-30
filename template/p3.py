#!/usr/bin/env python3
import sys
# import getpass  # not available on codechef
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy


# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "htong"
OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------


n,m = list(map(int,input().split()))
mrr = [list(map(int,input().split())) for _ in range(m)]  # and return as a list of list of int
# mrr = minus_one_matrix(mrr)

# your solution here
# just get 50% of the points here

mrr.sort(key=lambda x:(x[1], -x[2]), reverse=True)

cur = 10**6 + 100
res = [0]*(n+1)
right = 0
constrained = False
increasing = True

exiting = False

for i in range(1,n+1):
    # log(right, constrained, increasing)

    if constrained:
        # check feasibility, extend right
        while mrr and mrr[-1][1] < i:
            t,a,b = mrr.pop()
            if t == 1 and not increasing:
                print(-1)
                exiting = True
                break
            if t == 2 and increasing:
                print(-1)
                exiting = True
                break
            right = max(right, b)

    if right <= i:
        constrained = False

    if increasing:
        res[i] = (res[i-1] + 1)
    else:
        res[i] = (res[i-1] - 1)

    if mrr and mrr[-1][1] == i:
        t,a,b = mrr.pop()
        constrained = True
        increasing = t == 1
        right = b

if not exiting:

    minres = min(res[1:]) - 1
    res = " ".join(str(x - minres) for x in res[1:])
    print(res)

