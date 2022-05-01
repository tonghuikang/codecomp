#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------

n,m,a,b = list(map(int,input().split()))

# play first see who win

nice_spots = []
dx,dy = a // 2, (a+1) // 2

for xx in [-dx, n-1-dx]:
    for yy in [-dy, n-1-dy]:
        nice_spots.append()


def catcher(x1,y1,x2,y2):
    if abs(x1 - x2) + abs(y1 - y2) <= a:
        x1 = x2
        y1 = y2
        return x1,y1,x2,y2




def runner(x1,y1,x2,y2):
    for dx in [-x2, n-1-x2]:
        ydiff = b-abs(dx)

        for dy in [-ydiff, ydiff]:
            xx = x2+dx
            yy = min(m-1, max(0,y2+dy))

            if 0 <= xx < n and 0 <= yy < m and abs(xx-x1) + abs(yy-y1) > a:
                return x1,y1,xx,yy

    for dy in [-y2, m-1-y2]:
        xdiff = b-abs(dy)

        for dx in [-xdiff, xdiff]:
            yy = y2+dy
            xx = min(n-1, max(0,x2+dx))

            if 0 <= xx < n and 0 <= yy < m and abs(xx-x1) + abs(yy-y1) > a:
                return x1,y1,xx,yy

    # gg.com
    return x1,y1,x2,y2




def response(x,y,x_flipped=False,y_flipped=False,nm_flip=False,exiting=False):

    if x_flipped:
        x = n-1-x

    if y_flipped:
        y = m-1-y

    x += 1
    y += 1

    if nm_flip:
        x,y = y,x

    print("{} {}".format(x,y), flush=True)
    x1, y1 = list(map(int,input().split()))
    if x1 == x and y1 == y:
        sys.exit()

    if exiting:
        sys.exit()

    if nm_flip:
        x1,y1 = y1,x1

    x1 -= 1
    y1 -= 1

    if x_flipped:
        x1 = n-1-x1

    if y_flipped:
        y1 = m-1-y1

    return x1, y1



if a%2 == 1:
    required = a
else:
    required = a+1

play_as_catcher = False

if min(n,m) < required:
    play_as_catcher = True
if b < required:
    play_as_catcher = True

# simulate and play


x_flipped = False
y_flipped = False

x1, y1 = 0, 0
x2, y2 = n-1, m-1

if play_as_catcher:
    print("1", flush=True)
else:
    print("2", flush=True)
    x1,y1 = list(map(int,input().split()))

for i in range(100_000):
    if play_as_catcher:
        x1,y1,x2,y2,x_flipped,y_flipped = catcher(x1,y1,x2,y2,x_flipped,y_flipped)
        exiting = (x1 == x2 and y1 == y2)
        x2,y2 = response(x1,y1,x_flipped,y_flipped,nm_flip,exiting=exiting)
    else:
        x2,y2,x2,y2,x_flipped,y_flipped = runner(x1,y1,x2,y2,x_flipped,y_flipped)
        x1,y1 = response(x2,y2,x_flipped,y_flipped,nm_flip)
    
sys.exit()



# -----------------------------------------------------------------------------

# read line as an integer
# k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# lst = list(map(int,input().split()))

# -----------------------------------------------------------------------------

# your code here