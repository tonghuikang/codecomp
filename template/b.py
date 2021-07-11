#!/usr/bin/env python3
import getpass  # not available on codechef
from collections import Counter, defaultdict, deque
import sys
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
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


# class FenwickTree:
#     # also known as Binary Indexed Tree
#     # binarysearch.com/problems/Virtual-Array
#     # https://leetcode.com/problems/create-sorted-array-through-instructions
#     # may need to be implemented again to reduce constant factor
#     def __init__(self, bits=47):
#         self.c = defaultdict(int)
#         self.LARGE = 2**bits
        
#     def update(self, x, increment):
#         x += 1  # to avoid infinite loop at x > 0
#         while x <= self.LARGE:
#             # increase by the greatest power of two that divides x
#             self.c[x] += increment
#             x += x & -x
        
#     def query(self, x):
#         x += 1  # to avoid infinite loop at x > 0
#         res = 0
#         while x > 0:
#             # decrease by the greatest power of two that divides x
#             res += self.c[x]
#             x -= x & -x
#         return res


def solve_(segments, k):
    # t = FenwickTree()
    diff = Counter()

    points_ctr = Counter()
    pointset = set()
    # your solution here
    for start, end in segments:
        if start + 1 == end:
            continue
        # t.update(start, 1)
        # t.update(end+1, -1)
        diff[start] += 1
        diff[end+1] += -1
        points_ctr[start] += 1
        points_ctr[end] += 1
        pointset.add(start)
        pointset.add(end)

    points = sorted(pointset)
    intervals = []  # height, space

    cs = 0
    for a in points:
        cs += diff[a]
        height = cs - points_ctr[a]
        # log(height, cs - points_ctr[a], cs, points_ctr[a])

        # assert height == cs - points_ctr[a]

        if a + 1 in diff and a + 1 not in pointset:
            cs += diff[a+1]

        if height == 0:
            continue
        space = 1
        intervals.append((height, space))

    cs = 0
    for a,b in zip(points, points[1:]):
        cs += diff[a]
        if a + 1 in diff and a + 1 not in pointset:
            cs += diff[a+1]
        
        if a + 1 == b:
            continue
        height = cs
        # assert height == cs
        if height == 0:
            continue
        space = b-a-1
        intervals.append((height, space))

    intervals.sort(reverse=True)
    # log(intervals)

    res = len(segments)
    for height, space in intervals:
        # log(height,space,res)
        if k <= space:
            res += k*height
            break
        else:
            res += space*height
            k -= space

    return res

# import random

# size = 1000
# for _ in range(1000):
#     segments = []
#     for _ in range(1000):
#         a = random.randint(1, size-1)
#         b = random.randint(a+1, size)
#         segments.append((a,b))
#     solve_(segments, 100)

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified

allres = []
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    intervals = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(intervals, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    res = "Case #{}: {}".format(case_num+1, res)
    # print()   # Google and Facebook - case number required
    allres.append(res)
print("\n".join(allres))
    # print(res)