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


def solve_(commands):
    # your solution here
    
    commands = sorted(commands)

    cur = 0
    booked = 0
    visited = [(-10**10,0),(-10**10,0)]

    for t,x in commands:
        if t < booked:
            continue
        else:
            visited.append((t,cur))
            dist = abs(x-cur)
            visited.append((t+dist,x))
            booked = t+dist
            cur = x
    
    visited.append((2*10**10, visited[-1][1]))

    ignored = commands
    ignored.append((10**10, ignored[-1][0]))

    # log(visited)
    
    def interpolate(x1,x2,y1,y2,x):
        return y1 + (x-x1)*(y2-y1)/(x2-x1)

    ptr = 0
    successful = 0
    for (t1,x),(t2,_) in zip(ignored, ignored[1:]):
        while visited[ptr+1][0] < t1:
            ptr += 1

        (x1,y1),(x2,y2) = visited[ptr], visited[ptr+1]
        loc = interpolate(x1,x2,y1,y2,t1)

        posmax = loc
        posmin = loc

        while visited[ptr+1][0] < t2:
            posmax = max(posmax,visited[ptr+1][1])
            posmin = min(posmin,visited[ptr+1][1])
            ptr += 1

        (x1,y1),(x2,y2) = visited[ptr], visited[ptr+1]
        loc = interpolate(x1,x2,y1,y2,t2)

        posmax = max(posmax,loc)
        posmin = min(posmin,loc)

        if posmin <= x <= posmax:
            successful += 1

    return successful


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
    k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(mrr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list