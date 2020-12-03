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


def solve_1_(arr):
    # your solution here

    cnt = 0

    for i,row in enumerate(arr):
        if arr[i][(3*i)%len(arr[0])] == "#":
            cnt += 1

    return cnt

def solve_2_(lst):

    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    # your solution here

    res = []

    for x in [1,3,5,7]:
        cnt = 0
        for i,row in enumerate(arr):
            if arr[i][(x*i)%len(arr[0])] == "#":
                cnt += 1

        res.append(cnt)

    cnt = 0
    x = 1
    for i,row in enumerate(arr[::2]):
        if row[(x*i)%len(arr[0])] == "#":
            # if i%2 == 1:
            cnt += 1
        

    res.append(cnt)

    log(res)
    return res[0]*res[1]*res[2]*res[3]*res[4]


def solve_1(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_1_(*args)

def solve_2(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_2_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]


overall_res = 0

# for case_num in range(323):  # no loop over test case
for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    arr = read_strings(323)

    # res = solve_1(arr)  # please change
    res = solve_2(arr)  # please change
    
    overall_res += res
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list

print(overall_res)