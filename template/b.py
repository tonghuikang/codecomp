import sys
import heapq as hq
import functools, collections
import math, random
from collections import Counter, defaultdict
import threading

threading.stack_size(2**27)
sys.setrecursionlimit(10**6 + 5)

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


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


def solve(grid, sx, sy, ex, ey):  # fix inputs here
    console("----- solving ------")

    grid = [[0 if cell == "#" else 1 for cell in row] for row in grid]
    grid = [[0] * len(grid[0])]*2 + grid + [[0] * len(grid[0])]*2
    grid = [[0,0] + row + [0,0] for row in grid]
    sx, sy, ex, ey = sx+1, sy+1, ex+1, ey+1

    labels = [[False for _ in row] for row in grid]
    diffs = [(-1,0), (1,0), (0,-1), (0,1)]

    g = defaultdict(set)

    @functools.lru_cache(maxsize=None)
    def dfs(x,y,cur_label):
        for dx,dy in diffs:
            xx, yy = x+dx, y+dy
            if labels[xx][yy]:
                continue
            if grid[xx][yy] == 0:
                continue
            labels[xx][yy] = cur_label
            dfs(xx,yy,cur_label)

    cur_label = 0
    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            if labels[i][j]:
                continue
            if cell == 0:
                continue
            cur_label += 1
            labels[i][j] = cur_label
            dfs(i,j,cur_label)
            
    console("label")
    console(labels)


    start = labels[sx][sy]
    end = labels[ex][ey]
    console("start and end", start, end)
    if start == end:
        return 0

    connections = defaultdict(set)

    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            if cell == 0:
                continue
            for dx in [-2,-1,0,1,2]:
                for dy in [-2,-1,0,1,2]:
                    if labels[i][j] != False and labels[i+dx][j+dy] != False:
                        if labels[i][j] != labels[i+dx][j+dy]:
                            connections[labels[i][j]].add(labels[i+dx][j+dy])
                            connections[labels[i+dx][j+dy]].add(labels[i][j])

    console("connections", connections)

    G = [[] for _ in range(cur_label+1)]

    for k,lst in connections.items():
        G[k].extend([(x,1) for x in lst])

    console("G", G)

    _, result = dijkstra(G, start)
    
    console("result", result)

    if result[end] > 10**4:
        return -1
    return result[end]



def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

def main():
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows, w = list(map(int,input().split()))
    sx, sy = list(map(int,input().split()))
    ex, ey = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(input()))

    res = solve(grid, sx, sy, ex, ey)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)

t = threading.Thread(target=main)
t.start()
t.join()
