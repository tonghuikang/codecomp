#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
# import random
from collections import defaultdict
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"

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
    return [[int(x == "#") for x in input().strip()] for _ in range(rows)]

# ---------------------------- template ends here ----------------------------

# recusion template that does not use recursion

def dfs(start, g, entry_operation, exit_operation):
    # https://codeforces.com/contest/1646/submission/148435078
    # https://codeforces.com/contest/1656/submission/150799881
    entered = set([start])
    exiting = set()
    stack = [start]
    prev = {}

    null_pointer = "NULL"
    prev[start] = null_pointer

    while stack:
        cur = stack[-1]

        if cur not in exiting:
            for nex in g[cur]:
                if nex in entered:
                    continue

                entry_operation(prev[cur], cur, nex)

                entered.add(nex)
                stack.append(nex)
                prev[nex] = cur
            exiting.add(cur)

        else:
            stack.pop()
            exit_operation(prev[cur], cur)

# def entry_operation(prev, cur, nex):
#     # note that prev is `null_pointer` at the root node
#     pass

# def exit_operation(prev, cur):
#     pass


d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d4_to_idx = {x:i for i,x in enumerate(d4)}
dir_to_dxdy = {0: (1,0), 2: (0,1), 3: (-1,0), 1: (0,-1)}
# dir_to_dxdy = {"S": (1,0), "E": (0,1), "N": (-1,0), "W": (0,-1)}

# dcode_to_str = ["S", "W", "E", "N", "."]

for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    r,c = list(map(int,input().split()))
    # your solution here
    # if connected you can travel
    # just detour
    mrr = (read_strings(r))  # and return as a list of str

    check = (r*c - sum(sum(row) for row in mrr))*4
    log(check)

    g = defaultdict(list)

    for x in range(r):
        r1 = mrr[x]
        for y in range(c-1):
            if r1[y] == r1[y+1] == 0:
                g[x,y].append((x,y+1))
                g[x,y+1].append((x,y))

    for x in range(r-1):
        r1 = mrr[x]
        r2 = mrr[x+1]
        for y in range(c):
            if r1[y] == r2[y] == 0:
                g[x,y].append((x+1,y))
                g[x+1,y].append((x,y))

    block_direction = []

    def entry_operation(prev, cur, nex):
        block_direction.append((cur, nex))
        block_direction.append((nex, cur))

    # random.shuffle(block_direction)

    def exit_operation(prev, cur):
        pass
    #     if prev != "NULL":
    #         block_direction.append((cur, prev))

    dfs((0,0), g, entry_operation, exit_operation)

    # log(block_direction)

    dcode_to_str = ["S", "W", "E", "N", "."]

    initdir = {
        (0,0): 0, # "S",
        (0,1): 1, # "W",
        (1,0): 2, # "E",
        (1,1): 3, # "N",
    }
    res = [[initdir[i&1, j&1] if mrr[i >> 1][j >> 1] == 0 else 4 for j in range(c*2)] for i in range(r*2)]

    for (ax,ay),(bx,by) in block_direction:

        dx,dy = bx-ax, by-ay
        di = d4_to_idx[dx,dy]

        # d4 = [(1,0),(0,1),(-1,0),(0,-1)]
        # d4_to_idx = {x:i for i,x in enumerate(d4)}

        cake = [
            (1,0,0),  # "S"
            (1,1,2),  # "E"
            (0,1,3),  # "N"
            (0,0,1),  # "W"
        ]

        qx,qy,qd = cake[di]

        res[2*ax+qx][2*ay+qy] = qd

    for row in res:
        log(row)
    log()

    visited = set()

    cx,cy = 0,0
    ret = []
    while True:
        cdir = res[cx][cy]
        ret.append(cdir)
        dx,dy = dir_to_dxdy[res[cx][cy]]
        cx,cy = cx+dx, cy+dy
        
        if (cx,cy) in visited:
            assert False
        visited.add((cx,cy))
        if (cx == 0 and cy == 0):
            break
        # log(cx,cy)

    log(check, len(visited), len(ret))

    if check > len(ret):
        print("Case #{}: {}".format(case_num+1, "IMPOSSIBLE"))   # Google and Facebook - case number required
        continue

    assert len(ret) == check

    # return ret


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # r,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # mrr = read_strings(r)  # and return as a list of str
    # mrr = read_matrix(r)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    # res = solve(mrr, r, c)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, "".join(dcode_to_str[x] for x in ret)))   # Google and Facebook - case number required

    # print(res)
