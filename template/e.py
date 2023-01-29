#!/usr/bin/env python3
import sys
input = sys.stdin.readline  # to read input quickly
from collections import deque

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


def solve_(n,k,x):
    # your solution here

    xor = 0
    xand = 0
    for i in range(1,n+1):
        xor = xor^i
        xand = xor|i

    if k%2 and xor != x:
        return []

    if k%2 == 0 and xor != 0:
        return []
    
    if xand < x:
        return []


    target = x
    del x

    taken = set()

    res = []
    prevs = deque([])

    for x in range(n,0,-1):
        if len(res) == k:
            break

        if x in taken:
            continue

        log(x, res, prevs)

        y = x^target
        if (not (y in taken)) and (not (y > n)) and (not (x == y)):        
            taken.add(x)
            taken.add(y)
            if y == 0:
                res.append([x])
            else:
                res.append([x,y])
            continue
        
        if not prevs:
            prevs.append(x)
            continue

        z = prevs.popleft()
        y = x^z^target
        if (not (y in taken)) and (not (y > n)) and (not (x == y)):        
            taken.add(x)
            taken.add(y)
            taken.add(z)
            res.append([x,y,z])
            continue

        prevs.append(x)
        prevs.append(z)

    if len(res) < k:
        res.append([])

    for x in range(n,0,-1):
        if x not in taken:
            res[-1].append(x)

    # log(res)

    if len(res) < k or res[-1] == []:
        return []

    assert len(res) == k
    check = set()
    for arr in res:
        xor = 0
        assert len(arr) >= 1
        for x in arr:
            assert 1 <= x <= n
            assert x not in check
            check.add(x)
            xor = xor^x
        assert xor == target

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k,x = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,k,x)  # include input here

    if res == []:
        print(no)
        continue
    
    print(yes)

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    res = "\n".join(str(len(row)) + " " + " ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
