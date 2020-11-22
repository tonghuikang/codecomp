import sys, os
import heapq as hq
import functools, collections
import math, random
from collections import Counter, defaultdict

inp = iter(sys.stdin.readlines())
input = lambda: next(inp)

nrows,_ = list(map(int,input().split()))

grid = []
for _ in range(nrows):
    grid.append(input().strip())
    
grid = ["#"*len(grid[0])] + grid + ["#"*len(grid[0])]
grid = [["#"] + list(row) + ["#"] for row in grid]

g = defaultdict(list)

for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        val = grid[i][j]
        if val != ".":
            g[val].append((i,j))

start = g["S"][0]
end = g["G"][0]

if len(g) == 2:
    print(abs(start[0] - end[0]) + abs(start[1] - end[1]))
    sys.exit()

dxy = [(1,0),(-1,0),(0,-1),(0,1)]
visited = set([start])
stack = collections.deque([(start,0)])

while stack:
    (x,y),dist = stack.popleft()
    val = grid[x][y]

    for dx,dy in dxy:
        xx,yy = x+dx, y+dy
        if grid[xx][yy] == "#":
            continue
        if (xx,yy) in visited:
            continue
        visited.add((xx,yy))
        stack.append(((xx,yy), dist+1))

    if val in g:
        for i,j in g[val]:
            if (i,j) in visited:
                continue
            stack.append(((i,j), dist+1))
            visited.add((xx,yy))
        del g[val]

    if end in visited:
        break

if end in visited:
    while stack:
        loc, dist = stack.pop()
        if loc == end:
            print(dist)
            break
else:
    print(-1)
