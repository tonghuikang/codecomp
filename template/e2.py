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
    return [list(input().split()) for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(arr, k):
    # your solution here

    # return pow(2,4*k,M9)*6

    unconstrainted = [1,1]

    res = 1
    for _ in range(k-1):
        new = 0

        # same color, 4 choices for new color, n*n-1 (don't double count the same)
        new += 4*res * 4*res

        res = new%M9

        unconstrainted.append(res)

    unconstrainted = unconstrainted[::-1]

    log(unconstrainted)

    mapp = {}
    for node, color, level in arr[::-1]:
        node = -node
        log(node, node//2)
        if node//2 in mapp:
            if mapp[node//2] == color or mapp[node//2] == -color:
                return 0
        mapp[node] = color

    # log(arr)

    # to 3 colors
    count = {}
    visited = set()
    # visited = set([-x[0] for x in arr])


    # for node, color, level in arr:
    while arr:
        # log(sorted(arr))
        node, color, level = heapq.heappop(arr)

        node = -node
        if node in visited:
            continue
        visited.add(node)

        # log("node")
        # log(node)

        left_child = node*2
        right_child = node*2+1

        res = [1,1,1]

        if left_child in count:
            a0,a1,a2 = count[left_child]
        else:
            a0,a1,a2 = [2*unconstrainted[level], 2*unconstrainted[level], 2*unconstrainted[level]]

        if right_child in count:
            b0,b1,b2 = count[right_child]
        else:
            b0,b1,b2 = [2*unconstrainted[level], 2*unconstrainted[level], 2*unconstrainted[level]]

        res[0] = a1*b2 + a2*b1 + a1*b1 + a2*b2
        res[1] = a2*b0 + a0*b2 + a2*b2 + a0*b0
        res[2] = a0*b1 + a1*b0 + a0*b0 + a1*b1

        if level == k:
            res = [1,1,1]

        if color != 0:
            col = abs(color)-1
            r2 = res[col]
            res = [0,0,0]
            res[col] = r2
        # else:
        #     res[0] *= 2
        #     res[1] *= 2
        #     res[2] *= 2

        res = [res[0]%M9, res[1]%M9, res[2]%M9]

        count[node] = res

        log(node, color, res)

        parent = node//2
        if parent in visited:
            continue

        heapq.heappush(arr, (-(parent), 0, level-1))

        if parent == 0:
            break


    return sum(count[1])%M9


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
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    mapp = {"white": 1, "yellow": -1, "green": 2, "blue": -2, "red": 2, "orange": -2}

    r = int(input())
    # read multiple rows
    arr = read_strings(r)  # and return as a list of str

    arr = [(-int(x[0]), mapp[x[1]], -2 + len(bin(int(x[0])))) for x in arr]
    arr.sort()
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, k)  # include input here


    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
