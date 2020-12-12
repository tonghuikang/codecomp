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


def solve_1_(arr):
    
    # directions = [(1,0), (0,-1), (-1,0), (0,1)]
    curdir = 0

    # ship loc
    x = 0
    y = 0

    # waypoint loc
    a = 10
    b = 1

    for z in arr:
        log(z,x,y,a,b)
        direction, dist = z[0], int(z[1:])

        if direction == "F":
            x = x+a*dist
            y = y+b*dist
            continue

        if direction == "L":
            for _ in range((dist)//90):
                a,b = -b,a
            continue
        if direction == "R":
            for _ in range((dist)//90):
                a,b = b,-a
            continue

        if direction == "N":
            dx,dy = 0,1
        if direction == "S":
            dx,dy = 0,-1
        if direction == "E":
            dx,dy = 1,0
        if direction == "W":
            dx,dy = -1,0

        # log(a,dx,dist)
        a = a+dx*dist
        b = b+dy*dist

    
    # log(x,y)
    return abs(x) + abs(y)


def solve_1(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_1_(*args)


overall_res = 0

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

entries = []

while True:
# for case_num in [1]:  # no loop over test case
# for case_num in range(1):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)
    
    strr = input().strip()
    if strr == "EXIT":
        break
    # if strr == "":
    entries.append(strr)

overall_res = solve_1(entries)

print(overall_res)
