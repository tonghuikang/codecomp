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


def solve_(k):
    # your solution here
    d4 = [(0,1), (1,0), (0,-1), (-1,0)]
    stack = set([(0,1,0), (1,0,1), (0,-1,2), (-1,0,3)])

    save = []

    for i in range(k):
        new_stack = set()
        for x,y,d in stack:
            for dd in [-1,1]:
                new_d = (d+dd) % 4
                dx,dy = d4[new_d]
                new_stack.add((x+dx, y+dy, new_d))
        stack = new_stack

        save_res = len(set((x,y) for x,y,d in stack))
        log(i, save_res)
        save.append(save_res)

    log(save)

    res = set((x,y) for x,y,d in stack)
    return len(res)


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
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list