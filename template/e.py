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


def longest_increasing_subsequence(nums):
    # leetcode.com/problems/longest-increasing-subsequence/discuss/667975/
    dp = [MAXINT] * (len(nums) + 1)
    for elem in nums:
        dp[bisect.bisect_right(dp, elem)] = elem  # nondecreasing
    # log(dp)
    return dp.index(MAXINT)


# log(longest_increasing_subsequence([1,1,2,3,-100,-200,1]))
# log(longest_increasing_subsequence([1,1,2,3,1]))
# log(longest_increasing_subsequence([1,1,1,1,1]))


def solve_brute_force(arr, n):
    arr = [x-1 for x in arr]

    parents = {i:x for i,x in enumerate(arr, start=1)}

    maxres = 0
    for assignment in itertools.permutations(list(range(n))):
        for removal in itertools.permutations(list(range(n))):
            vals = list(assignment)
            krr = []
            g = defaultdict(set)
            for i,x in enumerate(arr, start=1):
                g[x].add(i)
            # log(assignment, removal)
            for x in removal:
                if g[x]:
                    break
                krr.append(vals[x])
                if x != 0:
                    # log(removal,g,x,parents[x])
                    g[parents[x]].remove(x)
                    vals[parents[x]] = min(vals[parents[x]], vals[x])
            else:
                res = longest_increasing_subsequence(krr)
                if res > maxres:
                    log(arr, krr, res)
                    maxres = max(maxres, res)

    return maxres
        

def solve_(arr, n):
    arr = [x-1 for x in arr]
    # your solution here

    # sum of children's score, or the longest depth
    score = [0 for _ in range(n)]
    depth = [0 for _ in range(n)]
    parents = {i:x for i,x in enumerate(arr, start=1)}

    g = defaultdict(list)
    for i,x in enumerate(arr, start=1):
        g[x].append(i)

    log(g)
    log(parents)

    res = 0
    for cur in range(n-1,-1,-1):
        val = 0
        dep = 1
        for nex in g[cur]:
            val += score[nex]
            dep = max(dep, depth[nex] + 1)
        val = max(val, dep)
        depth[cur] = dep
        score[cur] = val

    # log("depth", depth)

    return score[0]



while OFFLINE_TEST:
    n = random.randint(2,5)
    arr = [random.randint(1,x-1) for x in range(2,n+1)]
    if OFFLINE_TEST:
        p = solve(arr, n)
        log(p)
        q = solve_brute_force(arr, n)
        log(arr, p, q)
        assert p == q



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    n = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr, n)  # include input here
    # if OFFLINE_TEST:
    #     p,q = solve(arr, n), solve_brute_force(arr, n)
    #     log(arr, p, q)
    #     assert p == q

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
