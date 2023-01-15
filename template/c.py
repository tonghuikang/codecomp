#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

abc = "abcdefghijklmnopqrstuvwxyz"
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


def solve_(n, srr):
    # your solution here

    cntr = Counter(srr)
    vals = sorted(list(cntr.values()))[::-1] + [0]*(26-len(cntr))
    # log(cntr)
    # log(vals)

    minval = 0
    mincnt = 2*n+1
    for x in range(1,27):
        if n%x:
            continue
        target = [n//x]*x + [0]*(26-x)
        cnt = 0
        for a,b in zip(vals, target):
            cnt += abs(a-b)

        # log(vals)
        # log(target)
        # log(cnt)

        # log(cnt)
        if cnt < mincnt:
            mincnt = cnt
            minval = x

    x = minval
    log(minval, mincnt)
    assert mincnt%2 == 0
    print(mincnt // 2)
    # log(minval)

    vals = sorted(cntr.items(), key=lambda x:x[1], reverse=True)
    target = [(k,n//minval) for k,v in vals[:minval]]
    for a in abc:
        if (a,n//minval) not in target:
            vals.append((a,0))
    for a in abc:
        if (a,n//minval) not in target:
            if len(target) < minval:
                target.append((a,n//minval))
            else:
                target.append((a,0))
    
    c2 = Counter()
    for k,v in target:
        c2[k] = v

    # log(c2)
    assert sum(c2.values()) == n

    res = []
    for c in srr:
        if cntr[c] > c2[c]:
            for a in abc:
                if cntr[a] < c2[a]:
                    res.append(a)
                    cntr[c] -= 1
                    cntr[a] += 1
                    break
        else:
            res.append(c)

    # log(res)
    assert len(res) == len(srr)
    assert sum(a != b for a,b in zip(res, srr)) == mincnt // 2

    return "".join(res)


while OFFLINE_TEST and False:
    n = random.randint(1,100)
    srr = "".join([random.choice(abc) for x in range(n)])
    solve(n, srr)


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n, srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
