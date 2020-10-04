import sys, io, os
import math, random
import heapq as hq
from collections import defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass

# if Codeforces environment
if os.path.exists('input.txt'):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass

if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


def solve(*args):
    # screen input
    console("----- solving ------")
    console(*args)
    console("----- ------- ------")
    return solve_(*args)


def solve_(grid,sx,sy,ex,ey):  # fix inputs here

    minres = abs(sx-ex) + abs(sy-ey)
    console(minres)
    if grid == []:
        return minres

    d = defaultdict(list)
    grid = [(i,x,y) for i,(x,y) in enumerate(grid)]

    # x-order
    grid = sorted(grid, key=lambda x: x[1])
    for (i1,x1,y1),(i2,x2,y2) in zip(grid, grid[1:]):
        d[i1].append((i2,x2-x1))
        d[i2].append((i1,x2-x1))

    # y-order
    grid = sorted(grid, key=lambda x: x[2])
    for (i1,x1,y1),(i2,x2,y2) in zip(grid, grid[1:]):
        d[i1].append((i2,y2-y1))
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



# fast read all
for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _, nrows = list(map(int,input().split()))
    sx,sy,ex,ey = list(map(int,input().split()))

    # currow = 2
    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for z in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid,sx,sy,ex,ey)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)





