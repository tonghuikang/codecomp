#!/usr/bin/env python3
import sys
import bisect
import collections
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


# ---------------------------- template ends here ----------------------------

# recusion template that does not use recursion

def dfs(start, g, entry_operation, exit_operation):
    # g is map of node to nodes
    # assumes g is bidirectional
    # https://codeforces.com/contest/1646/submission/148435078
    # https://codeforces.com/contest/1656/submission/150799881
    # https://codeforces.com/contest/1714/submission/166648312
    entered = set([start])
    exiting = set()
    ptr = {x:0 for x in g}
    stack = [start]
    prev = {}

    null_pointer = "NULL"
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

def entry_operation(prev, cur, nex):
    # note that prev is `null_pointer` at the root node
    pass

def exit_operation(prev, cur):
    pass

def encode(a,b):
    return (a << 32) ^ b


def solve_(n):
    # your solution here
    amap = {}
    bmap = {}

    g = defaultdict(list)
    for i in range(n-1):
        p,a,b = list(map(int,input().split()))
        i += 1
        p -= 1
        g[i].append(p)
        g[p].append(i)

        amap[encode(p,i)] = a
        amap[encode(i,p)] = a

        bmap[encode(p,i)] = b
        bmap[encode(i,p)] = b

    # log(g)

    asum = 0
    bsum = 0
    psum = [0]
    res = [0 for _ in range(n)]

    def entry_operation(prev, cur, nex):
        nonlocal asum, bsum
        a = amap[encode(cur, nex)]
        b = bmap[encode(cur, nex)]
        asum += a
        bsum += b
        psum.append(bsum)
        res[nex] = bisect.bisect_right(psum, asum) - 1

    def exit_operation(prev, cur):
        nonlocal asum, bsum
        if prev == "NULL":
            return
        a = amap[encode(cur, prev)]
        b = bmap[encode(cur, prev)]
        asum -= a
        bsum -= b
        psum.pop()

    dfs(0, g, entry_operation, exit_operation)

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

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
    # mrr = read_matrix(n-1)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res[1:])
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
