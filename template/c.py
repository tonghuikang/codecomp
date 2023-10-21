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


def solve_(n, arr, mrr):
    # your solution here
    arr = [-1] + arr
    children = [set() for _ in range(n)]
    g = [set() for _ in range(n)]
    is_complex = [False for _ in range(n)]

    # leaf_count = [0 for _ in range(n)]
    # vocab_count = [Counter(x) for x in range(n)]

    for i,x in enumerate(arr[1:], start=1):
        g[x].add(i)
        children[x].add(i)

    proc = []
    for i,x in enumerate(g):
        if len(x) == 0:
            proc.append(i)
        if len(x) > 1:
            is_complex[i] = True
    
    while proc:
        cur = proc.pop()

        if len(children[cur]) == 1:
            curset = mrr[cur]
            mrr[cur] = mrr[list(children[cur])[0]]  # might be large
            for x in curset:
                mrr[cur].add(x)
        else:
            complex_set = set()
            for nex in children[cur]:
                if is_complex[nex]:
                    if len(complex_set) == 0:
                        complex_set = mrr[nex]
                    else:
                        complex_set = complex_set & mrr[nex]

            counts = Counter()
            for topic in mrr[cur]:
                counts[topic] += 1

            for nex in children[cur]:
                for topic in mrr[nex]:
                    counts[topic] += 1
            
            newset = set()
            num_children = len(children[cur])
            for topic,v in counts.items():
                if v >= num_children:
                    newset.add(topic)

            if complex_set:
                newset = newset & complex_set
            
            mrr[cur] = newset

        log(cur, complex_set)

        if cur == 0:
            break

        if is_complex[cur] is True:
            is_complex[arr[cur]] = True

        g[arr[cur]].remove(cur)
 
        if len(g[arr[cur]]) == 0:
            proc.append(arr[cur])

    log(is_complex)
    log(mrr)
    
    return len(mrr[0])


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
    arr = minus_one(arr)

    # read multiple rows
    mrr = read_strings(n)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    mrr = [set(row.split()[1:]) for row in mrr]

    res = solve(n, arr, mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
