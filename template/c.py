#!/usr/bin/env python3
import sys, getpass
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


def solve_(arr, brr, n):

    all_possible = set()
    for a,b in brr:
        all_possible.add(a)
        all_possible.add(b)
    arr = [(a,b) for a,b in arr if a in all_possible and b in all_possible] 
    # log(brr)

    reindex = {x:i for i,x in enumerate(all_possible)}

    arr = [(reindex[a], reindex[b]) for a,b in arr]
    brr = [(reindex[a], reindex[b]) for a,b in brr]

    log(arr)
    log(brr)

    g = defaultdict(list)
    c = defaultdict(int)
    for a,b in brr:
        g[a].append(b)
        g[b].append(a)
        c[a] += 1
        c[b] += 1

    trees = []
    cycles = []
    forbidden = set()
    visited = set()
    for root in range(n):
        if root in visited:
            continue
        if c[root] == 0:
            forbidden.add(root)
            continue
        stack = [root]
        count = c[root]
        visited.add(root)
        num_nodes = 1
        current_graph = set([root])
        while stack:
            cur = stack.pop()
            for nex in g[cur]:
                if nex in visited:
                    continue
                count += c[nex]
                num_nodes += 1
                visited.add(nex)
                stack.append(nex)
                current_graph.add(nex)
        log(count, num_nodes)
        if count >= num_nodes*2:
            cycles.extend(current_graph)
        else:
            trees.append(current_graph)


    # log(cycles)
    # log(forbidden)
    # log(trees)

    def evaluate(taken):
        if taken&forbidden:
            return 0
        for tree in trees:  # not all elements of a tree and be present together
            if len(tree) == len(tree & taken):
                return 0
        res = 0
        for a,b in arr:
            if a in taken and b in taken:
                res += 1
        return res

    maxres = 0
    for comb in itertools.product([0,1], repeat=n):
        taken = set([i for i,c in enumerate(comb) if c])
        res = evaluate(taken)
        # log(taken, res)
        maxres = max(maxres, res)

    return maxres


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    arr = read_matrix(m)  # and return as a list of list of int
    k = int(input())
    brr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    arr = [(a-1,b-1) for a,b in arr]
    brr = [(a-1,b-1) for a,b in brr]

    res = solve(arr, brr, n)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)