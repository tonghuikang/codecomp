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


def perpendicular_line(x1, y1, a, b, c):
    if a == 0 and b == 0:
        raise ValueError("Both a and b cannot be zero.")
    elif a == 0:
        a_new, b_new, c_new = 1, 0, -x1
    elif b == 0:
        a_new, b_new, c_new = 0, 1, -y1
    else:
        a_new, b_new = b, -a
        c_new = -a_new * x1 - b_new * y1

    return a_new, b_new, c_new


def find_intersection(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        print("The lines are parallel or coincident and do not have a unique intersection point.")
        return None
    else:
        x = (b2 * c1 - b1 * c2) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return (x, y)


X_CONST_1 = 89.213721983
Y_CONST_1 = 0.2138179231
C_CONST_1 = 1.1238719833

X_CONST_2 = 0.1278316213
Y_CONST_2 = 87.213892179
C_CONST_2 = 2.1238971981

X_CONST = 93.1230172983
Y_CONST = 96.3218973211
C_CONST = 98.1283719231


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    arr = query(X_CONST_1, Y_CONST_1, C_CONST_1)
    brr = query(X_CONST_2, Y_CONST_2, C_CONST_2)

    # log("xrr", xrr)
    # log("yrr", yrr)

    arr = query(X_CONST, Y_CONST, C_CONST)

    allres = []

    for px,py in arr:
        minres = [10000,0,0]
        for ax,ay in arr:
            for bx,by in brr:
                aax, aay, aac = perpendicular_line(ax, ay, X_CONST_1, Y_CONST_1, C_CONST_1)
                bbx, bby, bbc = perpendicular_line(bx, by, X_CONST_2, Y_CONST_2, C_CONST_2)
                x, y = find_intersection(aax, aay, aac, bbx, bby, bbc)
                log(x,y)
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
