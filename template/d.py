#!/usr/bin/env python3
import sys
import heapq
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


def solve_(n,m,arr,mrr,qrr):
    # your solution here

    # just implementation?

    g = defaultdict(set)
    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)
    
    stack = [0]
    parents = [-1 for _ in range(n)]
    childrens = [set() for _ in range(n)]
    visited = set(stack)
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
            parents[nex] = cur
            childrens[cur].add(nex)

    importance = [x for x in arr]
    subtree_size = [1 for _ in range(n)]

    leaves = [i for i,x in enumerate(childrens) if len(x) == 0]

    while leaves:
        cur = leaves.pop()
        par = parents[cur]
        if par == -1:
            break
        childrens[par].remove(cur)
        importance[par] += importance[cur]
        subtree_size[par] += subtree_size[cur]
        if len(childrens[par]) == 0:
            leaves.append(par)

    mapping = [[] for _ in range(n)]
    for i,x in enumerate(parents[1:], start=1):
        heapq.heappush(mapping[x], (-subtree_size[i], i))

    removal = [[] for _ in range(n)]

    # del i
    allres = []
    for q,x in qrr:
        if q == 0:  # query
            allres.append(importance[x])
        else:  # rotate
            while removal[x] and mapping[x] and removal[x][0] == mapping[x][0]:
                heapq.heappop(removal[x])
                heapq.heappop(mapping[x])

            if not mapping[x]:  # leaf
                continue

            nss, s = heapq.heappop(mapping[x])
            father = parents[x]
            
            heapq.heappush(removal[father], (-subtree_size[x], x))
            parents[x] = s
            parents[s] = father
            subtree_size[s], subtree_size[x] = subtree_size[x], -((-subtree_size[x]) - (-subtree_size[s]))
            importance[s], importance[x] = importance[x], importance[x] - importance[s]
            heapq.heappush(mapping[s], (-subtree_size[x], x))

            log(parents)
            log(subtree_size)
            log(importance)
            log(mapping)
            log(removal)
            log()

    return allres


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n-1)  # and return as a list of list of int
    qrr = read_matrix(m)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)
    qrr = minus_one_matrix(qrr)

    res = solve(n,m,arr,mrr,qrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
