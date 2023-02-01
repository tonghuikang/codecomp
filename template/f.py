#!/usr/bin/env python3
import sys
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


def solve_(n,k,arr,mrr):
    # your solution here

    g = defaultdict(list)

    for a,b in mrr:
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    subtree_gcd = {}
    parents = [-1 for _ in range(n)]
    children = [set() for _ in range(n)]

    stack = [0]
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex == parents[cur]:
                continue
            parents[nex] = cur
            children[cur].add(nex)
            stack.append(nex)

    # log(parents)
    # log(children)

    leaves = []

    for x in range(n):
        if len(children[x]) == 0:
            leaves.append((arr[x], x))

    heapq.heapify(leaves)

    # log(leaves)
    k -= 1

    while leaves and k:
        # log(leaves, k, children)
        val, cur = heapq.heappop(leaves)
        # log(cur)
        if cur == 0:
            break
        par = parents[cur]
        arr[par] = math.gcd(arr[par], arr[cur] * arr[cur])
        
        children[par].remove(cur)
        if len(children[par]) == 0:
            heapq.heappush(leaves, (arr[par], par))
        if val < arr[par]:
            k -= 1
        arr[cur] = 0


    brr = [x for x in arr if x != 0]
    gcd = brr[0]
    for x in brr:
        gcd = math.gcd(gcd, x)

    return arr[0] * gcd


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n-1)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,k,arr,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
