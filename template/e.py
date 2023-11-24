#!/usr/bin/env python3
import sys

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

from collections import defaultdict

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


def solve_(n, arr, mrr):
    # your solution here

    # prune nodes with only neighbors

    g = defaultdict(set)

    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)

    for i in range(n):
        if len(g[i]) == 1:
            break
    
    start = i

    stack = [start]
    visited = set(stack)

    g3 = {}

    while stack:
        cur = stack.pop()
        s2 = list(g[cur])
        r2 = []   # for records
        while s2:
            nex = s2.pop()
            
            if nex in visited:  # i.e. the parent
                continue

            visited.add(nex)
            
            if len(g[nex]) == 2:
                a,b = list(g[nex])
                if a == cur:
                    n2 = b
                else:
                    n2 = a
                s2.append(n2)
                continue
            
            r2.append(nex)
            stack.append(nex)

        g3[cur] = r2

    log("g3", g3)

    g4 = defaultdict(list)
    for i,row in g3.items():
        for j in row:
            g4[i].append(j)
            g4[j].append(i)
    g3 = g4

    log("g3 =", g3)

    if len(g3) == 2:
        arr = [x for i,x in enumerate(arr) if i in g3]
        return max(0, sum(arr))

    g = g3

    for i in range(n):
        if i in g and len(g[i]) > 2:
            break
    else:
        assert False

    ROOT = i

    log("ROOT", ROOT)

    stack = [ROOT]
    while stack:
        cur = stack.pop()

    vals = [x for x in arr]

    log(vals)

    RESULT = [0]

    def entry_operation(prev, cur, nex):
        # note that prev is `null_pointer` at the root node
        pass

    def exit_operation(prev, cur):
        # root node
        # choose itself and more than two children
        # choose exactly two children
        # choose one child
        # option to remove all will be considered the option for zero
        if cur == ROOT:
            maxval = 0
            brr = [vals[nex] for nex in g[cur]]
            brr.sort(reverse=True)

            log(cur, brr)

            # choose one child
            maxval = max(
                maxval,
                brr[0],  # choose one child
                brr[0] + brr[1],  # choose exactly two children
            )

            val = brr[0] + brr[1] + arr[cur]
            for x in brr[2:]:
                val += x
                maxval = max(maxval, val)

            RESULT[0] = maxval
            return

        if len(g[cur]) == 1:
            return
            
        # non-leaf node
        # retain itself and at least two children
        # retain only one child
        # option to remove all is done at parent (might be needed to allow other options)

        brr = [vals[nex] for nex in g[cur] if nex != cur]
        brr.sort(reverse=True)

        log(cur, brr)

        maxval = brr[0]
        val = brr[0] + arr[cur]

        for x in brr[1:]:
            val += x
            maxval = max(maxval, val)

        vals[cur] = maxval


    dfs(ROOT, g, entry_operation, exit_operation)
    
    log(vals)

    # NOTE: check small edge cases - null graph, single node graph

    return RESULT[0]


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
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(n-1)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    res = solve(n, arr, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
