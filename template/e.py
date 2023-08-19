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


def topological_sort(map_from_node_to_nodes, all_nodes=set()):
    # leetcode.com/problems/course-schedule-ii/
    indegree_counter = defaultdict(int)
    for lst in map_from_node_to_nodes.values():
        for v in lst:
            indegree_counter[v] += 1

    if not all_nodes:  # assume all nodes are found in the map
        all_nodes = set(indegree_counter.keys()) | set(map_from_node_to_nodes)

    dq = deque([node for node in all_nodes if node not in indegree_counter])

    res = []
    while dq:
        cur = dq.popleft()
        res.append(cur)
        for nex in map_from_node_to_nodes[cur]:
            indegree_counter[nex] -= 1
            if indegree_counter[nex] == 0:
                dq.append(nex)
    return res if len(res) == len(all_nodes) else []


def solve_(n, mrr):
    # your solution here

    g = defaultdict(set)
    f = defaultdict(set)

    for i,(c,*row) in enumerate(mrr, start=1):
        for x in row:
            g[x].add(i)
            f[i].add(x)

    reachable = set([1])
    stack = [1]

    while stack:
        cur = stack.pop()
        for nex in f[cur]:
            if nex in reachable:
                continue
            stack.append(nex)
            reachable.add(nex)
    
    for x in g:
        if x not in reachable:
            del g[x]
        for q in list(g[x]):
            if q not in reachable:
                g[x].remove(q)

    return topological_sort(g)[:-1]


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

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
    mrr = read_matrix(n)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
