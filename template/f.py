#!/usr/bin/env python3
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
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------

def query(a,b,c):
    print("? {} {} {}".format(a,b,c), flush=True)
    response = list(map(float,input().split()))
    xrr = response[0::2]
    yrr = response[1::2]
    return [[x,y] for x,y in zip(xrr, yrr)]

def alert(arr):
    res = " ".join(f"{x} {y}" for x,y in arr)
    print("! {}".format(res), flush=True)

# -----------------------------------------------------------------------------

# From GPT-4
def project_point_onto_line(x, y, a, b, c):
    # Calculate the line's magnitude
    line_magnitude = (a**2 + b**2)**0.5

    # Normalize the line coefficients
    a_normalized = a / line_magnitude
    b_normalized = b / line_magnitude
    c_normalized = c / line_magnitude

    # Calculate the distance from the point to the line
    distance = a_normalized * x + b_normalized * y + c_normalized

    # Calculate the projected point coordinates
    x_projected = x - a_normalized * distance
    y_projected = y - b_normalized * distance

    return x_projected, y_projected


X_CONST = 93.1230172983
Y_CONST = 96.3218973211
C_CONST = 98.1283719231

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    arr = query(1, 0, 0)
    yrr = [y for x,y in arr]

    arr = query(0, 1, 0)
    xrr = [x for x,y in arr]

    # log("xrr", xrr)
    # log("yrr", yrr)

    arr = query(X_CONST, Y_CONST, C_CONST)

    allres = []

    for px,py in arr:
        minres = [100,0,0]
        for x in xrr:
            for y in yrr:
                cx, cy = project_point_onto_line(x, y, X_CONST, Y_CONST, C_CONST)
                res = [(cx-px)**2 + (cy-py)**2, x, y]
                minres = min(minres, res)
        log(minres)
        allres.append([minres[1], minres[2]])

    alert(allres)


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
sys.exit()