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
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}


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


def solve_(arr, mrr, n):
    # your solution here

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    g = defaultdict(set)
    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)
        if arr[a] == arr[b]:
            dp[a][b] = 2
            dp[b][a] = 2
        else:
            dp[a][b] = 1
            dp[b][a] = 1


    # if s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
    # else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # [left unsued, left sused], [right unsued, right used]

    stack = [0]
    visited = set(stack)
    parent = [-1 for _ in range(n)]

    while stack:
        # where should we expand the graph next
        cur = stack.pop()
        log(cur, stack)
        right_nodes = []
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
            right_nodes.append(nex)

        for right in right_nodes:
            right_prev = cur
            left_parent = {}
            left_parent[right] = -1
            left_stack = [right]
            left_visited = set(left_stack)
            while left_stack:
                left = left_stack.pop()
                left_prev = left_parent[left]
                if arr[left] == arr[right] and left != right and left_prev != -1 and left_prev != left and left not in g[right]:
                    dp[left][right] = max(dp[left][right], 2 + dp[left_prev][right_prev])
                    dp[right][left] = dp[left][right]
                elif left != right and left_prev != -1 and left_prev != left and left not in g[right]:
                    dp[left][right] = max(dp[left][right], dp[left_prev][right], dp[left][right_prev])
                    dp[right][left] = dp[left][right]
                for left_nex in g[left]:
                    if left_nex in left_visited:
                        continue
                    if left_nex not in visited:
                        continue
                    left_visited.add(left_nex)
                    left_stack.append(left_nex)
                    left_parent[left_nex] = left

    # for row in dp:
    #     log(row)

    return max(max(row) for row in dp)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    srr = input().strip()
    arr = [abc_map[x] for x in srr]

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(arr, mrr, n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
