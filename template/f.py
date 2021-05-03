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


def minimum_spanning_tree(edges):
    # leetcode.com/problems/min-cost-to-connect-all-points
    if len(edges):
        return 0
    ds = DisjointSet()
    # total_tree_cost = 0
    taken_edges = []
    # costs, edges = zip(*sorted(zip(costs, edges)))  # sort based on costs
    for (u, v) in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            taken_edges.add((u,v))
            # total_tree_cost += cost
    return taken_edges


def solve_(arr, edges, req, num_nodes):
    # your solution here
    if sum(arr) < req:
        return []

    edges = minimum_spanning_tree(edges)
    # edges = set((a,b) for i,(a,b) in enumerate(edges))
    # edges_index = 

    # find leaf, rooted at zero
    g = defaultdict(set)
    for a,b in edges:
        g[a].add(b)
        g[b].add(a)


    # arr will record amount in the root
    heap = [(-a,i) for i,a in enumerate(arr)]   # -amount (if not visited), root
    heapq.heapify(heap)

    d = DisjointSet()
    visited = set()

    # idk how to implement :/
    # while heap:
    #     cur = heapq.heappop(heap)
    #     if arr[d.find(cur)] < k:
    #         continue
    #     for nex in d[cur]:
    #         d[cur].remove(nex)

    



    return ""


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    num_nodes, num_edges, req = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    edges = read_matrix(num_edges)  # and return as a list of list of int
    edges = minus_one_matrix(edges)

    res = solve(arr, edges, req, num_nodes)  # include input here
    if res == []:
        print(no)
    else:
        print(yes)
        print(res, sep="\n")
    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)