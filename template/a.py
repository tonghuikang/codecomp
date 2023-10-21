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
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
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
        # log(*args)
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

# An orthogonally contiguous set of stones of the same color is called a group.
# A group of stones is captured (and removed from the board) once no stones in the group has an adjacent empty space.


class DisjointSet:
    # leetcode.com/problems/accounts-merge/
    def __init__(self, parent={}):
        if not parent:
            parent = {}
        self.parent = parent

    def find(self, item):
        if item not in self.parent:
            self.parent[item] = item
            return item
        elif self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2


def solve_(r,c,mrr):
    # your solution here

    mrr = [list(row) for row in mrr]
    maxres = 0

    # log(mrr)

    for i in range(r):
        for j in range(c):
            if mrr[i][j] != ".":
                continue
            mrr[i][j] = "B"
            val = 0

            visited = set()
            for dx, dy in d4:
                start_x = i + dx
                start_y = j + dy
                if 0 <= start_x < r and 0 <= start_y < c:
            # for start_x in range(r):
            #     for start_y in range(c):
                    # if (start_x, start_y) in visited:
                    #     continue
                    # log(start_x, start_y)
                    if mrr[start_x][start_y] != "W":
                        continue
                    if (start_x,start_y) in visited:
                        break
                    stack = [(start_x,start_y)]
                    saved = False
                    while stack:
                        # log(stack)
                        x,y = stack.pop()
                        for dx,dy in d4:
                            xx = x+dx
                            yy = y+dy
                            if 0 <= xx < r and 0 <= yy < c and (xx,yy) not in visited:
                                if mrr[xx][yy] == ".":
                                    saved = True
                                    continue
                                if mrr[xx][yy] == "W":
                                    stack.append((xx,yy))
                                    visited.add((xx,yy))

                    if saved is False:
                        # log(i,j,start_x,start_y)
                        val += len(visited)
            
            # log()
            # log(mrr)
            maxres = max(maxres, val)
            mrr[i][j] = "."
            # return -1

    return maxres


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
    r,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    mrr = read_strings(r)  # and return as a list of str
    # mrr = read_matrix(r)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(r,c,mrr)  # include input here

    # if res > 0:
    #     res = "YES"
    # else:
    #     res = "NO"

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
