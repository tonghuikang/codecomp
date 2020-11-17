import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(g,n,m):
    og = [[x for x in row] for row in grid]
    # your solution here

    x,y = 0,0
    
    res = []

    # leave the last two rows out
    # crawl based on top row

    for y in range(n-2):  # special consideration for last two rows
        for x in range(m-1):  # special consideration for last column
            if g[y][x] == 0:
                continue

            if g[y][x] == 1 and g[y][x+1] == 1:
                if g[y+1][x] == 1:
                    r = [(y,x), (y,x+1), (y+1,x)]
                else:
                    r = [(y,x), (y,x+1), (y+1,x+1)]
            if g[y][x] == 1 and g[y][x+1] == 0:
                r = [(y,x), (y+1,x), (y+1,x+1)]

            #
            assert len(r) == 3
            assert len(set(r)) == 3
            res.append(r)
            for yy,xx in r:
                g[yy][xx] = 1-g[yy][xx]
            #

        assert x+1 == m-1
        if g[y][x] == 0 and g[y][x+1] == 0:
            continue
        elif g[y][x] == 1 and g[y][x+1] == 0:
            r = [(y,x),   (y+1,x), (y+1,x+1)]
        elif g[y][x] == 0 and g[y][x+1] == 1:
            r = [(y,x+1), (y+1,x), (y+1,x+1)]
        elif g[y][x] == 1 and g[y][x+1] == 1:
            r = [(y,x), (y,x+1), (y+1,x)]
        
        #
        assert len(r) == 3
        assert len(set(r)) == 3
        res.append(r)
        for yy,xx in r:
            g[yy][xx] = 1-g[yy][xx]
        #

    # console(y, n-3)
    # assert y == n-3
    for x in range(m-2):
        if g[-2][x] == 0 and g[-1][x] == 0:
            continue
        if g[-2][x] == 1 and g[-1][x] == 0:
            r = [(-2,x), (-2,x+1), (-1,x+1)]
        if g[-2][x] == 0 and g[-1][x] == 1:
            r = [(-1,x), (-2,x+1), (-1,x+1)]
        if g[-2][x] == 1 and g[-1][x] == 1:
            if g[-2][x+1] == 1:
                r = [(-2,x), (-1,x), (-2,x+1)]
            else:
                r = [(-2,x), (-1,x), (-1,x+1)]
        #
        assert len(r) == 3
        assert len(set(r)) == 3
        res.append(r)
        for yy,xx in r:
            g[yy][xx] = 1-g[yy][xx]
        #

    l4 = [(-2,-2), (-2,-1), (-1,-2), (-1,-1)]

    if g[-2][-2] + g[-2][-1] + g[-1][-2] + g[-1][-1] == 4:
        console("resolve 4")
        r = l4[:3]
        #
        assert len(r) == 3
        assert len(set(r)) == 3
        res.append(r)
        for yy,xx in r:
            g[yy][xx] = 1-g[yy][xx]
        # console(grid)
        #

    if g[-2][-2] + g[-2][-1] + g[-1][-2] + g[-1][-1] == 1:
        console("resolve 1")
        for i,(y,x) in enumerate(l4 + l4):
            if g[y][x] == 1:
                r = (l4+l4)[i:i+3]
                break
        #
        assert len(r) == 3
        assert len(set(r)) == 3
        res.append(r)
        for yy,xx in r:
            g[yy][xx] = 1-g[yy][xx]
        # console(grid)
        #

    if g[-2][-2] + g[-2][-1] + g[-1][-2] + g[-1][-1] == 2:
        console("resolve 2")
        sett = set()
        for i,(y,x) in enumerate(l4 + l4 + l4):
            if g[y][x] == 0:
                sett.add((y,x))
            if len(sett) == 2:
                sett.add((y,x))
            if len(sett) == 3:
                break
        r = list(sett)

        #
        assert len(r) == 3
        assert len(set(r)) == 3
        res.append(r)
        for yy,xx in r:
            g[yy][xx] = 1-g[yy][xx]
        #
        # console(grid)


    if g[-2][-2] + g[-2][-1] + g[-1][-2] + g[-1][-1] == 3:
        console("resolve 3")
        r = []
        for i,(y,x) in enumerate(l4):
            if g[y][x] == 1:
                r.append((y,x))

        #
        assert len(r) == 3
        assert len(set(r)) == 3
        res.append(r)
        for yy,xx in r:
            g[yy][xx] = 1-g[yy][xx]
        #

    # console(res)
    res2 = []
    for re in res:
        re2 = []
        for a,b in re:
            if a < 0:
                a = n+a
            if b < 0:
                b = m+b
            re2.extend((a+1,b+1))
        res2.append(re2)

    # console(res2)



    # console(grid)
    assert sum(sum(row) for row in grid) == 0

    for x1,y1,x2,y2,x3,y3 in res2:
        x1,y1,x2,y2,x3,y3 = x1-1,y1-1,x2-1,y2-1,x3-1,y3-1
        og[x1][y1] = 1 - og[x1][y1]
        og[x2][y2] = 1 - og[x2][y2]
        og[x3][y3] = 1 - og[x3][y3]
    assert sum(sum(row) for row in og) == 0

    assert len(res2) <= n*m

    return res2



def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


# import random
# while True:
#     grid = [[int(random.random()) for _ in range(4)] for _ in range(4)]
#     solve_(grid,3,3)
#     # break



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
    if not ONLINE_JUDGE:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.readline


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(n):
        grid.append(list(map(int,list(input().strip()))))

    res = solve(grid,n,m)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(len(res))
    for r in res:
        print(*r)  # if printing a list