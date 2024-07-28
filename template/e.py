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


def query(pos):
    print("{}".format(pos), flush=True)

def query_tuple(a, b):
    print("{} {}".format(a, b), flush=True)


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


# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
# lst = list(map(int,input().split()))

for _ in range(int(input())):
    n, m = list(map(int,input().split()))
    list_of_node_to_nodes = [[] for _ in range(n)]
    for _ in range(m):
        a, b = list(map(int,input().split()))
        a -= 1
        b -= 1
        list_of_node_to_nodes[a].append(b)
        list_of_node_to_nodes[b].append(a)
    
    coloring = is_bipartite(list_of_node_to_nodes)

    # log(coloring)

    if coloring == False:
        query("Alice")
        for _ in range(n):
            query_tuple(1, 2)
            _, _ = list(map(int,input().split()))
        continue

    white = [i for i,x in coloring.items() if x == 1]
    black = [i for i,x in coloring.items() if x != 1]

    white_color = 1
    black_color = 2

    query("Bob")
    for _ in range(n):
        a, b = list(map(int,input().split()))

        if a == 1 or b == 1:
            if white:
                idx = white.pop()
                query_tuple(idx+1, 1)
                continue

        if a == 2 or b == 2:
            if black:
                idx = black.pop()
                query_tuple(idx+1, 2)
                continue

        if white:
            if a == 3 or b == 3:
                idx = white.pop()
                query_tuple(idx+1, 3)
                continue
            
        if black:
            if a == 3 or b == 3:
                idx = black.pop()
                query_tuple(idx+1, 3)
                continue

        raise


# -----------------------------------------------------------------------------

# your code here
