#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

LARGE = -10**9

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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
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




class DisjointSet:
    # github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
    # faster implementation of DSU
    def __init__(self, n: int = 0) -> None:
        if n > 0:  # constant size DSU
            self.parent_or_size = [-1] * n
        else:
            # WARNING: non-negative numeric elements only
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
                self.parent_or_size[self.parent_or_size[parent]],
            )
        return a

    def size(self, a: int) -> int:
        return -self.parent_or_size[self.find(a)]


def solve_(n, arr, mrr):
    # your solution here
    arr = [-1] + arr
    children = [set() for _ in range(n)]
    g = [set() for _ in range(n)]

    for i,x in enumerate(arr[1:], start=1):
        g[x].add(i)
        children[x].add(i)

    ds = DisjointSet(n+10)
    for i,x in enumerate(g):
        if len(x) == 1:
            child = list(x)[0]
            ds.union(i,child)

    for i in range(n):
        ds.find(i)
    
    for i in range(n):
        ds.find(i)

    replacement = {}
    ldr0 = ds.find(0)

    for i in range(n):
        ldr = ds.find(i)
        if ldr == ldr0:
            ldr = 0
        if ldr != i:
            replacement[i] = ldr

    removed = set(replacement.keys())

    for k,v in replacement.items():
        for topic in mrr[k]:
            mrr[v].add(topic)

    for x in removed:
        mrr[x] = -1

    arr = [
        -LARGE if i in removed else (
            replacement[x] if x in replacement else x
        ) for i,x in enumerate(arr)]

    children = [set() for _ in range(n)]
    g = [set() for _ in range(n)]

    for i,x in enumerate(arr[1:], start=1):
        if i in removed:
            continue
        if x in replacement:
            x = replacement[x]
        children[x].add(i)
        g[x].add(i)

    log(replacement)
    log("arr", arr)
    log(mrr)
    log("----")

    # log(g)
    # log(children)

    proc = []
    for i,x in enumerate(g):
        if i in removed:
            continue
        if len(x) == 0:
            proc.append(i)

    while proc:
        log(proc)
        cur = proc.pop()
        log(cur)

        required_set = set()
        required_set_is_set = False
        for nex in children[cur]:
            if len(children[nex]) > 0:  # is a not leaf
                if required_set_is_set:
                    required_set = required_set & mrr[nex]
                    # log(cur, "required_set_is_set", children[nex])
                else:
                    required_set_is_set = True
                    required_set = mrr[nex]
                    # log(cur, "required_set_is_set", children[nex])

        counts = Counter()
        for x in mrr[cur]:
            counts[x] += 1
        num_leaf_children = 0
        for nex in children[cur]:
            if len(children[nex]) == 0:  # is a leaf
                num_leaf_children += 1
                for x in mrr[nex]:
                    counts[x] += 1
        
        if required_set_is_set:
            curset = set()
            for x in required_set:
                if counts[x] >= num_leaf_children:
                    curset.add(x)
        else:
            curset = set()
            for x in counts.keys():
                if counts[x] >= num_leaf_children:
                    curset.add(x)

        # log(cur, "num_leaf_children", num_leaf_children, counts, required_set_is_set, required_set)

        mrr[cur] = curset

        if cur == 0:
            break

        g[arr[cur]].remove(cur)
 
        if len(g[arr[cur]]) == 0:
            proc.append(arr[cur])

    log(mrr)
    
    return len(mrr[0])


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = minus_one(arr)

    # read multiple rows
    mrr = read_strings(n)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    mrr = [set(row.split()[1:]) for row in mrr]

    res = solve(n, arr, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
