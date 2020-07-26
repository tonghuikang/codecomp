import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid,m,start,end):  # fix inputs here
    console("----- solving ------")
    start, end = start-1, end-1
    grid = [(a-1, b) for a,b in grid]
    console(grid, m, start, end)

    supplies = [x[1] for x in grid]

    g = defaultdict(list)
    for i,(a,_) in enumerate(grid[1:], start=1):
        g[i].append(a)
        g[a].append(i)

    console(g)

    visited = [False for x in grid]

    def dfs(cur):
        visited[cur] = True
        console(cur, "dfs")
        if cur == end:
            return [cur]
        for nex in g[cur]:
            if visited[nex]:
                continue
            visited[nex] = True
            path = dfs(nex)
            # visited[nex] = False
            if path:
                return [cur] + path
        return []        

    path = dfs(start)
    console(path, "path")

    visited = [False for x in grid]
    for p in path:
        visited[p] = True

    def dfs2(cur, depth=0):
        # if depth * 2 >= m:  # no point detouring
        #     return []
        sups = []
        if supplies[cur] > 0:
            sups.append((depth, supplies[cur]))
        
        for nex in g[cur]:
            if visited[nex]:
                continue
            visited[nex] = True
            sups += dfs2(nex, depth+1)
        return sups
        
    path_supps = [[]] + [dfs2(p) for p in path[1:-1]] + [[]]
    console("path_supps", path_supps)

    lst = [[(0,math.inf)] for _ in path_supps]
    lst[0] = [(0,0)]
    lst[-1] = [(0,0)]

    for i, supps in enumerate(path_supps):
        for depth, cost in supps:
            if i + depth >= len(path):
                continue
            lst[i + depth].append((depth, cost))

    console(lst)

    cost_heap = [(0,m)]  # cost, range
    heapq.heapify(cost_heap)

    for i,stn in enumerate(lst):
        while cost_heap[0][1] < i:
            heapq.heappop(cost_heap)
        for depth, cost in stn:
            min_cost = cost_heap[0][0]
            heapq.heappush(cost_heap, (min_cost + cost, i+m-depth*2))
            console(cost_heap)

    if cost_heap[0][0] == math.inf:
        return -1
    # return a string (i.e. not a list or matrix)
    return cost_heap[0][0]


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows,m,a,b = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid,m,a,b)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
