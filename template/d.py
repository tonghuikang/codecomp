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


def solve_(arr):
    if set(arr) == len(arr):
        log("no change")
        return arr
    # your solution here
    res = [-2 for x in arr]

    got_sender = set()

    for i,x in enumerate(arr):
        if x in got_sender:
            continue
        res[i] = x
        got_sender.add(x)

    log(res)

    no_sender = set(i for i,_ in enumerate(arr) if i not in got_sender)
    no_sender = list(no_sender)

    for i,x in enumerate(res):
        if x == -2:
            y = no_sender[-1]
            if i != y:
                res[i] = no_sender.pop()
                continue
            if len(no_sender) > 1:
                tmp = no_sender.pop()
                res[i] = no_sender.pop()
                no_sender.append(tmp)

    if not no_sender:
        log("all assigned")
        return res

    to_be_assigned = []
    for i,x in enumerate(res):
        if x == -2:
            to_be_assigned.append(i)

    assert len(to_be_assigned) == len(no_sender)

    no_sender.sort()
    if len(no_sender) > 1:
        while True:
            random.shuffle(to_be_assigned)
            log(to_be_assigned)
            log(no_sender)
            for i,j in zip(to_be_assigned, no_sender):
                if i == j:
                    break
                res[i] = j
            else:
                break
        return res

    no_sender = no_sender[0]
    to_be_assigned = to_be_assigned[0]
    log(no_sender)
    log(to_be_assigned)
    intended = arr[to_be_assigned]

    for i,x in enumerate(res):
        if x == intended:
            res[i] = to_be_assigned
            res[to_be_assigned] = intended
            break
    else:
        assert False

    return res

for i in range(100000):
    break
    length = random.randint(2,5)
    arr = [random.randint(0,length-1) for _ in range(length)]
    for i,x in enumerate(arr):
        if i == x:
            break
    else:
        # arr = [1,0,1]
        maxcnt = len(set(arr))
        res = solve(arr)
        cnt = sum(i==x for i,x in zip(res, arr))
        log("test")
        log(arr)
        log(res)
        log(maxcnt, cnt)
        assert -2 not in set(res)
        assert len(set(res)) == len(res)
        assert maxcnt == cnt
        log()

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
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)
    arr = [x-1 for x in arr]

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here
    cnt = sum(i==x for i,x in zip(res, arr))
    print(cnt)
    log(res)
    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x+1) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)