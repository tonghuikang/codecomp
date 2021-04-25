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
M = 60*720*10**9

def take_min(angle):
    return min(M-angle, angle)

def solve_(aa,bb,cc):
    aa,bb,cc = sorted([aa,bb,cc])
    # your solution here
    res_arr = []

    # for z1,z2,z3 in itertools.product([-1,1], repeat=3):
    if True:
        for a,b,c in itertools.permutations([aa,bb,cc]):
            d,e,f = abs(a-b), abs(b-c), abs(a-c)
            d,e,f = take_min(d), take_min(e), take_min(f)
            # d = (d*z1)%M
            # e = (e*z2)%M
            # f = (f*z3)%M
            for p in range(12*60):  # number of seconds elapsed
                # if p == 62:
                #     log(d, p, (d + p*M) % 719)
                if (d + p*M) % 719 != 0 and (d - p*M) % 719 != 0:
                    continue
                x = ((d + p*M)//719)%(12*60*60*10**9)
                diff1 = 720*x - p*M - (12*x - (p//60)*M)
                diff2 = 12*x - (p//60)*M - x
                diff1 = take_min(abs(diff1))
                diff2 = take_min(abs(diff2))
                if sorted([diff1,diff2]) == sorted([e,f]):
                    # log("ok", x)

                    # log("Case #{}: {} {} {} {}".format(case_num, 
                    #     (x//(60*60*10**9)),
                    #     (x//(60*10**9))%60,
                    #     (x//(10**9))%60,
                    #     (x//(1))%(10**9)
                    # ))
                    res_arr.append(x)

    LARGE = 12*60*60*10**9
    new_arr = []
    for x in res_arr:
        new_arr.append(x)
        if x != 0:
            new_arr.append(LARGE-x)
            
    log(new_arr)

    for nsecs in new_arr:
        p,q,r = nsecs, (720//60*nsecs)%(60*720*10**9), (720*nsecs)%(60*720*10**9) 
        p,q,r = sorted([p,q,r])
        if p-aa == q-bb == r-cc:
            return nsecs
    
    return 0


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    x = solve(a,b,c)  # include input here
    
    # print result
    # Google and Facebook - case number required
    print("Case #{}: {} {} {} {}".format(case_num, 
        (x//(60*60*10**9)),
        (x//(60*10**9))%60,
        (x//(10**9))%60,
        (x//(1))%(10**9)
    ))

    # Other platforms - no case number required
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)