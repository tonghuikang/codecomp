#!/usr/bin/env python3
import sys
from collections import defaultdict
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



class DisjointSet:
    # github.com/not522/ac-library-python/blob/master/atcoder/dsu.py

    def __init__(self, n: int = 0) -> None:
        if n > 0:  # constant size DSU
            self.parent_or_size = [-1]*n
        else:
            self.parent_or_size = defaultdict(lambda: -1)

    def union(self, a: int, b: int) -> int:
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def find(self, a: int) -> int:
        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )
        return a

    def size(self, a: int) -> int:
        return -self.parent_or_size[self.leader(a)]


def minimum_spanning_tree(edges, costs):
    # leetcode.com/problems/min-cost-to-connect-all-points
    if len(edges) == len(costs) == 0:
        return 0
    ds = DisjointSet()
    total_tree_cost = 0
    costs, edges = zip(*sorted(zip(costs, edges)))  # sort based on costs
    for cost, (u, v) in zip(costs, edges):
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            total_tree_cost += cost
    return total_tree_cost


import random

def solve_(n,m,mrr):
    # your solution here

    order = list(range(m))

    while True:
        random.shuffle(order)
        missed = set()
        res = [0 for _ in range(m)]
        ds = DisjointSet(m)
        for i in order:
            u, v  = mrr[i]
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                res[i] = 1
            else:
                missed.add(i)

        log(missed)

        ds2 = DisjointSet()
        for i in missed:
            u,v = mrr[i]
            if ds2.find(u) != ds2.find(v):
                ds2.union(u, v)
            else:
                break
        else:
            # log('no triangle')
            return res


    # for eidx in missed:
    #     a,b = mrr[eidx]
    #     for eidx2 in node_to_eidx[a]:
    #         if eidx2 in missed:
    #             continue
    #         res[eidx], res[eidx2] = res[eidx2], res[eidx]
    #         return res

    #     for eidx2 in node_to_eidx[b]:
    #         if eidx2 in missed:
    #             continue
    #         res[eidx], res[eidx2] = res[eidx2], res[eidx]
    #         return res
    
    assert False



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(m)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(n,m,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = "".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
