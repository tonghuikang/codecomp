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

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


if True:
    def dfs(start, g, entry_operation, exit_operation):
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

    def entry_operation(prev, cur, nex):
        pass

    def exit_operation(prev, cur):
        pass


def solve_(mrr, k):
    # your solution here

    # make depth sum 1 and -1
    # root from leaf
    null_pointer = "NULL"

    g = defaultdict(list)

    for a,b in mrr:
        g[a].append(b)
        g[b].append(a)

    for i in range(k):
        if len(g[i]) == 1:
            break
    root = i
    log(root)

    depth = [0 for _ in range(k)]

    def entry_operation(prev, cur, nex):
        depth[nex] = depth[cur] + 1

    def exit_operation(prev, cur):
        pass
 
    dfs(root, g, entry_operation, exit_operation)    

    ##########################################

    target_val = [1 if d%2 else -1 for d in depth]
    return_val = [0 for _ in range(k)]
    subtree_val = [0 for _ in range(k)]

    def entry_operation(prev, cur, nex):
        depth[nex] = depth[cur] + 1

    def exit_operation(prev, cur):
        return_val[cur] = target_val[cur] - subtree_val[cur]
        if prev != null_pointer:
            subtree_val[prev] += target_val[cur]
 
    dfs(root, g, entry_operation, exit_operation)

    # expected_root_value = 0
    # total = sum(return_val) - return_val[root]
    # log(total)

    return_val[root] = -1

    return return_val


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(mrr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
