import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

import heapq as hq
import math

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


def solve(grid,sx,sy,ex,ey):  # fix inputs here
    console("----- solving ------")
    # console(grid,sx,sy,ex,ey)

    minres = abs(sx-ex) + abs(sy-ey)
    console(minres)
    if grid == []:
        return minres

    d = defaultdict(list)
    allx = sorted(set(x for x,y in grid))
    ally = sorted(set(y for x,y in grid))
    nextx = {a:b for a,b in zip(allx, allx[1:])}
    prevx = {b:a for a,b in zip(allx, allx[1:])}
    nexty = {a:b for a,b in zip(ally, ally[1:])}
    prevy = {b:a for a,b in zip(ally, ally[1:])}

    console(allx, nextx, prevx)
    console(ally, nexty, prevy)

    # i point
    # (x,0) x-axis
    # (0,y) y-axis
    # "source" source
    # "dest" destination
    for i,(x,y) in enumerate(grid):
        # x-axis to point
        d[(x,0)].append((i,0))

        # y-axis to point
        d[(0,y)].append((i,0))

        # start to x-axis
        d["source"].append(((x,0),abs(x-sx)))

        # start to y-axis
        d["source"].append(((0,y),abs(y-sy)))

        # point to destination
        d[i].append(("dest", abs(x-ex) + abs(y-ey)))

    d["dest"] = []
    console(d.keys())

    # point to adjacent x-axis
    # point to adjacent y-axis
    for i,(x,y) in enumerate(grid):
        if x in nextx:
            d[i].append(((nextx[x],0),abs(x-nextx[x])))
        if x in prevx:
            d[i].append(((prevx[x],0),abs(x-prevx[x])))
        if y in nexty:
            d[i].append(((0,nexty[y]),abs(y-nexty[y])))
        if y in prevy:
            d[i].append(((0,prevy[y]),abs(y-prevy[y])))


    # return a string (i.e. not a list or matrix)
    # console("keys", d.keys())
    # console(d)

    idxs = {k:i for i,k in enumerate(d.keys())}

    G = [[] for _ in range(len(idxs))]

    for e,vrr in d.items():
        for v,cost in vrr:
            G[idxs[e]].append((idxs[v],cost))
    # console(G)

    _,costs = dijkstra(G, idxs["source"])
    

    res = costs[idxs["dest"]]

    return min(minres, res)


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()
for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _, nrows = list(map(int,inp[0].split()))
    sx,sy,ex,ey = list(map(int,inp[1].split()))

    currow = 2
    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,inp[currow].split())))
        currow += 1

    res = solve(grid,sx,sy,ex,ey)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
