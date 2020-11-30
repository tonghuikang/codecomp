import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


  
# # A wrapper over recursive  
# # function findPeakUtil() 
# def findPeak(arr, n): 
  
#     return findPeakUtil(arr, 0, n - 1, n) 


def solve_(ax,ay,bx,by,cx,cy,dx,dy):
    xx = sorted([ax,bx,cx,dx])
    yy = sorted([ay,by,cy,dy])

    # if they lie on a line, take the median

    mx = sum(sorted([ax,bx,cx,dx])[1:3]) / 2
    my = sum(sorted([ay,by,cy,dy])[1:3]) / 2

    if ax == bx == cx == dx:
        return int(sum([abs(ay - my), abs(by - my), abs(cy - my), abs(dy - my)]))

    if ay == by == cy == dy:
        return int(sum([abs(ax - mx), abs(bx - mx), abs(cx - mx), abs(dx - mx)]))


    # A binary search based function  
    # that returns index of a peak element 
    def findPeakUtil(func, low, high, n): 
        
        # Find index of middle element 
        # (low + high)/2  
        mid = low + (high - low)/2 
        mid = int(mid) 
        
        # Compare middle element with its  
        # neighbours (if neighbours exist) 
        if ((mid == 0 or func(mid - 1) <= func(mid)) and 
            (mid == n - 1 or func(mid + 1) <= func(mid))): 
            return mid 
    
    
        # If middle element is not peak and  
        # its left neighbour is greater  
        # than it, then left half must  
        # have a peak element 
        elif (mid > 0 and func(mid - 1) > func(mid)): 
            return findPeakUtil(func, low, (mid - 1), n) 
    
        # If middle element is not peak and 
        # its right neighbour is greater 
        # than it, then right half must  
        # have a peak element 
        else: 
            return findPeakUtil(func, (mid + 1), high, n) 


    diff = [-1,0,-1]
    minres = -10**10
    n = 10**9 + 10**8

    for kx in diff:
        for ky in diff:
            cx, cy = mx + kx, my + ky

            cx = int(cx)
            cy = int(cy)

            def func(length):
                px,qx,rx,sx = cx + length, cx + length, cx - length, cx - length
                py,qy,ry,sy = cy + length, cy + length, cy - length, cy - length

                for (ex,ey),(fx,fy),(gx,gy),(hx,hy) in itertools.permutations([(px,py),(qx,qy),(rx,ry),(sx,sy)]):
                    res = abs(ex - ax) + abs(fx - bx) + abs(gx - cx) + abs(hx - dx) + abs(ey - ay) + abs(fy - by) + abs(gy - cy) + abs(hy - dy)
                return -res

            res2 = findPeakUtil(func, 0, n - 1, n) 
            minres = max(minres, res2)

            # def func(length):
            #     px,qx,rx,sx = cx + length + 0.5, cx + length + 0.5, cx - length - 0.5, cx - length - 0.5
            #     py,qy,ry,sy = cy + length + 0.5, cy - length - 0.5, cy + length + 0.5, cy - length - 0.5

            #     for (ex,ey),(fx,fy),(gx,gy),(hx,hy) in itertools.permutations([(px,py),(qx,qy),(rx,ry),(sx,sy)]):
            #         res = abs(ex - ax) + abs(fx - bx) + abs(gx - cx) + abs(hx - dx) + abs(ey - ay) + abs(fy - by) + abs(gy - cy) + abs(hy - dy)
            #     return -res

            res2 = findPeakUtil(func, 0, n - 1, n) 
            minres = max(minres, res2)

            log(func(0))

    return int(-minres)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# for case_num in [1]:  # no loop over test case
for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    ax,ay = list(map(int,input().split()))
    bx,by = list(map(int,input().split()))
    cx,cy = list(map(int,input().split()))
    dx,dy = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(ax,ay,bx,by,cx,cy,dx,dy)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list