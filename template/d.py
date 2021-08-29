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


def solve_(mrr):
    # your solution here

    mrr = [row[::-1] for row in mrr]
    indexes = {}
    last = [row[-1] for row in mrr]

    c = defaultdict(list)
    for i,x in enumerate(last):
        c[x].append(i)
        indexes[x] = i

    stack = [q for q in c.values() if len(q) == 2]

    while stack:
        i,j = stack.pop()
        # log(i,j)

        mrr[i].pop()
        if mrr[i]:
            if mrr[i][-1] in indexes:
                stack.append((i, indexes[mrr[i][-1]]))

        mrr[j].pop()
        if mrr[j]:
            if mrr[j][-1] in indexes:
                stack.append((j, indexes[mrr[j][-1]]))

        if mrr[j] and mrr[i] and mrr[i][-1] == mrr[j][-1]:
            stack.append((i,j))

        if mrr[i]:
            indexes[mrr[i][-1]] = i

        if mrr[j]:
            indexes[mrr[j][-1]] = j

    for row in mrr:
        if row:
            return "No"
    return "Yes"


    # c = Counter(last)

    # pool = set()
    # for k,v in c.items():
    #     if v == 2:
    #         pool.add(k)






    # for i,row in enumerate(mrr[1:], start=1):
    #     while row:

    #         if row[-1] in indexes:
    #             idx = indexes[row[-1]]
    #             mrr[idx].pop()
    #             row.pop()

    #             if mrr[idx]:
    #                 indexes[mrr[idx][-1]] = idx

    #         else:
    #             break

    #     if row:
    #         indexes[row[-1]] = i

    # for row in mrr:
    #     if row:
    #         return



    return ""


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k*2)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    mrr = mrr[1::2]

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