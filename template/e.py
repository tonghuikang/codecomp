#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

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

# ---------------------------- template ends here ----------------------------


def solve_(mrr, n):
    # your solution here

    d = {k:[] for k in range(n)}
    for a,b,c in mrr:
        d[a-1].append((b-1,c))

    # log(d)

    d2 = []
    for k in range(n):
        v = d[k]
        v = sorted(v)
        visited = set()
        v2 = []
        for b,c in v:
            if b in visited:
                continue
            visited.add(b)
            v2.append((b,c))
        d2.append(v2)
    d = d2

    # log(d)
    LARGE = 10**10

    res = []
    for start in range(n):
        visited = {k:LARGE for k in range(n)}
        cleared = set()
        stack = [(0, start)]
        curres = LARGE
        while stack:
            cur_cost,cur = heapq.heappop(stack)
            if cur in cleared:
                continue
            cleared.add(cur)
            for nex,cost in d[cur]:
                if nex == start:
                    curres = min(curres, cur_cost+cost)
                if nex in cleared:
                    continue
                visited[nex] = min(visited[nex], cur_cost+cost)
                heapq.heappush(stack, (cur_cost+cost, nex))
        res.append(curres if curres < LARGE else -1)
    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr, n)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print("\n".join(str(x) for x in res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)