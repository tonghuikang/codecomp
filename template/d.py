import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict, deque

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

# G = [[(1, 6), (3, 7)],
#      [(2, 5), (3, 8), (4, -4)],
#      [(1, -2), (4, 7)],
#      [(2, -3), (4, 9)],
#      [(0, 2)]]

# print(dijkstra(G, 0))


def solve(lst):  # fix inputs here
    console("----- solving ------")
    lenlst = len(lst)
    if len(lst) == 2:
        return 1

    # join envelope
    # join local max/mins

    def get_envelop(lst):
        edges = []
        i = 0
        while i < len(lst) - 2:
            start = i
            cur = lst[i]
            curmax = lst[i+1]
            i += 1
            while curmax < cur and i < len(lst) - 1:
                i += 1
                if lst[i] > curmax:  # add edge
                    edges.append((start, i))
                curmax = max(curmax, lst[i])
        return edges

    edges_1 = get_envelop(lst)
    edges_2 = get_envelop([-x for x in lst])
    edges_3 = get_envelop(lst[::-1])
    edges_4 = get_envelop([-x for x in lst][::-1])

    edges_3 = [(lenlst - 1 - b, lenlst - 1 - a) for a,b in edges_3]
    edges_4 = [(lenlst - 1 - b, lenlst - 1 - a) for a,b in edges_4]

    console(edges_1)
    console(edges_2)
    console(edges_3)
    console(edges_4)

    def get_envelop_2(lst):
        edges = []
        i = 0
        while i < len(lst) - 1:
            start = i
            cur = lst[i]
            curmax = lst[i+1]
            i += 1
            while curmax < cur and i < len(lst) - 1:
                i += 1
                if lst[i] > curmax:  # add edge
                    edges.append((start, i))
                    curmax = max(curmax, lst[i])
                else:
                    i = i-1
                    break
        return edges

    edges_5 = get_envelop_2(lst)
    edges_6 = get_envelop_2([-x for x in lst])
    edges_7 = get_envelop_2(lst[::-1])
    edges_8 = get_envelop_2([-x for x in lst][::-1])

    edges_7 = [(lenlst - 1 - b, lenlst - 1 - a) for a,b in edges_7]
    edges_8 = [(lenlst - 1 - b, lenlst - 1 - a) for a,b in edges_8]

    console(edges_5)
    console(edges_6)
    console(edges_7)
    console(edges_8)

    edgeset = set()
    edgeset.update([(i,i+1) for i in range(lenlst-1)])
    edgeset.update(edges_1)
    edgeset.update(edges_2)
    edgeset.update(edges_3)
    edgeset.update(edges_4)
    edgeset.update(edges_5)
    edgeset.update(edges_6)
    edgeset.update(edges_7)
    edgeset.update(edges_8)

    G = [[] for _ in range(lenlst)]
    for a,b in edgeset:
        G[a].append((b,1))

    console(G)

    path, weights = dijkstra(G, 0)

    console(path)
    console(weights)

    return weights[-1]


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
