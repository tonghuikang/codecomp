#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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


def solve_(n, w, d, mrr):
    # mrr is a polygon defined by points [(x1,y1), (x2,y2) ... ]

    mrr = mrr + [mrr[0]]

    for (x1,y1),(x2,y2) in zip(mrr, mrr[1:]):
        # Start Generation Here
        translated = [(x - x1, y - y1) for x, y in mrr]
        angle = math.atan2(y2 - y1, x2 - x1)
        cos_theta = math.cos(-angle)
        sin_theta = math.sin(-angle)
        rotated_mrr = [(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta) for x, y in translated]
        
        m = max(x for x,y in rotated_mrr)
        
        # check if line segment (m, w), (m-d, w) intersects with the polygon
        # Start Generation Here
        # Define the line segment endpoints
        A = (m + 1e-15, w + 1e-15)
        B = (m - d + 1e-15, w + 1e-15)

        def segments_intersect(p1, p2, p3, p4):
            def orientation(a, b, c):
                val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
                if val == 0:
                    return 0  # colinear
                return 1 if val > 0 else 2  # clockwise or counterclockwise

            o1 = orientation(p1, p2, p3)
            o2 = orientation(p1, p2, p4)
            o3 = orientation(p3, p4, p1)
            o4 = orientation(p3, p4, p2)

            # General case
            if o1 != o2 and o3 != o4:
                return True

            # Special Cases
            # p1, p2 and p3 are colinear and p3 lies on segment p1p2
            if o1 == 0 and on_segment(p1, p3, p2):
                return True

            # p1, p2 and p4 are colinear and p4 lies on segment p1p2
            if o2 == 0 and on_segment(p1, p4, p2):
                return True

            # p3, p4 and p1 are colinear and p1 lies on segment p3p4
            if o3 == 0 and on_segment(p3, p1, p4):
                return True

            # p3, p4 and p2 are colinear and p2 lies on segment p3p4
            if o4 == 0 and on_segment(p3, p2, p4):
                return True

            return False

        def on_segment(a, b, c):
            if min(a[0], c[0]) <= b[0] <= max(a[0], c[0]) and min(a[1], c[1]) <= b[1] <= max(a[1], c[1]):
                return True
            return False

        intersects = False
        for i in range(len(rotated_mrr)):
            C = rotated_mrr[i]
            D = rotated_mrr[(i + 1) % len(rotated_mrr)]
            if segments_intersect(A, B, C, D):
                intersects = True
                break

        if intersects:
            # Handle the intersection case as needed
            continue

        return "Yes"
        
    return "No"


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,w,d = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, w, d, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
