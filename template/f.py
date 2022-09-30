#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------

def query(pos):
    print("? {}".format(pos+1), flush=True)
    response = int(input()) - 1
    assert response >= 0
    return response

def alert(arr):
    print("! {}".format(" ".join(str(x) for x in arr)), flush=True)

# -----------------------------------------------------------------------------

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
        return -self.parent_or_size[self.find(a)]

import random
# get highest degree
# get adjacent nodes
# if nodes is in previous group, join

for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    ds = DisjointSet(n)
    for i in range(n):
        ds.find(i)
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    degrees = list(map(int,input().split()))

    taken = set()
    arr = [(x,i) for i,x in enumerate(degrees)]
    # random.shuffle(arr)
    arr.sort()
    # arr.reverse()

    # log(arr)
    query_cnt = 0

    while arr:
        x,cur = arr.pop()
        if cur in taken:
            continue
        taken.add(cur)
        for _ in range(x):
            nex = query(cur)
            query_cnt += 1
            ds.union(cur, nex)
            if nex in taken:
                break
            taken.add(nex)

    assert query_cnt <= n

    for i in range(n):
        ldr = ds.find(i)

    cntr = 1
    val_to_cntr = {}
    for i in range(n):
        ldr = ds.find(i)
        if ldr not in val_to_cntr:
            val_to_cntr[ldr] = cntr
            cntr += 1

    res = [-1 for _ in range(n)]
    for i in range(n):
        res[i] = val_to_cntr[ds.find(i)]

    assert max(res) <= n
    assert min(res) >= 1

    cnt_nodes = defaultdict(int)
    cnt_edges = defaultdict(int)
    for i,x in enumerate(res):
        cnt_nodes[x] += 1
        cnt_edges[x] += degrees[i]
    
    for i in cnt_nodes.keys():
        assert cnt_edges[i] <= cnt_nodes[i]**2

    alert(res)

    # -----------------------------------------------------------------------------

    # your code here
sys.exit()
