import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

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


def solve(grid, nrows):  # fix inputs here
    console("----- solving ------")

    g = defaultdict(list)
    for a,b in grid:
        a = a-1
        b = b-1
        g[a].append(b)
        g[b].append(a)

    prev = [-1 for _ in range(nrows)]
    depths = [-1 for _ in range(nrows)]
    stack = [0]

    @bootstrap
    def explore(node, depth):
        for nex in g[node]:
            if prev[nex] == -1:
                prev[nex] = node
                depths[nex] = depth+1
                yield explore(nex, depth+1)
        yield
    
    prev[0] = -2
    depths[0] = 0
    explore(0, 0)

    console(prev)
    console(depths)

    argmax = depths.index(max(depths))
    prev = [-1 for _ in range(nrows)]
    depths = [-1 for _ in range(nrows)]

    prev[argmax] = -2
    depths[argmax] = 0
    explore(argmax, 0)

    console(prev)
    console(depths)

    max_depths = max(depths)

    if max_depths%2 == 0:
        print("1 2")
        print("2 1")
        return

    if depths.count(max_depths) == 1:
        # x - y - ?? - a - b
        # x - y - ?? - a        +  y - b
        # break a - b
        # add   y - b
        x = argmax
        y = depths.index(1)
        a = depths.index(max_depths-1)
        b = depths.index(max_depths)
        print("{} {}".format(a+1, b+1))
        print("{} {}".format(y+1, b+1))
        return

    else:
        # x - y - ?? - a - b    +  x - y - ?? - c - d   # maybe a == c
        # x - y - ?? - a - b - d
        # break c - d
        # add   b - d
        b = depths.index(max_depths)
        a = g[b][0]  # guaranteed length one
        d = depths[::-1].index(max_depths)
        c = g[d][0]  # guaranteed length one
        print("{} {}".format(c+1, d+1))
        print("{} {}".format(b+1, d+1))
        return


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    nrows = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows-1):
        grid.append(list(map(int,input().split())))

    res = solve(grid, nrows)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
