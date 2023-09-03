# command to run
# python interactive_runner.py python3 interactive_google_local_testing_tool.py -- python3 interactive_google.py

# you need to download interactive_runner.py from
# https://storage.googleapis.com/coding-competitions.appspot.com/interactive_runner.py
# this is question agnostic

# you need to download interactive_google_local_testing_tool.py from the question page
# copy the testing tool code downloaded from the question page to the file
# this is question specific
# for some testing tools you might need to specify the test case and it will look something like
# python interactive_runner.py python3 interactive_google_local_testing_tool.py 0 -- python3 interactive_google.py

# interactive_google.py is the solution that you write, which is this file
# please remember to flush output
# run sys.exit() at the end as well


import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"


# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


# ---------------------------- template ends here ----------------------------


def walk():
    print("W", flush=True)
    response = list(map(int, input().split()))
    return response


def teleport(pos):
    print("T {}".format(pos + 1), flush=True)
    response = list(map(int, input().split()))
    return response


def alert(pos):
    print("E {}".format(pos), flush=True)


# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = v
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here

for case_num in range(int(input())):
    n, k = list(map(int, input().split()))
    k0 = k
    log(n, k)
    lst = list(range(n))
    random.shuffle(lst)

    _, _ = list(map(int, input().split()))

    res = []
    weights = []

    for x in lst:
        if k == 0:
            break
        k -= 1
        _, count = teleport(x)

        res.append(count)
        weights.append(1)

        if k == 0:
            break
        k -= 1
        _, count = walk()

        res.append(count)
        weights.append(1 / count)

    # log(res)
    # log(weights)

    estimate = int(sum(c * w for c, w in zip(res, weights)) / sum(weights) * n * 0.5)
    alert(estimate)

sys.exit()
