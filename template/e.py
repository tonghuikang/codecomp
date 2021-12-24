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
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(mrr, n, k):
    # your solution here

    # keep on finding the deepest node in the forest

    edges = defaultdict(list)
    for a,b in mrr:
        edges[a].append(b)
        edges[b].append(a)

    children = defaultdict(list)
    parent = {}

    stack = [0]
    visited = set(stack)

    while stack:
        cur = stack.pop()
        for nex in edges[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
            children[cur].append(nex)
            parent[nex] = cur

    log("children", children)
    log("parent", parent)

    stack = []
    subtree_size = {i:1 for i in range(n)}
    children_size = {i:len(children[i]) for i in range(n)}
    for i in range(n):
        if len(children[i]) == 0:
            stack.append(i)

    visited = set(stack)
    while stack:
        cur = stack.pop()
        if cur == 0:
            continue
        log(cur)
        nex = parent[cur]
        subtree_size[nex] += subtree_size[cur]
        children_size[nex] -= 1
        if children_size[nex] == 0:
            stack.append(nex)

    log(children_size)
    log(subtree_size)






    return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

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
    mrr = read_matrix(n-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(mrr, n, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
