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


# A recursive function used by longestPath. See below
# link for details
# https:#www.geeksforgeeks.org/topological-sorting/

 
# The function to find longest distances from a given vertex.
# It uses recursive topologicalSortUtil() to get topological
# sorting.
def longestPath(s, Stack, visited, adj, V):
    dist = [-10**9 for i in range(V)]
 
    def topologicalSortUtil(v):
        visited[v] = True
    
        # Recur for all the vertices adjacent to this vertex
        # list<AdjListNode>::iterator i
        for i in adj[v]:
            if (not visited[i[0]]):
                topologicalSortUtil(i[0])
    
        # Push current vertex to stack which stores topological
        # sort
        Stack.append(v)

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for i in range(V):
        if (visited[i] == False):
            topologicalSortUtil(i)
    # print(Stack)
 
    # Initialize distances to all vertices as infinite and
    # distance to source as 0
    dist[s] = 0
    # Stack.append(1)
 
    # Process vertices in topological order
    while (len(Stack) > 0):
       
        # Get the next vertex from topological order
        u = Stack[-1]
        del Stack[-1]
        #print(u)
 
        # Update distances of all adjacent vertices
        # list<AdjListNode>::iterator i
        if (dist[u] != 10**9):
            for i in adj[u]:
                # print(u, i)
                if (dist[i[0]] < dist[u] + i[1]):
                    dist[i[0]] = dist[u] + i[1]
 
    # Print calculated longest distances
    # print(dist)
    return max(dist)
 

def z_function(S):
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/z_algorithm.py
    # https://cp-algorithms.com/string/z-function.html
    n = len(S)
    Z = [0] * n
    l = r = 0

    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1

            l, r = i, i + z

        Z[i] = z

    Z[0] = n
    return Z


def solve_(arr):
    # your solution here

    maxres = 0
    n = len(arr)
    g = defaultdict(list)
    adj = [[] for i in range(len(arr))]

    for i,x in enumerate(arr):
        for j,y in enumerate(arr):
            if i == j:
                continue
            combined = x + "$#" + y
            frr = z_function(combined)
            log(x,y,frr)
            maxval = 0
            for a,b in enumerate(frr[-len(y):][::-1], start=1):
                if a == b:
                    maxval = a
            if maxval > 0:
                g[j].append((i, maxval))
                adj[j].append((i, maxval))

    for s in range(n):
        log(g)

        V, Stack, visited = n, [], [False for i in range(n)] 

        res = longestPath(s, Stack, visited, adj, V)
        maxres = max(maxres, res)
    # This code is contributed by mohit kumar 29.

    return maxres


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
