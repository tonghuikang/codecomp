#!/usr/bin/env python3
import sys, getpass

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


def query(pos):
    print("{}".format(pos), flush=True)
    response = int(input())
    return response


def alert(pos):
    print("! {}".format(pos + 1), flush=True)
    sys.exit()


# -----------------------------------------------------------------------------

for case_num in range(int(input())):
    # read line as an integer
    n = int(input())
    arr = list(map(int,input().split()))

    arrset = set(arr)
    cur = 0
    while cur in arrset:
        cur += 1

    while True:
        cur = query(cur)
        if cur == -1:
            break

sys.exit()

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here
