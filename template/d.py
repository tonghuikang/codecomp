import sys, os
import heapq, functools, collections, itertools
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(ax,ay,bx,by,cx,cy):
    # your solution here

    (ax,ay),(bx,by),(cx,cy) = sorted([(ax,ay),(bx,by),(cx,cy)], key=lambda x:(x[1],x[0]))
    dest = (ax,ay),(bx,by),(cx,cy)
    console(dest)

    addn = 0
    type = 0

    if bx - ax == 1 and by == ay and bx == cx and cy - by == 1:
        dx,dy = (bx,by)
        console("center b")
        console("down right")
        if dx > 0:
            dx -= 1
        addn = 1
    elif bx - ax == 1 and by == ay and ax == cx and cy - ay == 1:
        dx,dy = (ax,ay)
        type = 1
        console("center a")
        console("point down left")
    elif cy - ay == 1 and cx == ax and cy == by and cx - bx == 1:
        dx,dy = (cx,cy)
        console("center c")
        console("up right")
        console("NULL")
        type = 1
        return 0
    elif by - ay == 1 and bx == ax and by == cy and cx - bx == 1:
        dx,dy = (bx,by)
        console("center b")
        console("up left")
        if dy > 0:
            dy -= 1
        addn = 1
    else:
        console("ERROR")

    console(dx,dy)

    if type == 1:
        if (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
            return addn + 2*(abs(dx)+abs(dy)) - min(abs(dx),abs(dy))
        else:
            return addn + 2*(abs(dx)+abs(dy)) - 2*min(abs(dx),abs(dy))
    else:
        if not ((dx > 0 and dy > 0) or (dx < 0 and dy < 0)):
            return addn + 2*(abs(dx)+abs(dy)) - min(abs(dx),abs(dy))
        else:
            return addn + 2*(abs(dx)+abs(dy)) - 2*min(abs(dx),abs(dy))        



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
    if not ONLINE_JUDGE:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
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
    ax,ay,bx,by,cx,cy = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(ax,ay,bx,by,cx,cy)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list