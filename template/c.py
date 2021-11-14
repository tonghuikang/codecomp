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
class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def solve_(srr):
    # your solution here

    left = LLNode(-1)
    prev = left

    iteration = []
    iteration_map = {}
    a,b,c = 0,1,2
    for _ in range(10):
        a,b,c = a+1,b+1,c+1
        a,b,c = a%10,b%10,c%10
        iteration.append((a,b,c))
        iteration_map[a,b] = c

    iteration_pool = defaultdict(list)
    for c in srr:
        cur = LLNode(int(c))
        cur.prev = prev
        prev.next = cur

        if (prev.val, cur.val) in iteration_map:
            iteration_pool[prev.val, cur.val].append((prev, cur))

        prev = cur

    cur = LLNode(-2)
    prev.next = cur
    cur.prev = prev


    cur = left
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next

    # log(res)


    flag = True
    while flag:
        flag = False

        for a,b,c in iteration:
            for prev, cur in iteration_pool[a,b]:
                # log(prev, cur, type(prev))
                new = LLNode(c)
                prev.prev.next = new
                cur.next.pev = new
                new.prev = prev.prev
                new.next = cur.next
                flag = True

                if (new.prev.val, new.val) in iteration_map:
                    iteration_pool[new.prev.val, new.val].append((new.prev, new))

                if (new.val, new.next.val) in iteration_map:
                    iteration_pool[new.val, new.next.val].append((new, new.next))

                cur = left
                res = []
                while cur:
                    res.append(cur.val)
                    cur = cur.next

                # log(res)

            iteration_pool[a,b] = []

    res = [x for x in res if x >= 0]

    # prevlen = len(srr) + 1
    # while prevlen != len(srr):
    #     prevlen = len(srr)
    #     srr = srr.replace("01", "2")
    #     srr = srr.replace("12", "3")
    #     srr = srr.replace("23", "4")
    #     srr = srr.replace("34", "5")
    #     srr = srr.replace("45", "6")
    #     srr = srr.replace("56", "7")
    #     srr = srr.replace("67", "8")
    #     srr = srr.replace("78", "9")
    #     srr = srr.replace("89", "0")
    #     srr = srr.replace("90", "1")

    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = "".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
