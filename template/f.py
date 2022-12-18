#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    mrr = []
    for _ in range(rows):
        row = [int(x) for x in list(input())]
        mrr.append(row)
    return mrr

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------



def dfs(start, g, entry_operation, exit_operation):
    # g is map of node to nodes
    # assumes g is bidirectional
    # https://codeforces.com/contest/1714/submission/166648312
    entered = set([start])
    exiting = set()
    ptr = {x:0 for x in g}
    stack = [start]
    prev = {}

    null_pointer = "NULL"
    # might be faster to use an integer for null_pointer
    # especially if you avoid string compare when checking if null pointer
    # leaving as a string for safety reasons
    prev[start] = null_pointer

    while stack:
        cur = stack[-1]

        if cur not in exiting:
            while ptr[cur] < len(g[cur]):
                nex = g[cur][ptr[cur]]
                ptr[cur] += 1
                if nex in entered:
                    continue

                entry_operation(prev[cur], cur, nex)

                entered.add(nex)
                stack.append(nex)
                prev[nex] = cur
                break
            if ptr[cur] == len(g[cur]):
                exiting.add(cur)

        else:
            stack.pop()
            exit_operation(prev[cur], cur)



def solve_(n,m,k,mrrs):
    
    # your solution here

    # calculate which graph is adjacent to each other, this forms a graph
    # write a path that visits all the nodes in the grpah

    def is_adjacent(i1,i2):
        arr = mrrs[i1]
        brr = mrrs[i2]

        x,y = -1,-1
        for i,(row1, row2) in enumerate(zip(arr, brr)):
            for j,(cell1, cell2) in enumerate(zip(row1, row2)):
                if cell1 != cell2:
                    if x != -1:
                        return False, -1, -1
                    x,y = i,j

        if x == -1:
            return True, -1, -1

        for dx,dy in d4:
            xx = x+dx
            yy = y+dy
            if arr[xx][yy] != brr[xx][yy]:
                return False, -1, -1

        return True, x, y

    g = {i:[] for i in range(k)}
    mapp = {}

    for i in range(k):
        for j in range(i+1, k):
            # log(i,j)
            boo, x, y = is_adjacent(i,j)
            if boo:
                g[i].append(j)
                g[j].append(i)
                mapp[i,j] = (x,y)
                mapp[j,i] = (x,y)

    log(g)

    res = []

    def entry_operation(prev, cur, nex):
        # note that prev is `null_pointer` at the root node
        res.append((1, 1+mapp[cur, nex][0], 1+mapp[cur, nex][1]))
        res.append((2, nex+1))
        pass

    def exit_operation(prev, cur):
        if prev == "NULL":
            return
        res.append((1, 1+mapp[prev, cur][0], 1+mapp[prev, cur][1]))
        pass

    dfs(0, g, entry_operation, exit_operation)


    res = [[0+1], [len(res)]] + res

    log(res)

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,m,k = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrrs = []
    for _ in range(k+1):
        _ = input().strip()
        arr = read_strings(n)  # and return as a list of list of int
        mrrs.append([[int(x) for x in row] for row in arr])
    # mrr = minus_one_matrix(mrr)

    k += 1
    res = solve(n,m,k,mrrs)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
