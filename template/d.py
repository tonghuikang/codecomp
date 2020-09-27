import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(n,m,arr):  # fix inputs here
    console("----- solving ------")
    console(n,m,arr)

    desired = [0 for _ in range(10)]
    for a in arr:
        desired[a] += 1
    desired = tuple(desired)

    counts = defaultdict(int)
    start = [0 for _ in range(10)]
    start[0] = n*2
    start = tuple(start)

    stack = [start]
    counts[start] = 1
    visited = set()

    console(start, desired)

    z = 0

    while stack:
        cur = stack[0]
        del stack[0]

        if cur in visited:
            continue
        if cur[0] == 0:
            continue
        
        visited.add(cur)

        new = list(cur)
        for i,a in enumerate(cur):
            if i+1 >= 10:
                continue
            if a == 0:
                continue
            new[0] -= 1
            new[i] -= 1
            new[i+1] += 1
            counts[tuple(new)] += (counts[cur])*a
            stack.append(tuple(new))
            new[i+1] -= 1
            new[i] += 1
            new[0] += 1
        console(counts)

        z += 1
        if z == 10:
            break
    
    return counts[desired]


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,m,nrows = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split()))[0])

    res = solve(n,m,grid)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
