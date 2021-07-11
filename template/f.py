#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# import io, os  # if all integers, otherwise need to post process
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

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

def read_matrix(nrows):
    return [list(map(int,input().split())) for _ in range(nrows)]

def read_matrix_and_flatten(nrows):
    return [int(x) for i in range(nrows) for x in input().split()]

def read_strings(nrows):
    return [input().strip() for _ in range(nrows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------

def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2


def solve_(mrr,m,k):
    # your solution here

    sumrows = [sum(row) for row in mrr]
    diffs = [b-a for a,b in zip(sumrows,sumrows[1:])]

    log(diffs)

    flag = False
    if diffs[0] == diffs[1]:
        # consider first three
        pass
    else: 
        assert diffs[-1] == diffs[-2]
        flag = True
        # consider last two
        # make everything negative
        mrr = [[-x for x in row] for row in mrr[::-1]]
    
    arr = mrr[1]
    brr = mrr[2]
    crr = mrr[3]

    acnt = Counter(arr)
    bcnt = Counter(brr)
    ccnt = Counter(crr)

    # alist = 
    # blist =
    # clist = 

    g = defaultdict(list)

    for k1,v1 in acnt.items():
        for k2,v2 in bcnt.items():
            diff = k2-k1
            k3 = k2+diff
            if k3 in ccnt:
                v3 = ccnt[k3]
                v = min(v1,v2,v3)
                for i in range(v):
                    g[k1].append(k3)

    log(g)


    # clist = defaultdict(list)
    # for k,z in crr:

    # for i,x in enumerate(brr):
    # for x,v in bcnt.items():
    #     for j,y in enumerate(arr):
    #         diff = x-y
    #         if x+diff in clist:






        



    # for row in mrr:
    #     log(sum(row))

    # for row1,row2 in zip(mrr,mrr[1:]):
    #     log(sum(row2) - sum(row1))

    # consider three consecutive positons
    # maximum bipartitie matching

    

    

    # speeds = [b-a for a, b in zip(mrr[0], mrr[-1])        s
    


    return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    m,k = list(map(int,input().split()))
    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr,m,k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)