#!/usr/bin/env python3
import sys
# import getpass  # not available on codechef
from collections import Counter, defaultdict
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

# M9 = 10**9 + 7  # 998244353
# yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
# def log(*args):
#     if OFFLINE_TEST:
#         print('\033[36m', *args, '\033[0m', file=sys.stderr)

# def solve(*args):
#     # screen input
#     if OFFLINE_TEST:
#         log("----- solving ------")
#         log(*args)
#         log("----- ------- ------")
#     return solve_(*args)

# ---------------------------- template ends here ----------------------------

# import time
# start_time = time.time()

LARGE = 5*10**6 + 10
# LARGE = 2*10**7 + 10

def solve_(lst):
    # your solution here

    # factorise all numbers
    # populate factor count

    c = Counter(lst)
    fcount = Counter()

    for i in range(1, LARGE):
        for j in range(i, LARGE, i):
            if j in c:
                fcount[i] += c[j]
                # log("x")

    # print(time.time() - start_time)
    # print(fcount)
    # del c
    res = {i:i*x for i,x in fcount.items()}

    # log(res)

    for i in range(LARGE):
        if i not in fcount:
            continue
        for j in range(2*i, LARGE, i):
            if j not in fcount:
                continue
            y = fcount[j]
            # decrease = i*y
            # increase = j*y
            # log(diff, increase, decrease)
            res[j] = max(res[j], res[i] + (j-i) * y)
            # log("y")

        # log(res)
    # print(time.time() - start_time)

    return max(res.values())



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve_(lst)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
