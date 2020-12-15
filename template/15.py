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

    return 0


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


sample_input="""
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

sample_input="""
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

sample_input = sample_input.strip()
sample_input = process(sample_input)

sample_res = solve(sample_input)
# print(sample_res)


test_input="""
"""

test_input = test_input.strip()

test_input = process(test_input)
test_res = solve(test_input)
# print(test_res)



