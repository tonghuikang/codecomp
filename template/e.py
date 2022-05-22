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

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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


def solve_(arr,mrr,n,k):
    del k
    del n
    # your solution here

    # prune the tree from the leaves
    # only prune if
        # the node is a leaf
        # the parent of the leaf has the correct value

    swap_tree_all = defaultdict(set)
    swap_to_idx = {}

    for i,(a,b) in enumerate(mrr):
        swap_tree_all[a].add(b)
        swap_tree_all[b].add(a)

        swap_to_idx[a,b] = i
        swap_to_idx[b,a] = i

    stack = []
    for k,v in swap_tree_all.items():
        if len(v) > 1:
            continue
        k2 = list(v)[0]
        if arr[k2] == k:
            stack.append(k)

    swap_tree_init = defaultdict(dict)
    for i,(a,b) in enumerate(mrr):
        swap_tree_init[a][arr[b]] = (b)
        swap_tree_init[b][arr[a]] = (a)

    stack_reserve = []
    for loc,v in swap_tree_all.items():
        if len(v) > 1:
            continue
        loc_pare = list(v)[0]
        if loc in swap_tree_init[loc_pare]:
            stack_reserve.append(tuple(sorted((loc_pare, swap_tree_init[loc_pare][loc]))))

    stack_reserve = set(stack_reserve)
    log(stack_reserve)


    res = []
    while stack:
        # log(stack)

        loc_leaf = stack.pop()
        if arr[loc_leaf] == loc_leaf:
            # already swapped
            continue
        
        # swap leaf with parent
        loc_pare = list(swap_tree_all[loc_leaf])[0]
        arr[loc_pare], arr[loc_leaf] = arr[loc_leaf], arr[loc_pare]
        res.append(swap_to_idx[loc_pare, loc_leaf])

        swap_tree_all[loc_pare].remove(loc_leaf)
        swap_tree_all[loc_leaf].remove(loc_pare)

        if len(swap_tree_all[loc_pare]) == 1:
            loc_anot = list(swap_tree_all[loc_pare])[0]
            if arr[loc_anot] == loc_pare:
                stack.append(loc_pare)
        
        if arr[loc_pare] in swap_tree_all[loc_pare]:
            loc_pare = arr[loc_pare]
            if len(swap_tree_all[loc_pare]) == 1:
                loc_anot = list(swap_tree_all[loc_pare])[0]
                if arr[loc_anot] == loc_pare:
                    stack.append(loc_pare)

    # assert len(set(res)) == len(res)
    # assert len(res) == len(mrr)
    # assert arr == sorted(arr)

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(arr,mrr,n,k)  # include input here

    # print length if applicable
    # print(len(res))
    res = [(x+1) for x in res]
    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
