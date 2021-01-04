#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------



def build_graph(edges, bidirectional=False, costs=None):
    g = defaultdict(list)
    if costs:
        for (a,b),cost in zip(edges, costs):
            g[a].append((b,cost))
            if bidirectional:
                g[b].append((a,cost))
    else:
        for a,b in edges:
            g[a].append(b)
            if bidirectional:
                g[b].append(a)
    return g


def dijkstra(list_of_indexes_and_costs, start):  # is it possible to do dijkstra directly?
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    length = len(list_of_indexes_and_costs)
    visited = [False]*length
    weights = [MAXINT]*length
    path = [None]*length
    queue = []
    weights[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        g, u = heapq.heappop(queue)
        visited[u] = True
        for v, w in list_of_indexes_and_costs[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    heapq.heappush(queue, (f, v))
    return path, weights


def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target, idxs=set()):
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    d = map_from_node_to_nodes_and_costs

    if target not in d:  # destination may not have outgoing paths
        d[target] = []
    if source not in d:
        return MAXINT
    
    # assign indexes
    if idxs:
        idxs = {k:i for i,k in enumerate(idxs)}
    else:
        idxs = {k:i for i,k in enumerate(d.keys())}

    # populate list of indexes and costs
    list_of_indexes_and_costs = [[] for _ in range(len(idxs))]
    for e,vrr in d.items():
        for v,cost in vrr:
            list_of_indexes_and_costs[idxs[e]].append((idxs[v],cost))

    _, costs = dijkstra(list_of_indexes_and_costs, idxs[source])
    return costs


def solve_(mrr,n):
    # your solution here
    g = build_graph(mrr, costs=[1]*len(mrr))
    log(g)
    drr = dijkstra_with_preprocessing(g, 1, 1, idxs=range(1,n+1))
    log(drr)
    return drr

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    _ = input()
    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr,n)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    print(*res)
 
    # all_res.append(res)
# print("\n".join(str(x) for x in all_res))