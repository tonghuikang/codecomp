import sys, io, os
import math, random
import heapq as hq
from collections import defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(grid,sx,sy,ex,ey):  # fix inputs here
    '''
    Given a grid, starting point and ending point, return the lowest cost
    Please configure the cost logic in the code
    I don't know how this is a template LOL
    '''
    minres = abs(sx-ex) + abs(sy-ey)
    console(minres)
    if grid == []:
        return minres

    d = defaultdict(list)
    grid = [(i,x,y) for i,(x,y) in enumerate(grid)]

    # x-order
    grid = sorted(grid, key=lambda x: x[1])
    for (i1,x1,y1),(i2,x2,y2) in zip(grid, grid[1:]):
        d[i1].append((i2,x2-x1))  # the cost is defined as the difference
        d[i2].append((i1,x2-x1))

    # y-order
    grid = sorted(grid, key=lambda x: x[2])
    for (i1,x1,y1),(i2,x2,y2) in zip(grid, grid[1:]):
        d[i1].append((i2,y2-y1))  # the cost is defined as the difference
        d[i2].append((i1,y2-y1))

    for i,x,y in grid:
        # start to x-axis
        d[-2].append((i,abs(x-sx)))

        # start to y-axis
        d[-2].append((i,abs(y-sy)))

        # point to destination
        d[i].append((-1, abs(x-ex) + abs(y-ey)))

    res = dijkstra_with_preprocessing(d, -2, -1)

    return min(minres,res)

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


import heapq as hq
def dijkstra(G, s):
    '''
    G is a list of node to nodes and costs
    '''
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


## Usage example
# @bootstrap
# def recurse(n):
#   if (n < 2): yield n
#   yield (yield recurse(n-1)) + (yield recurse(n-2))



