#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


def solve_(lst, k):
    if lst == sorted(lst):
        return []

    # your solution here
    lst = [x-1 for x in lst]
    locs = {i:x for i,x in enumerate(lst)}
    log(locs)

    required = set([0, k-1])
    cureven = True
    res = []
    settled = set([-1, k])

    while required:
        log(lst, res)

        for val in required:

            if locs[val] == val:
                required.remove(val)
                settled.add(val)
                if val-1 not in settled:
                    required.add(val)
                if val+1 not in settled:
                    required.add(val)
                break

            if cureven:
                if locs[val] > val:  # move left
                    pos = locs[val]-1
                    if pos%2 == 0:  # needs to be even to move
                        log("move left, even", pos, val)
                        for i in range(pos+1, val, -1):
                            lst[i], lst[i-1] = lst[i-1], lst[i]
                            cureven = not cureven
                            res.append(i)
                        
                        required.remove(val)
                        settled.add(val)
                        locs = {i:x for i,x in enumerate(lst)}
                        if val-1 not in settled:
                            required.add(val)
                        if val+1 not in settled:
                            required.add(val)
                        break
                    else:
                        pass
                
                else:  # move right
                    pos = locs[val]
                    if pos%2 == 0:  # needs to be even to move
                        # move
                        for i in range(pos, val):
                            lst[i], lst[i+1] = lst[i+1], lst[i]
                            cureven = not cureven
                            res.append(i)

                        locs = {i:x for i,x in enumerate(lst)}
                        required.remove(val)
                        settled.add(val)
                        if val-1 not in settled:
                            required.add(val)
                        if val+1 not in settled:
                            required.add(val)
                        break
                    
                    else:
                        pass
        
                        

        else:
            break

    return res


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
    lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(lst, k)  # include input here

    # print length if applicable
    print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)