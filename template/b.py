import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid, n, a, b, x, y):  # fix inputs here
    grid = [(u-1, v-1) for u,v in grid]
    a, b = a-1, b-1
    console("----- solving ------")

    # you cannot escape in a tree
    if 2*x >= y:
        console("cannot escape evenutally")
        return "Alice"

    # need to check if alice can get bob first

    # check if longest path is more than 2*x + 1    
    # traverse twice

    d = defaultdict(list)

    for u,v in grid:
        d[u].append(v)
        d[v].append(u)

    visited = [-1 for _ in range(n)]
    visited[a] = 0
    stack = [(a,0)]

    while stack:
        cur, dist = stack.pop()
        for nex in d[cur]:
            if visited[nex] != -1:
                continue
            visited[nex] = dist+1
            stack.append((nex, dist+1))
    
    console(visited)
    if visited[b] <= x:
        console("catch at first step")
        return "Alice"
    
    end = visited.index(max(visited))

    visited = [-1 for _ in range(n)]
    visited[end] = 0
    stack = [(end,0)]

    while stack:
        cur, dist = stack.pop()
        for nex in d[cur]:
            if visited[nex] != -1:
                continue
            visited[nex] = dist+1
            stack.append((nex, dist+1))

    console(visited)
    if max(visited) > 2*x:
        console("big enough")
        return "Bob"
    
    console("not big enough")
    return "Alice"



def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()
currow = 0
for case_num in range(int(inp[currow])):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    currow = currow + 1
    nrows, a, b, x, y = list(map(int,inp[currow].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows-1):
        currow = currow + 1
        grid.append(list(map(int,inp[currow].split())))

    res = solve(grid, nrows, a, b, x, y)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
