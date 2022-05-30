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
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
# import getpass  # not available on codechef
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



def get_centroid(mrr, n):
    # your solution here

    assert mrr and len(mrr) >= 1

    g = collections.defaultdict(set)
    subtree_sizes = [1]*n
    parents = [-1]*n
    start = mrr[0][0]

    def entry_operation(prev, cur, nex):
        # note that prev is `null_pointer` at the root node
        parents[nex] = cur

    def exit_operation(prev, cur):
        if prev == "NULL":
            return
        subtree_sizes[prev] += subtree_sizes[cur]

    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)

    k = len(g)

    dfs(start,g,entry_operation,exit_operation)
    
    log(parents)
    log(subtree_sizes)

    res = []
    for cur,(subtree_size, parent) in enumerate(zip(subtree_sizes, parents)):
        if cur not in g:
            continue
        sides = []
        for nex in g[cur]:
            if nex != parents[cur] and cur != start:
                sides.append(subtree_sizes[nex])

        parent_size = k - sum(sides) - 1
        if parent_size != 0:
            sides.append(parent_size)

        # log(cur, sides)
        if max(sides) <= k//2 and cur != start:
            return cur

        # res.append(count(sides))

    return start


def query(pos):
    print("{}".format(pos), flush=True)
    response = int(input())
    return response


n = int(input())
mrr = read_matrix(n-1)  # and return as a list of list of int

if n == 1:
    query(1)
    sys.exit()

# if n <= 16:
#     for i in range(n):
#         i += 1
#         res = query(i)
#         if res == 0:
#             sys.exit()


while True:
    centroid = get_centroid(mrr, n+100)
    target = query(centroid)
    if target == 0:
        sys.exit()

    passing = {}
    g = defaultdict(set)
    for a,b in mrr:
        passing[a] = True
        passing[b] = True
        g[a].add(b)
        g[b].add(a)

    def entry_operation(prev, cur, nex):
        # note that prev is `null_pointer` at the root node
        if cur == centroid:
            passing[nex] = False
        else:
            passing[nex] = passing[cur]

    def exit_operation(prev, cur):
        pass

    dfs(target, g, entry_operation, exit_operation)

    passing[centroid] = False
    new_mrr = []
    for a,b in mrr:
        if (not passing[a]) or (not passing[b]):
            continue
        new_mrr.append((a,b))
    mrr = new_mrr
    # prune your tree here

    # print(mrr)

    if not mrr:
        query(target)
        sys.exit()


sys.exit()

