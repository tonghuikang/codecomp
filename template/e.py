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
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
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



def is_bipartite(map_from_node_to_nodes):
    # leetcode.com/problems/is-graph-bipartite/discuss/119514/
    graph = map_from_node_to_nodes
    n, colored = len(map_from_node_to_nodes), {}
    for i in range(n):
        if i not in colored and graph[i]:
            colored[i] = 1
            queue = collections.deque([i])
            while queue:
                cur = queue.popleft()
                for nex in graph[cur]:
                    if nex not in colored:
                        colored[nex] = -colored[cur]
                        queue.append(nex)
                    elif colored[nex] == colored[cur]:
                        return False, colored
    # you can obtain 2-coloring from the `colored` as well
    return False, colored



def solve_(n,m,crr,xrr):
    # your solution here

    res = 0

    res += xrr[crr[0]]
    xrr[crr[0]] = 0
    res += xrr[crr[-1]]
    xrr[crr[-1]] = 0

    log("base", res)
    
    seen = set(crr)

    xrr = [x if i in seen else 0 for i,x in enumerate(xrr)]

    g = defaultdict(set)

    for i,(a,b) in enumerate(zip(crr, crr[1:])):
        if a != b:
            g[a].add(b)
            g[b].add(a)

    # minimum cost to choose such that one is colored


    return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    crr = list(map(int,input().split()))
    xrr = list(map(int,input().split()))

    crr = minus_one(crr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,m,crr,xrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
