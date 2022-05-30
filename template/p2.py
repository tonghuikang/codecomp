#!/usr/bin/env python3
import sys
# import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
# OFFLINE_TEST = getpass.getuser() == "htong"
OFFLINE_TEST = False  # codechef does not allow getpass
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


def dfs(start, g, entry_operation, exit_operation):
    # https://codeforces.com/contest/1646/submission/148435078
    # https://codeforces.com/contest/1656/submission/150799881
    entered = set([start])
    exiting = set()
    stack = [start]
    prev = {}

    null_pointer = "NULL"
    prev[start] = null_pointer

    while stack:
        cur = stack[-1]

        if cur not in exiting:
            for nex in g[cur]:
                if nex in entered:
                    continue

                entry_operation(prev[cur], cur, nex)

                entered.add(nex)
                stack.append(nex)
                prev[nex] = cur
            exiting.add(cur)

        else:
            stack.pop()
            exit_operation(prev[cur], cur)


def solve_(mrr, k):
    # your solution here

    g = collections.defaultdict(set)
    subtree_sizes = [1]*k
    parents = [-1]*k

    def entry_operation(prev, cur, nex):
        # note that prev is `null_pointer` at the root node
        parents[nex] = cur

    def exit_operation(prev, cur):
        if cur != 0:
            subtree_sizes[prev] += subtree_sizes[cur]

    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)

    dfs(0,g,entry_operation,exit_operation)
    
    log(parents)
    log(subtree_sizes)

    def count(sides):
        res = 0

        # zero in node, all anywhere except node
        res += (k-1) ** 3

        for x in sides:
            # all three is same branch
            res -= x ** 3

            # two in same branch, one outside
            res -= x ** 2 * (k-1-x) * 3

            log(res)

        # one in node, two anywhere except node
        res += (k-1) ** 2 * 3

        for x in sides:
            # two outside node is in same branch
            res -= x ** 2 * 3

        # two in node, one anywhere except node
        res += (k-1) * 3

        # three in node
        res += 1

        return res

    res = []
    for cur,(subtree_size, parent) in enumerate(zip(subtree_sizes, parents)):
        sides = []
        for nex in g[cur]:
            if nex != parents[cur]:
                sides.append(subtree_sizes[nex])

        parent_size = k - sum(sides) - 1
        if parent_size != 0:
            sides.append(parent_size)

        # log(cur, sides)

        res.append(count(sides))

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(mrr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
