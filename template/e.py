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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


# ---------------------------- template ends here ----------------------------

from functools import cache

def alert(arr):
    arr = " ".join(str(x) for x in arr)
    print("! {}".format(arr), flush=True)


# -----------------------------------------------------------------------------


def is_bipartite(list_of_node_to_nodes):
    # leetcode.com/problems/is-graph-bipartite/discuss/119514/
    n, colored = len(list_of_node_to_nodes), {}
    for i in range(n):
        if i not in colored and list_of_node_to_nodes[i]:
            colored[i] = 1
            queue = collections.deque([i])
            while queue:
                cur = queue.popleft()
                for nex in list_of_node_to_nodes[cur]:
                    if nex not in colored:
                        colored[nex] = -colored[cur]
                        queue.append(nex)
                    elif colored[nex] == colored[cur]:
                        return False
    # you can obtain the 2-coloring from the `colored` as well
    return colored


# read line as an integer
t = int(input())

for _ in range(t):
    n = int(input())

    g = [set() for _ in range(n)]

    # those not reachable by curhead will be 0

    all_count = [2*n]
    
    @cache
    def query(i, j):
        assert i < j
        print("? {} {}".format(i+1, j+1), flush=True)
        if all_count[0] == 0:
            assert False
        all_count[0] -= 1
        log(all_count)
        response = input().strip()
        return response

    curhead = n-1
    curquery = n-2
 
    while curquery >= 0:
        a = curquery
        b = curhead
        if query(a, b) == "NO":
            g[a].add(b)
            g[b].add(a)    
        else:
            curhead = curquery
        curquery -= 1

    curhead = n-1
    curquery = n-2

    while curquery >= 0:
        a = n-1-curquery
        b = n-1-curhead
        if query(b, a) == "NO":
            g[a].add(b)
            g[b].add(a)    
        else:
            curhead = curquery
        curquery -= 1

    pairs = []

    for i in range(n-1):
        a = i
        b = i+1
        if query(a, b) == "NO":
            g[a].add(b)
            g[b].add(a)    
            pairs.append((a,b))
 
    for (a,b),(c,d) in zip(pairs, pairs[1:]):
        if b == c:
            continue
        if query(b, c) == "NO":
            g[b].add(c)
            g[c].add(b)
        elif query(b, d) == "NO":
            g[b].add(d)
            g[d].add(b)
        elif query(a, c) == "NO":
            g[a].add(c)
            g[c].add(a)
        elif query(a, d) == "NO":
            g[a].add(d)
            g[d].add(a)

    coloring = is_bipartite(g)
    log(g)
    log(coloring)

    arr = [1 for _ in range(n)]
    for i,x in coloring.items():
        if x == 1:
            arr[i] = 1
        else:
            arr[i] = 0
            
    alert(arr)



# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here
sys.exit()