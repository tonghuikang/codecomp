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


def solve_(arr,brr,crr):
    # your solution here

    blocks = []
    ar = [arr[0]]
    br = []
    cr = []

    for a,b,c in zip(arr[1:],brr[1:],crr[1:]):
        if b == c:
            blocks.append((ar,br,cr))
            ar = [a]
            br = []
            cr = []
        else:
            ar.append(a)
            br.append(b)
            cr.append(c)
    else:
        blocks.append((ar,br,cr))

    # log(blocks)

#  [([3, 4], [1], [2]), ([3, 3], [2], [3])]

    lsts = []
    addns = []
    for block in blocks:
        ar, br, cr = block
        ends = [ar[-1]-1]
        addn = [0]
        for a,b,c in zip(ar[::-1][1:], br[::-1], cr[::-1]):
            ends.append(abs(b-c))
            x,y = sorted([b,c])
            # log(x,y,a)
            addn.append(x-1 + a-y)
        ends.append(0)
        addn.append(0)

        addns.append(addn)
        lsts.append(ends)
    
    lsts[0].pop()
    addns[0].pop()

    # log(lsts)
    # log(addns)

    maxres = 0
    for lst,addn in zip(lsts,addns):
        curres = 0
        best_start = 0
        best_pos = 0
        for i,(x,y) in enumerate(zip(lst,addn), start=0):
            if x > best_start + (i-best_pos)*2:
                best_start = x
                best_pos = i
            else:
                best_start += y
            curres = max(curres, (i-best_pos)*2 + best_start + x)
        # log(curres)
        maxres = max(maxres, curres)
 
    # log(lsts)

    return maxres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    crr = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr, brr, crr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)