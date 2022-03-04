#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
# import math, random
# import functools, itertools, collections, heapq, bisect
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

def solve_(mrr, total_vertices):
    if total_vertices == 2:
        return 2,2,[1,1]
    # your solution here

    # https://courses.grainger.illinois.edu/cs473/sp2011/lectures/09_lec.pdf
    
    res = [-1 for _ in range(total_vertices)]

    g = defaultdict(set)
    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)
        # log(a, b)

    leaves = set()
    degree = defaultdict(int)
    for x in range(total_vertices):
        degree[x] = len(g[x])
        if len(g[x]) == 1:
            leaves.add(x)
            res[x] = 1

    opt = [-1 for _ in range(total_vertices)]
    opt1_store = [-1 for _ in range(total_vertices)]
    opt2_store = [-1 for _ in range(total_vertices)]

    # @bootstrap
    # def recurse(n):
    #     if n <= 0:
    #         yield 0
    #     yield (yield recurse(n-1)) + 2

    allstart = list(leaves)[0]

    res = [0 for _ in range(total_vertices)]

    @bootstrap
    def recurse(cur, prev=-1):
        children = set()
        grand_children = set()
        for nex in g[cur]:
            if nex == prev:
                continue
            gc = yield recurse(nex, cur)
            grand_children.update(gc)
            children.add(nex)

        opt1 = 1 + sum(opt[x] for x in grand_children)
        opt2 = sum(opt[x] for x in children)

        opt1_store[cur] = opt1
        opt2_store[cur] = opt2
        opt[cur] = max(opt1, opt2)

        # if opt[cur] == opt1:
        #     res[cur] = 1
        # else:
        #     res[cur] = 0

        yield children
        
    recurse(allstart)

    @bootstrap
    def recurse(cur, prev=-1, prev_color=False):
        if opt[cur] == opt1_store[cur] and not prev_color:
            res[cur] = 1
            for nex in g[cur]:
                if nex == prev:
                    continue
                yield recurse(nex, cur, True)

        else:
            res[cur] = 0
            for nex in g[cur]:
                if nex == prev:
                    continue
                yield recurse(nex, cur, False)

        yield

    recurse(allstart)

    # log(opt)
    # log(res)

    assignment = [degree[i] if x == 1 else 1 for i,x in enumerate(res)]
    a = sum(degree[i] == x for i,x in enumerate(assignment))
    b = sum(assignment)

    return a,b,assignment


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

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

    a,b,res = solve(mrr, k)  # include input here
    print(a,b)
    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)

