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
    arr = ["x" + ar + "x" for ar in arr]
    arr = ["x"*len(arr[0])] + arr + ["x"*len(arr[0])]

    for _ in range(1000):
        new_arr = [[x for x in row] for row in arr]
        for i in range(1,len(arr)-1): 
            for j in range(1,len(arr[0])-1):
                if arr[i][j] == ".":
                    continue
                
                diff = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

                cnt = 0
                for dx,dy in diff:
                    for z in range(1,1000):
                        if arr[i+dx*z][j+dy*z] == "x":
                            break
                        if arr[i+dx*z][j+dy*z] == "L":
                            break
                        if arr[i+dx*z][j+dy*z] == "#":
                            cnt += 1
                            break
                # log(lst)
                if cnt >= 5 and arr[i][j] == "#":
                    new_arr[i][j] = "L"
                if cnt == 0 and arr[i][j] == "L":
                    new_arr[i][j] = "#"
        arr = new_arr
        log(sum(ar.count("#") for ar in arr))
    return sum(ar.count("#") for ar in arr)


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

overall_res = solve_1(entries)

print(overall_res)
