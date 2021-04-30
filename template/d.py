#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly
sys.setrecursionlimit(10**6 + 5)

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


# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def solve_(krr,mrr,root,n):
    # your solution here
    root -= 1
    specials = set([x-1 for x in krr])
    
    g = defaultdict(set)
    for a,b in mrr:
        g[a-1].add(b-1)
        g[b-1].add(a-1)

    distance = {}  # distance from root
    distance[root] = 0

    stack = [root]
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in distance:
                continue
            stack.append(nex)
            distance[nex] = distance[cur] + 1

    tagged_nodes = set()
    # tagged_nodes_item = {k:k for k in specials}
    visited = set([root])

    # @bootstrap
    def dfs(cur):
        tagged = cur in specials
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            visited.add(cur)
            is_tagged, ptr_node = dfs(nex)
            if is_tagged:   
                tagged = True
                # tagged_nodes_item[nex] = ptr_node
        if tagged:
            tagged_nodes.add(cur)
        return tagged, None
    dfs(root)

    earliest = {}  # distance from root
    earliest[root] = 0

    stack = [root]
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in earliest:
                continue
            stack.append(nex)
            if nex in tagged_nodes:
                earliest[nex] = earliest[cur] + 1
            else:
                earliest[nex] = earliest[cur]


    log([distance[i]  for i in range(n)])
    log([earliest[i]  for i in range(n)])

    return [2*earliest[i] - distance[i] for i in range(n)]



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
    n,k,a = list(map(int,input().split()))
    krr = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(n-1)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(krr,mrr,a,n)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(" ".join(str(x) for x in res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)