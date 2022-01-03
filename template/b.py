#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = 10**18 + 10

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

    a,b,c = mrr[0]

    left = a
    right = b
    left_right_cost = c
    left_cost = c
    right_cost = c

    res = [c]

    for i,(a,b,c) in enumerate(mrr[1:], start=1):

        if a <= left and b >= right:
            if c < left_right_cost:
                left_right_cost = c

        elif a < left or b > right:
            left_right_cost = MAXINT

        if a == left:
            left = a
            left_cost = min(left_cost, c)

        elif a < left:
            left = a
            left_cost = c

        if b == right:
            right = b
            right_cost = min(right_cost, c)

        elif b > right:
            right = b
            right_cost = c

        res.append(min(left_right_cost, left_cost + right_cost))



    return res


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    k = int(input())
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
