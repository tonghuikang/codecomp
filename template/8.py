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
    brr = []
    for ar in arr:
        a, c = ar.split()
        c = int(c)
        brr.append((a,c))
        
    visited = set()
    cur = 0
    cnt = 0
    while True:
        a, c = brr[cur]
        if a == "acc":
            cnt += c
            cur = cur+1
        elif a == "nop":
            cur = cur+1
        elif a == "jmp":
            cur = cur + c
        if cur in visited:
            return -1
        visited.add(cur)
        log(cur,cnt)
        if cur == 636:
            return cnt


def solve_1(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_1_(*args)


overall_res = 0

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

entries = []

while True:
# for case_num in [1]:  # no loop over test case
# for case_num in range(1):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)
    
    strr = input().strip()
    if strr == "EXIT":
        break
    # if strr == "":
    entries.append(strr)

    # overall_res += solve_1()

for i in range(len(entries)):
    entries_copy = [x for x in entries]
    if entries_copy[i][:3] == "acc":
        continue
        
    elif entries_copy[i][:3] == "nop":
        entries_copy[i] = "jmp" + entries_copy[i][3:]
        res = solve_1(entries_copy)
        overall_res = max(overall_res, res)

    elif entries_copy[i][:3] == "jmp":
        entries_copy[i] = "nop" + entries_copy[i][3:]
        res = solve_1(entries_copy)
        overall_res = max(overall_res, res)

print(overall_res)
