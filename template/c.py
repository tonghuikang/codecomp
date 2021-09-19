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
    return [[x*2 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def shoelace_formula(xs,ys):
    # https://stackoverflow.com/a/30950874/5894029
    return sum(xs[i]*ys[i-1] - xs[i-1]*ys[i] for i in range(len(xs)))

def triangle_formula(xs,ys):
    # shoelace formula is 10x slower for some reason
    return (xs[0]*ys[1] + xs[1]*ys[2] + xs[2]*ys[0]) - (xs[0]*ys[2] + xs[1]*ys[0] + xs[2]*ys[1])

def get_polygon_area(xs,ys,take_abs=True,take_double=False):
    signed_area = triangle_formula(xs,ys)  # switch to func=triangle_formula if needed for speed
    if not take_double:  # may cause precision issues idk
        signed_area = signed_area/2
    if take_abs:
        return abs(signed_area)
    return signed_area

def checkStraightLine(coordinates):
    # https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/408984/
    (x0, y0), (x1, y1) = coordinates[:2]
    return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)


def euclidean_dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def solve_(mrr,x0,y0):
    if len(mrr) <= 2:
        return "IMPOSSIBLE"

    # either triangle or quads point on intersection of diagonals
    minres = 10**18

    for i,(x1,y1) in enumerate(mrr):
        for j,(x2,y2) in enumerate(mrr[i+1:], start=i+1):
            for x3,y3 in mrr[j+1:]:

                default_area = get_polygon_area([x1,x2,x3], [y1,y2,y3], take_abs=True, take_double=True)

                a1 = get_polygon_area([x1,x2,x0], [y1,y2,y0], take_abs=True, take_double=True)
                a2 = get_polygon_area([x1,x0,x3], [y1,y0,y3], take_abs=True, take_double=True)
                a3 = get_polygon_area([x0,x2,x3], [y0,y2,y3], take_abs=True, take_double=True)

                # log("areas", default_area, a1+a2+a3)

                if a1 == 0 or a2 == 0 or a3 == 0:
                    continue

                # check if outside
                if a1 + a2 + a3 == default_area:

                    # parameter = euclidean_dist(x1,y1,x2,y2,x3,y3)
                    p1 = euclidean_dist(x1,y1,x2,y2      )
                    p2 = euclidean_dist(x1,y1,      x3,y3)
                    p3 = euclidean_dist(      x2,y2,x3,y3)
                    p = p1 + p2 + p3

                    # log("trig", p, p1, p2, p3)
                    minres = min(minres, p)


    point_set = set(tuple(point) for point in mrr)

    # case at the intersection of diagonals
    for i,(x1,y1) in enumerate(mrr):
        for j,(x2,y2) in enumerate(mrr[i+1:], start=i+1):

            if not (x1 + x2 == x0*2 and y1 + y2 == y0*2):
                continue


            for k,(x3,y3) in enumerate(mrr):
                if k == i or k == j:
                    continue

                a1 = get_polygon_area([x1,x2,x3], [y1,y2,y3], take_abs=True, take_double=True)
                if a1 == 0:
                    continue

                dx1,dy1 = x3-x1, y3-y1
                dx2,dy2 = x3-x2, y3-y2
                x4, y4 = x3 - dx1 - dx2, y3 - dy1 - dy2

                if (x4,y4) in point_set:
                    p1 = euclidean_dist(x3,y3,x1,y1)
                    p2 = euclidean_dist(x3,y3,x2,y2)
                    p3 = euclidean_dist(x4,y4,x1,y1)
                    p4 = euclidean_dist(x4,y4,x2,y2)
                    p = p1+p2+p3+p4

                    # log("quad", x1,y1,x2,y2,x3,y3,x4,y4)
                    minres = min(minres, p)

    if minres >= 10**18:
        return "IMPOSSIBLE"

    return minres



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n)  # and return as a list of list of int
    xx,yy = list(map(int,input().split()))

    res = solve(mrr,xx,yy)  # include input here
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
