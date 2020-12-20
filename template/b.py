import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(srr,a,b):
    # your solution here

    # left ones, right zeroes, assumes a > b, otherwise switch
    if a < b:
        srr = srr.replace("1","x").replace("0","1").replace("x","0")
        a,b = b,a
    log(srr, a, b)


    def count(brr):
        right_zeroes = brr.count("0")
        left_zeroes = 0
        cnt = 0
        for s in brr:
            if s == "0":
                right_zeroes -= 1
                left_zeroes += 1
            if s == "1":
                cnt += right_zeroes*b
                cnt += left_zeroes*a
        return cnt

    # all zeroes base count
    crr = srr.replace("?","0")
    cnt = count(crr)
    log(cnt)
    
    # b3
    # log(count("0100"))
    # log(count("1100"))
    # log(count("1101"))

    right_zeroes = crr.count("0")
    left_zeroes = 0
    right_ones = crr.count("1")
    left_ones = 0

    minres = cnt
    # log(cnt - a + 2*b)
    for s in srr:
        # log(left_zeroes, right_zeroes, right_ones, left_ones)
        if s == "?":
            right_zeroes -= 1
            cnt += left_zeroes*a
            cnt += right_zeroes*b
            cnt -= right_ones*a
            cnt -= left_ones*b
            left_ones += 1
            minres = min(minres, cnt)
        if s == "0":
            right_zeroes -= 1
            left_zeroes += 1
        if s == "1":
            right_ones -= 1
            left_ones += 1
        # log(s, cnt)

    # assert cnt == count(srr.replace("?","1"))

    return minres


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

for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    a,b = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(strr,a,b)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list