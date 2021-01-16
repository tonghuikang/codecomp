#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
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

# ---------------------------- template ends here ----------------------------


def ncr(n, r):
    if r == 0:
        return 1
    return n * ncr(n-1, r-1) // r

def solve_(k):
    if k == 1:
        return ["AB"]

    if k > 4:
        raise Exception

    break_arr = [0, 1, 3, 35, ncr(2**4, 2**3)//2, 10**10, 10**10, 10**10, 10**10]

    # your solution here
    length = 2**k
    res = []
    
    # print(math.gcd(6006,6864))
    counter = 0

    for comb in itertools.combinations(range(length), length//2):
        arr = ["A"]*length
        for c in comb:
            arr[c] = "B"
        arr = "".join(arr)
        res.append(arr)
        counter += 1
        if counter == break_arr[k]:
            break
    
    # res = ["AAAABBBB","AABBBBAA","ABBAABBA","AABBAABB","ABABABAB","AABAABBB"]

    for i in range(length):
        for j in range(i+1, length):
            same = 0
            diff = 0
            for arr in res:
                if arr[i] == arr[j]:
                    same += 1
                else:
                    diff += 1
            log(i, j, same, diff)

    # log(math.gcd(3003,3432))
    # log(ncr(2**4, 2**3)//2)
    return res
    # return []


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(k)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(len(res))
    print("\n".join(res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)