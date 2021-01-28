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


def solve_(mrr):
    # start_time = time.time()

    # your solution here
    # just backtrack

    # angles = [[0 for _ in mrr] for _ in mrr]

    # for i,(x1,y1) in enumerate(mrr):
    #     for j,(x2,y2) in enumerate(mrr):
    #         angles[i][j] = math.atan2(y2-y1,x2-x1)
    half_pi = math.pi/2 - 10**-15
    # log(half_pi)

    def nice(x,y,z):
        # log("mrr", mrr)
        p,q,r = mrr[x], mrr[y], mrr[z]
        
        c2 = (p[0]-r[0])**2 + (p[1]-r[1])**2
        b2 = (q[0]-p[0])**2 + (q[1]-p[1])**2
        a2 = (q[0]-r[0])**2 + (q[1]-r[1])**2
        # log(a2,b2,c2,2*(a2**0.5)*(b2**0.5))
        # log((c2 - a2 - b2) / 2*(a2**0.5)*(b2**0.5))
        # log("calc")
        try:
            angle = math.acos((a2 + b2 - c2) / (2*(a2**0.5)*(b2**0.5)))
            # log(x,y,z,angle)
            if angle < half_pi:
                return True
            return False
        except:
            return False

    # log(nice(3,0,1))

    def attempt():
        unvisited = set(range(len(mrr)))
        prev = random.choice(list(unvisited))
        unvisited.remove(prev)
        cur = random.choice(list(unvisited))
        unvisited.remove(cur)

        sequence = [prev, cur]
        while unvisited:
            for nex in unvisited:
                if nice(prev, cur, nex):
                    sequence.append(nex)
                    unvisited.remove(nex)
                    prev, cur = cur, nex
                    break
            else:
                # back = sequence.pop()
                # if len(sequence) < 2:
                return []
                # unvisited.add(back)
                # prev, cur = sequence[-2], sequence[-1]
            # log(sequence, unvisited)
        return sequence

    while True:
        # log("attempting")
        res = attempt()
        if res:
            return res
            
    return [-1]



for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr)  # include input here

    if res == [-1]:
        print(-1)
    else:
        res = [1+x for x in res]
        print(*res)
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)