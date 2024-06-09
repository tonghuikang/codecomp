#!/usr/bin/env python3
import sys
from collections import defaultdict

input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}
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
        print("\033[36m", *args, "\033[0m", file=sys.stderr)


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x - 1 for x in arr]


def minus_one_matrix(mrr):
    return [[x - 1 for x in row] for row in mrr]


# ---------------------------- template ends here ----------------------------


def dfs(start, g, entry_operation, exit_operation):
    # g is map of node to nodes
    # assumes g is bidirectional
    # https://codeforces.com/contest/1714/submission/166648312
    entered = set([start])
    exiting = set()
    ptr = {x: 0 for x in g}
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


def entry_operation(prev, cur, nex):
    # note that prev is `null_pointer` at the root node
    pass


def exit_operation(prev, cur):
    pass


def solve_(n, mrr):
    # root on leaf, connect to whoever with the most connections, repeat

    counts = [0 for _ in range(n)]
    g = defaultdict(set)
    for a,b in mrr:
        counts[a] += 1
        counts[b] += 1
        g[a].add(b)
        g[b].add(a)
    
    for i,x in enumerate(counts):
        if x == 1:
            break
    else:
        raise

    root = i

    # your child has only one child, you rather connect with your grandchild

    stack = [root]
    visited = set(stack)
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            if len(g[nex]) == 2:
                for grandchild in g[nex]:
                    if grandchild != cur:
                        break
                else:
                    raise
                g[cur].remove(nex)
                g[nex].remove(cur)
                g[cur].add(grandchild)
                g[grandchild].add(cur)
                visited.add(grandchild)
                stack.append(grandchild)
            else:
                stack.append(nex)

    counts_new = [0 for _ in range(n)]
    for k in range(n):
        for v in g[k]:
            counts_new[v] += 1

    assert sum(counts_new) == 2 * (n-1)
    log(counts_new)

    return sum(1 for x in counts_new if x == 1)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
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

    res = solve(n, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
