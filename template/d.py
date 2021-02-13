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


def solve_(mrr,h,w):
    # your solution here

    stack = [(0,0), (h-1,0), (0,w-1), (h-1,w-1)]
    grounds = set(stack)
    # grounds_considered = set()

    grounds_by_row = defaultdict(set)
    grounds_by_col = defaultdict(set)

    efficient_axis_to_consider = [(0,True),(h-1,True),(0,False),(w-1,False)]  # loc, is_row
    efficient_axis_considered = set()
    for loc,is_row in efficient_axis_to_consider:
        efficient_axis_considered.add((loc,is_row))

    for i,row in enumerate(mrr):
        for j,cell in enumerate(row):
            if cell != ".":
                grounds.add((i,j))
                grounds_by_row[i].add((i,j))
                grounds_by_col[j].add((i,j))

    allres = 0
    while True:
        while efficient_axis_to_consider:
            loc,is_row = efficient_axis_to_consider.pop()
            if is_row:
                for row,col in grounds_by_row[loc]:
                    if (row,True) not in efficient_axis_considered:
                        efficient_axis_to_consider.append((row,True))
                        efficient_axis_considered.add((row,True))
                    if (col,False) not in efficient_axis_considered:
                        efficient_axis_to_consider.append((col,False))
                        efficient_axis_considered.add((col,False))
                    grounds_by_col[col].remove((row,col))
                    if len(grounds_by_col[col]) == 0:
                        del grounds_by_col[col]
                del grounds_by_row[loc]
            else:
                for row,col in grounds_by_col[loc]:
                    if (row,True) not in efficient_axis_considered:
                        efficient_axis_to_consider.append((row,True))
                        efficient_axis_considered.add((row,True))
                    if (col,False) not in efficient_axis_considered:
                        efficient_axis_to_consider.append((col,False))
                        efficient_axis_considered.add((col,False))
                    grounds_by_row[row].remove((row,col))
                    if len(grounds_by_row[row]) == 0:
                        del grounds_by_row[row]
                del grounds_by_col[loc]

        maxlen = 0
        nexres = None,None

        for col,sett in grounds_by_col.items():
            length = len(sett)
            assert length > 0
            if length > maxlen:
                nexres = col, False
                maxlen = length

        for row,sett in grounds_by_row.items():
            length = len(sett)
            assert length > 0
            if length > maxlen:
                nexres = row, True
                maxlen = length

        # log(maxlen, nexres)
        if maxlen == 0:  # manually add
            assert not grounds_by_col
            assert not grounds_by_row
            break
        
        allres += 1
        efficient_axis_to_consider.append(nexres)
        efficient_axis_considered.add(nexres)

    # log(efficient_axis_considered)

    addn_row = 0
    for loc in range(h):
        if (loc,True) not in efficient_axis_considered:
            # log(loc,True)
            addn_row += 1
    
    addn_col = 0
    for loc in range(w):
        if (loc,False) not in efficient_axis_considered:
            # log(loc,False)
            addn_col += 1
    
    log(allres, addn_row, addn_col)

    return allres + min(addn_row, addn_col)


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    h,w = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(h)  # and return as a list of list of int
    mrr = read_strings(h)  # and return as a list of str

    res = solve(mrr,h,w)  # include input here
    
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