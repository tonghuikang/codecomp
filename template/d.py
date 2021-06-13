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


def query(pos):
    print("? {}".format(pos+1), flush=True)
    response = lst = list(map(int,input().split()))
    return response

def alert(g):
    result_string = []
    stack = [0]
    visited = set(stack)
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
            result_string.append("{} {}".format(cur+1, nex+1))
        # log(result_string)
    print("!\n{}".format("\n".join(result_string)), flush=True)
    # print("!\n{}".format("\n".join(result_string)))
    sys.exit()

k = int(input())

# parent = {}
# results = {}

if k == 2:
    g = defaultdict(set)
    g[0] = [1]
    g[1] = [0]
    alert(g)

stack = [(k-1)//2]
visited = set(stack)
computed = set()
g = defaultdict(set)
# g2 = defaultdict(set)
# three elements that are two away from each other definitely share a common node
cnt = 0

while stack:
    # log(stack)
    # log(computed)
    # log(visited)
    cur = stack.pop()
    if cur in computed:  # do not compute even if in stack
        continue
    computed.add(cur)

    cnt += 1
    if cnt > (k+1)//2:
        assert False
    lst = query(cur)
    # results[cur] = lst

    holding2 = []
    holding3 = []
    c1 = 0
    x1 = -1

    for nex,x in enumerate(lst):
        if x == 0:
            assert nex == cur

        if x == 2 and nex not in visited:
            stack.append(nex)
            visited.add(nex)
            holding2.append(nex)
            # g2[nex].add(cur)
            # g2[cur].add(nex)
                
        if x == 1:
            g[cur].add(nex)
            g[nex].add(cur)
            # parent[nex] = cur
            visited.add(nex)
            computed.add(nex)
            c1 += 1
            x1 = nex

        if x == 3 and nex not in visited:
            holding3.append(nex)
    
    # if there is only one c1, connect all c2 to c1
    if c1 == 1:
        for val in holding2:
            g[val].add(x1)
            g[x1].add(val)
            computed.add(val)
        stack.extend(holding3)

alert(g)



        

# lst = query(0)



# def solve_():
#     # your solution here
#     # find the neighbour
#     # guess two away
#     return ""


# # for case_num in [0]:  # no loop over test case
# # for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

#     # read line as an integer
#     # k = int(input())

#     # read line as a string
#     # srr = input().strip()

#     # read one line and parse each word as a string
#     # lst = input().split()
    
#     # read one line and parse each word as an integer
#     # a,b,c = list(map(int,input().split()))
#     # lst = list(map(int,input().split()))
#     # lst = minus_one(lst)

#     # read multiple rows
#     # arr = read_strings(k)  # and return as a list of str
#     # mrr = read_matrix(k)  # and return as a list of list of int
#     # mrr = minus_one_matrix(mrr)

#     res = solve()  # include input here

#     # print length if applicable
#     # print(len(res))

#     # parse result
#     # res = " ".join(str(x) for x in res)
#     # res = "\n".join(str(x) for x in res)
#     # res = "\n".join(" ".join(str(x) for x in row) for row in res)

#     # print result
#     # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

#     print(res)