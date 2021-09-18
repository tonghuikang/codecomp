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


# https://stackoverflow.com/questions/59597399/area-of-triangle-using-3-sets-of-coordinates
def get_area(x,y):
    area=( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1])) )
    assert area%2 == 0
    return abs(area//2)


# https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/408984/JavaPython-3-check-slopes-short-code-w-explanation-and-analysis.
def checkStraightLine(coordinates) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)


def euclidean_dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def solve_(mrr,x0,y0):
    if len(mrr) <= 2:
        return "IMPOSSIBLE"

    mrr.sort()
    # all triangles

    # all quads that are colinear

    minres = 10**18

    for i,(x1,y1) in enumerate(mrr):
        for j,(x2,y2) in enumerate(mrr[i+1:], start=i+1):
            for x3,y3 in mrr[j+1:]:
                log("trig coords", [x1,y1], [x2,y2], [x3,y3])
                # check if colinear

                if checkStraightLine([[x0,y0], [x1,y1], [x2,y2], [x3,y3]]):
                    continue
                if checkStraightLine([[x0,y0],          [x2,y2], [x3,y3]]):
                    continue
                if checkStraightLine([[x0,y0], [x1,y1],          [x3,y3]]):
                    continue
                if checkStraightLine([[x0,y0], [x1,y1], [x2,y2]         ]):
                    continue

                default_area = get_area([x1,x2,x3], [y1,y2,y3])
                a1 = get_area([x1,x2,x0], [y1,y2,y0])
                a2 = get_area([x1,x0,x3], [y1,y0,y3])
                a3 = get_area([x0,x2,x3], [y0,y2,y3])

                log("areas", default_area, a1+a2+a3)

                # check if outside
                if a1 + a2 + a3 > default_area:
                    continue

                # parameter = euclidean_dist(x1,y1,x2,y2,x3,y3)
                p1 = euclidean_dist(x1,y1,x2,y2      )
                p2 = euclidean_dist(x1,y1,      x3,y3)
                p3 = euclidean_dist(      x2,y2,x3,y3)
                p = p1 + p2 + p3

                log("trig", p, p1, p2, p3)
                minres = min(minres, p)


    # case that you need quad
    for i,(x1,y1) in enumerate(mrr):
        for j,(x2,y2) in enumerate(mrr[i+1:], start=i+1):
            if checkStraightLine([[x0,y0], [x1,y1], [x2,y2]]):

                assert x1 <= x2
                if not x1 <= x0 <= x2:
                    continue

                minleft = 10**18
                minright = 10**18

                if x1 == x2:
                    # no grad
                    for k,(x3,y3) in enumerate(mrr):
                        if k == i or k == j:
                            continue
                        # if x3 == x2:
                        #     continue
                        if checkStraightLine([[x3,y3], [x1,y1], [x2,y2]]):
                            continue

                        p1 = euclidean_dist(x3,y3,x1,y1)
                        p2 = euclidean_dist(x3,y3,x2,y2)
                        p = p1+p2

                        if x3 < x1:  # on left
                            minleft = min(minleft, p)

                        if x3 > x1:  # on right
                            minright = min(minright, p)

                else:
                    for k,(x3,y3) in enumerate(mrr):
                        if k == i or k == j:
                            continue
                        a = get_area([x1,x2,x3], [y1,y2,y3])
                        if a == 0:
                            continue

                        p1 = euclidean_dist(x3,y3,x1,y1)
                        p2 = euclidean_dist(x3,y3,x2,y2)
                        p = p1+p2

                        if a > 0:
                            minleft = min(minleft, p)
                        else:
                            minright = min(minright, p)

                total_p = minleft + minright
                log("total_p", minleft, minright)
                minres = min(minres, total_p)


    if minres >= 10**18:
        return "IMPOSSIBLE"

    return minres/2


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
    mrr = minus_one_matrix(mrr)
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
