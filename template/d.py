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
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(n,p,m,ar,ac,arr,prr):
    # your solution here

    arr = [x.split() for x in arr]

    op_map = {
        "+": lambda x: x[0]+x[1],
        "-": lambda x: x[0]-x[1],
        "*": lambda x: x[0]*x[1],
        "/": lambda x: x[0]//x[1],
    }
    
    arr = [(op_map[x], int(y)) for x,y in arr]

    def ops(dx,dy,val):
        # north
        if (dx,dy) == (-1,0):
            op, y = arr[0]
            return op((val, y))

        # east
        if (dx,dy) == (0,1):
            op, y = arr[1]
            return op((val, y))

        # west
        if (dx,dy) == (0,-1):
            op, y = arr[2]
            return op((val, y))

        # south
        if (dx,dy) == (1,0):
            op, y = arr[3]
            return op((val, y))

        assert False

    
    states = {(ar-1,ac-1): 0}
    for turn in range(m):

        new_states = {k:v for k,v in states.items()}
        for (x,y), val in states.items():
            for dx,dy in d4:
                xx = x+dx
                yy = y+dy
                if 0 <= xx < n and 0 <= yy < n:
                    next_val = ops(dx,dy,val)
                    if (xx,yy) in new_states:
                        new_states[xx,yy] = max(new_states[xx,yy], next_val)
                    else:
                        new_states[xx,yy] = next_val

        log(new_states)
        states = new_states
        
    return max(states.values())



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,p,m,ar,ac = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    arr = read_strings(4)  # and return as a list of str
    prr = read_matrix(p)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,p,m,ar,ac,arr,prr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
