#!/usr/bin/env python3
import sys
from collections import defaultdict
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
# abc = "abcdefghijklmnopqrstuvwxyz"
# abc_map = {c:i for i,c in enumerate(abc)}
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


def sum_product_triplet(arr):
    dp = [x for x in arr]

    for _ in range(2):
        cursum = sum(dp)
        new_dp = [0 for _ in arr]
        for i,x in enumerate(arr):
            cursum -= dp[i]
            new_dp[i] = x*cursum
        dp = new_dp
        # log(dp)
    return sum(dp)


# log(sum_product_triplet([1,1,1,1,1,1,1]))


def solve_(n,mrr):
    # your solution here
    if n <= 2:
        return 0

    g = defaultdict(list)

    for a,b in mrr:
        g[a].append(b)
        g[b].append(a)

    child_count = [1 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    def entry_operation(prev, cur, nex):
        parent[nex] = cur

    def exit_operation(prev, cur):
        if prev == "NULL":
            return
        child_count[prev] += child_count[cur]

    dfs(0, g, entry_operation, exit_operation)

    # log(parent)
    # log(child_count)

    res = 0

    for k,v in g.items():
        arr = []
        for nei in v:
            if nei == parent[k]:
                continue
            arr.append(child_count[nei])
        leftover = n - 1 - sum(arr)
        if leftover:
            arr.append(leftover)

        val = sum_product_triplet(arr)
        res += val

        # log(k, v, arr, val)

    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

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
    mrr = read_matrix(n-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(n,mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
