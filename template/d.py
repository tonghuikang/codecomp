import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, brr):  # fix inputs here
    console("----- solving ------")
    arr = sorted(arr, key=lambda x:x[1])
    arr = sorted(arr, key=lambda x:x[0])
    brr = sorted(brr, key=lambda x:x[1])[::-1]
    brr = sorted(brr, key=lambda x:x[0])
    console(arr)
    console(brr)

    arr2 = [arr[0]]
    miny = arr[0][1]
    for x,y in arr[1:]:
        if y >= miny:
            continue
        arr2.append([x,y])
        miny = min(miny, y)

    brr2 = [brr[-1]]
    maxy = brr[-1][1]
    for x,y in brr[::-1][1:]:
        if y <= maxy:
            continue
        brr2.append([x,y])
        maxy = max(maxy, y)
    brr2 = brr2[::-1]
    brr2 = [[-1, brr2[0][1]+1]] + brr2 + [[brr2[-1][0]+1, -1]]

    del arr, brr

    limits = {}
    
    for robx, roby in arr2:
        cur = []
        for (x1,y1),(x2,y2) in zip(brr2, brr2[1:]):
            if x2 < robx:
                continue
            if y1 < roby:
                continue
            dx = max(0, x1+1 - robx)
            dy = max(0, y2+1 - roby)
            cur.append([dx,dy])

        console("cur", cur)

        for (dx1,dy1),(dx2,dy2) in zip(cur,cur[1:]):
            console(dx2,dy1)
            if dx2 in limits:
                limits[dx2] = max(limits[dx2], dy1)
            else:
                limits[dx2] = dy1
        # limits.extend(cur)

        if cur:
            dx2, dy1 = cur[0]
            if dx2 in limits:
                limits[dx2] = max(limits[dx2], dy1)
            else:
                limits[dx2] = dy1

            dx2, dy1 = cur[-1]
            if dx2 in limits:
                limits[dx2] = max(limits[dx2], dy1)
            else:
                limits[dx2] = dy1

    if not limits:
        return 0

    del arr2, brr2

    limits = sorted(limits.items())
    console("limits", limits)

    limits = sorted(limits, key=lambda x:x[1])[::-1]
    limits = sorted(limits, key=lambda x:x[0])
    brr = limits
    brr2 = [limits[-1]]
    maxy = brr[-1][1]
    for x,y in brr[::-1][1:]:
        if y <= maxy:
            continue
        brr2.append((x,y))
        maxy = max(maxy, y)
    brr2 = brr2[::-1]

    console("limits", brr2)
    console("result", brr2)

    limits = brr2

    minres = min(limits[0][1], limits[-1][0])
    for (k1,v1),(k2,v2) in zip(limits,limits[1:]):
        minres = min(minres, k1+v2)


    return minres



def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    a,b = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    arr = []
    for _ in range(a):
        arr.append(list(map(int,input().split())))

    brr = []
    for _ in range(b):
        brr.append(list(map(int,input().split())))

    res = solve(arr, brr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
