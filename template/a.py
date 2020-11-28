import sys, os
import heapq as hq
import math, random, functools, collections
from collections import Counter, defaultdict
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy


OFFLINE_TEST = False
def console(*args):  # print on terminal in different color
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target):
    d = map_from_node_to_nodes_and_costs
    if target not in d:
        d[-1] = []

    # assign indexes
    idxs = {k:i for i,k in enumerate(d.keys())}

    # population array of nodes and costs
    G = [[] for _ in range(len(idxs))]
    for e,vrr in d.items():
        for v,cost in vrr:
            G[idxs[e]].append((idxs[v],cost))

    _,costs = dijkstra(G, idxs[source])
    return costs[idxs[target]]


def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [None]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights


def solve_(a,b,x,y):
    # your solution here

    g = defaultdict(list)

    for i in range(1,100+1):
        g[(1,i)].append(((2,i),x))
        g[(2,i)].append(((1,i),x))
    
    for i in range(1,99+1):
        g[(1,i+1)].append(((2,i  ),x))
        g[(2,i  )].append(((1,i+1),x))

    for i in range(1,99+1):
        g[(1,i)].append(((1,i+1),y))
        g[(2,i)].append(((2,i+1),y))
        g[(1,i+1)].append(((1,i),y))
        g[(2,i+1)].append(((2,i),y))

    return dijkstra_with_preprocessing(g, (1,a), (2,b))


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    a,b,x,y = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(a,b,x,y)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list