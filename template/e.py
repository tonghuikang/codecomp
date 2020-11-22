import sys, os
import heapq as hq
import functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

# def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target):

    # return costs[idxs[target]]


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


def console(*args):  
    # print on terminal in different color
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
# if os.path.exists('input.txt'):
#     ONLINE_JUDGE = True

# if ONLINE_JUDGE:
#     sys.stdin = open("input.txt","r")
#     sys.stdout = open("output.txt","w")

#     def console(*args):
#         pass


# def solve(*args):
#     # screen input
#     # if not ONLINE_JUDGE:
#     #     console("----- solving ------")
#     #     console(*args)
#     #     console("----- ------- ------")
#     return solve_(*args)


# if True:
#     # if memory is not a constraint
#     inp = iter(sys.stdin.readlines())
#     input = lambda: next(inp)
# else:
    # if memory is a constraint
input = sys.stdin.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows,_ = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(input().strip())
    #     grid.append(list(map(int,input().split())))

    # res = solve(grid)  # please change
    

    grid = ["#"*len(grid[0])] + grid + ["#"*len(grid[0])]
    grid = [["#"] + list(row) + ["#"] for row in grid]

    # map_from_node_to_nodes_and_costs
    g = defaultdict(list)

    dxy = [(-1,0), (1,0), (0,-1), (0,1)] 
    sx,sy = -1,-1
    ex,ey = -1,-1

    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            if grid[i][j] == "#":
                continue
            val = grid[i][j]
            for dx,dy in dxy:
                xx,yy = i+dx,j+dy
                if grid[xx][yy] == "#":
                    continue
                g[(i,j)].append(((xx,yy),2))

            if val != ".":
                g[(i,j)].append((val,1))
                g[val].append(((i,j),1))

    # console(g)
    del grid

    source = "G"
    target = "S"
    d = g
    if target not in d:
        d[-1] = []

    # assign indexes
    idxs = {k:i for i,k in enumerate(d.keys())}

    # population array of nodes and costs
    G = [[] for _ in range(len(idxs))]
    for e,vrr in d.items():
        for v,cost in vrr:
            G[idxs[e]].append((idxs[v],cost))

    del g
    del d

    _,costs = dijkstra(G, idxs[source])
    
    res = costs[idxs[target]]
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))
    if res > 10**6:
        print(-1)
    else:
        print(res//2 - 1)

    # Codeforces - no case number required
    # print(res)
    # print(*res)  # if printing a list