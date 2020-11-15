import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

from collections import defaultdict

import heapq as hq
import math

LARGE = 1000

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [LARGE]*n
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


# d is a map from e to [(v1,cost), (v2,cost), ...]
# node indexes can be of any data type

# define your source and target
# source = "source"
# target = "target"

# # processing edge matrix
# idxs = {k:i for i,k in enumerate(d.keys())}
# G = [[] for _ in range(len(idxs))]
# for e,vrr in d.items():
#     for v,cost in vrr:
#         G[idxs[e]].append((idxs[v],cost))

# _,costs = dijkstra(G, idxs[source])
# res = costs[idxs[target]]


def solve_(arr, grid):  
    d = defaultdict(set)
    # d2 = defaultdict(set)
    arr = [set(ar) for ar in arr]

    for abc in "abcdefghijklmnopqrstuvwxyz".upper():
        d[abc].add(abc)

    for ar in arr:
        for a in ar:
            for b in ar:
                if a != b:
                    d[a].add(b)
                    d[b].add(a)
    
    d = {k:[(x,1) for x in v] for k,v in d.items()}
    

    cost_arr = []
    for abc in "abcdefghijklmnopqrstuvwxyz".upper():
        source = abc
        # processing edge matrix
        idxs = {k:i for i,k in enumerate(d.keys())}
        G = [[] for _ in range(len(idxs))]
        for e,vrr in d.items():
            for v,cost in vrr:
                G[idxs[e]].append((idxs[v],cost))

        _,costs = dijkstra(G, idxs[source])
        # console(costs)
        cost_arr.append(costs)

    # console(cost_arr)
    mapping = {abc:i for i,abc in enumerate("abcdefghijklmnopqrstuvwxyz".upper())}

    res = []
    for x, y in grid:
        mindist = LARGE
        for a in arr[x]:
            if mindist == 2:
                break
            for b in arr[y]:
                if a == b:
                    mindist = min(mindist, 2)
                    break
                calc = 2+cost_arr[mapping[a]][mapping[b]]
                if calc < mindist:
                    mindist = min(mindist, calc)
        res.append(mindist)

    return [x if x < LARGE else -1 for x in res]
                
    
    # your solution here

    # @functools.lru_cache(maxsize=None)
    # def query(a,b):


    return ""


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    # if not ONLINE_JUDGE:
    #     console("----- solving ------")
    #     console(*args)
    #     console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _, nrows = list(map(int,input().split()))

    arr = input()
    arr = "".join(chr(a) for a in arr)
    arr = arr.split()
    # console(arr)

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    grid = [(x-1,y-1) for x,y in grid]
    res = solve(arr, grid)  # please change
    
    # print result
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, " ".join(str(r) for r in res)))

    # Codeforces - no case number required
    # print(res)
    # print(*res)  # if printing a list