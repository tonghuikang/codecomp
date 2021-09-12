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

# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
    # usage - please remember to YIELD to call and return
    '''
    @bootstrap
    def recurse(n):
        if n <= 0:
            yield 0
        yield (yield recurse(n-1)) + 2

    res = recurse(10**5)
    '''
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    if stack:
                        stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc



def solve_(mrr):
    # your solution here

    g = defaultdict(set)
    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)


    buds = set()
    non_buds = set()
    num_children_not_a_bud = 0
    visited = set()

    # + number of children that is not a bud
    # - number of buds
    # + 1


    @bootstrap
    def is_bud(cur):
        visited.add(cur)
        # log(cur)
        children_is_bud = []
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            child_is_bud = is_bud(nex)
            children_is_bud.append(child_is_bud)

        if not children_is_bud or all(child_is_bud for child_is_bud in children_is_bud):
            non_buds.add(cur)
            return False

        nonlocal num_children_not_a_bud
        num_children_not_a_bud += len(children_is_bud) - sum(children_is_bud)
        buds.add(cur)
        return True

    is_bud(1)

    # log(num_children_not_a_bud)
    # log(buds)
    # log(non_buds)

    return num_children_not_a_bud - len(buds) + 1


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k-1)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
