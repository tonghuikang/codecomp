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


def solve_(inp):
    recent = defaultdict(list)
    for i,k in enumerate(inp):
        recent[k].append(i)
    
    last = inp[-1]
    for i in range(len(inp), 30000000):
        if len(recent[last]) == 1:
            recent[0].append(i)
            last = 0
        else:
            diff = recent[last][-1] - recent[last][-2]
            recent[diff].append(i)
            last = diff

    return last


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



def process(string_input):
    arr = string_input.split("\n")

    ins = []
    brr = []
    for a in arr[::-1]:
        if a[:4] == "mask":
            mask = a[-36:]
            brr.append([mask, ins])
            ins = []
        else:
            a = a[3:].replace("[", "").replace("]","").replace(" = "," ")
            ins.append([int(x) for x in a.split()])

    return brr


# sample_input="""
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# """

# sample_input="""
# 0,3,6
# """

inp = [[0,3,5],
[1,3,2],
[2,1,3],
[1,2,3],
[2,3,1],
[3,2,1],
[3,1,2],
[12,20,0,6,1,17,7]]

import time
# sample_input = sample_input.strip()
for inpp in inp[::-1]:
    start_time = time.time()
    sample_res = solve(inpp)
    print(sample_res)
    log(time.time()-start_time)
    break


# test_input="""
# 12,20,0,6,1,17,7
# """

# test_input = test_input.strip()

# test_input = process(test_input)
# test_res = solve(test_input)
# # print(test_res)



