#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------

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
                    if stack:
                        stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc



# minmax

def solve_(mrr, edges):
    # your solution here

    g = defaultdict(list)
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    
    maxres = 0

    # for boo in range(2):
    #     stack = [0]
    #     status = [-1]*len(mrr)
    #     status[0] = boo
    #     curres = 0
    #     while stack:
    #         cur = stack.pop()
    #         # log(cur)
    #         for nex in g[cur]:
    #             # log(nex)
    #             if status[nex] >= 0:
    #                 continue
    #             status[nex] = 1-status[cur]
    #             stack.append(nex)
    #             val = abs(mrr[nex][status[nex]] - mrr[cur][status[cur]])
    #             # log(val)
    #             # log(nex)
    #             curres += val
                
    #     maxres = max(maxres, curres)

    visited = set([0])

    @bootstrap
    def solve(cur):
        resmincur = 0
        resmaxcur = 0
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            resminnex, resmaxnex = solve(nex)
            resmax = max(resminnex + abs(mrr[nex][0] - mrr[cur][1]), resmaxnex + abs(mrr[nex][1] - mrr[cur][1]))
            resmin = max(resmaxnex + abs(mrr[nex][1] - mrr[cur][0]), resminnex + abs(mrr[nex][0] - mrr[cur][0]))
            resmincur += resmin
            resmaxcur += resmax
        return resmincur, resmaxcur

    return max(solve(0))


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    edges = read_matrix(k-1)  # and return as a list of list of int
    edges = minus_one_matrix(edges)

    res = solve(mrr, edges)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)