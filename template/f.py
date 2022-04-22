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

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
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


all_cntr = Counter()

for n in range(2, 13):
    log(n)

    for comb in itertools.permutations(list(range(n))):
        if comb[0] == 0 or comb[-1] == n-1:
            continue
        
        p = 0
        for a,b in zip(comb[1:], comb):
            if b > a:
                p += 1

        q = 0
        for a in range(n):
            for b in range(a+1,n):
                if comb[a] > comb[b]:
                    q += 1

        if p <= 11 and q <= 11:
            all_cntr[n,p,q] += 1

log(all_cntr)
    
all_cntr = {(11, 4, 11): 13672, (11, 5, 11): 8886, (11, 4, 10): 7722, (10, 4, 11): 6433, (11, 3, 11): 5712, (11, 5, 10): 4390, (11, 4, 9): 4087, (10, 4, 10): 3834, (10, 3, 11): 3690, (11, 3, 10): 3596, (10, 5, 11): 2778, (9, 4, 11): 2424, (10, 3, 10): 2393, (11, 3, 9): 2088, (10, 4, 9): 2087, (9, 3, 11): 2064, (11, 4, 8): 1944, (11, 5, 9): 1920, (9, 4, 10): 1554, (10, 3, 9): 1503, (10, 5, 10): 1429, (9, 3, 10): 1414, (11, 6, 11): 1359, (11, 3, 8): 1162, (10, 4, 8): 1060, (9, 3, 9): 918, (9, 4, 9): 905, (8, 3, 11): 893, (10, 3, 8): 841, (11, 4, 7): 818, (11, 5, 8): 730, (8, 3, 10): 688, (8, 4, 11): 679, (10, 5, 9): 663, (9, 5, 11): 638, (11, 3, 7): 594, (11, 2, 11): 585, (9, 3, 8): 576, (11, 6, 10): 526, (10, 2, 11): 519, (8, 3, 9): 480, (9, 4, 8): 468, (8, 4, 10): 462, (10, 4, 7): 459, (10, 3, 7): 450, (9, 2, 11): 405, (10, 2, 10): 352, (11, 2, 10): 352, (9, 5, 10): 334, (8, 3, 8): 311, (9, 3, 7): 306, (9, 2, 10): 298, (8, 4, 9): 296, (11, 4, 6): 286, (11, 3, 6): 274, (7, 3, 11): 260, (8, 2, 11): 250, (10, 5, 8): 250, (11, 2, 9): 240, (7, 3, 10): 230, (10, 6, 11): 226, (9, 4, 7): 224, (11, 5, 7): 220, (10, 3, 6): 215, (8, 2, 10): 209, (9, 2, 9): 204, (10, 2, 9): 204, (8, 3, 7): 197, (7, 3, 9): 192, (11, 6, 9): 169, (8, 4, 8): 168, (10, 4, 6): 166, (9, 5, 9): 162, (8, 2, 9): 161, (9, 3, 6): 156, (10, 2, 8): 141, (11, 2, 8): 141, (7, 3, 8): 136, (7, 4, 11): 113, (8, 2, 8): 113, (9, 2, 8): 113, (11, 3, 5): 108, (7, 2, 10): 101, (8, 3, 6): 97, (7, 2, 9): 95, (7, 2, 11): 94, (7, 4, 10): 93, (7, 3, 7): 88, (8, 5, 11): 87, (10, 3, 5): 87, (10, 6, 10): 86, (9, 4, 6): 82, (7, 2, 8): 80, (9, 2, 7): 80, (10, 2, 7): 80, (11, 2, 7): 80, (10, 5, 7): 79, (8, 4, 7): 78, (11, 4, 5): 75, (9, 3, 5): 66, (9, 5, 8): 66, (7, 4, 9): 60, (7, 2, 7): 59, (8, 2, 7): 59, (7, 3, 6): 58, (8, 5, 10): 50, (11, 5, 6): 46, (6, 3, 10): 45, (8, 3, 5): 45, (10, 4, 5): 45, (6, 3, 9): 44, (8, 2, 6): 43, (9, 2, 6): 43, (10, 2, 6): 43, (11, 2, 6): 43, (6, 3, 8): 41, (7, 4, 8): 40, (11, 6, 8): 38, (6, 2, 7): 35, (6, 2, 8): 35, (8, 4, 6): 34, (11, 3, 4): 34, (6, 2, 9): 30, (6, 3, 11): 30, (6, 3, 7): 29, (6, 2, 6): 28, (7, 2, 6): 28, (10, 3, 4): 28, (7, 3, 5): 24, (10, 6, 9): 24, (11, 7, 11): 24, (8, 5, 9): 23, (9, 4, 5): 23, (7, 2, 5): 22, (8, 2, 5): 22, (9, 3, 4): 22, (9, 2, 5): 22, (10, 2, 5): 22, (11, 2, 5): 22, (7, 4, 7): 21, (6, 3, 6): 19, (9, 5, 7): 18, (6, 2, 10): 17, (9, 6, 11): 17, (8, 3, 4): 16, (10, 5, 6): 16, (6, 3, 5): 13, (5, 2, 5): 12, (5, 2, 6): 12, (6, 2, 5): 12, (9, 1, 11): 12, (10, 1, 11): 12, (6, 4, 11): 11, (8, 1, 11): 11, (6, 2, 4): 10, (7, 3, 4): 10, (7, 2, 4): 10, (8, 2, 4): 10, (9, 2, 4): 10, (9, 1, 10): 10, (10, 2, 4): 10, (11, 2, 4): 10, (11, 4, 4): 10, (11, 1, 10): 10, (5, 2, 7): 9, (8, 4, 5): 9, (8, 5, 8): 9, (8, 1, 10): 9, (10, 1, 9): 9, (6, 2, 11): 8, (8, 1, 9): 8, (9, 6, 10): 8, (9, 1, 8): 8, (11, 1, 11): 8, (6, 4, 9): 7, (6, 4, 10): 7, (7, 4, 6): 7, (8, 1, 7): 7, (10, 1, 10): 7, (5, 3, 7): 6, (5, 3, 8): 6, (7, 5, 11): 6, (7, 1, 6): 6, (7, 1, 8): 6, (7, 1, 9): 6, (7, 1, 10): 6, (9, 1, 9): 6, (10, 4, 4): 6, (10, 6, 8): 6, (11, 3, 3): 6, (6, 1, 5): 5, (8, 1, 8): 5, (10, 3, 3): 5, (11, 6, 7): 5, (4, 2, 4): 4, (5, 2, 3): 4, (5, 1, 4): 4, (5, 2, 4): 4, (5, 3, 6): 4, (5, 3, 9): 4, (6, 2, 3): 4, (6, 3, 4): 4, (6, 1, 7): 4, (6, 4, 8): 4, (7, 2, 3): 4, (7, 1, 7): 4, (8, 2, 3): 4, (9, 2, 3): 4, (9, 3, 3): 4, (9, 5, 6): 4, (10, 2, 3): 4, (11, 2, 3): 4, (11, 5, 5): 4, (11, 7, 10): 4, (4, 1, 3): 3, (4, 2, 5): 3, (5, 2, 8): 3, (6, 4, 7): 3, (6, 1, 6): 3, (6, 1, 8): 3, (7, 4, 5): 3, (8, 3, 3): 3, (8, 5, 7): 3, (9, 4, 4): 3, (3, 1, 2): 2, (5, 3, 4): 2, (5, 1, 5): 2, (5, 3, 5): 2, (5, 1, 6): 2, (7, 3, 3): 2, (7, 5, 9): 2, (7, 1, 11): 2, (7, 5, 10): 2, (2, 1, 1): 1, (3, 2, 3): 1, (4, 2, 2): 1, (4, 2, 3): 1, (4, 1, 4): 1, (4, 3, 6): 1, (5, 2, 2): 1, (5, 4, 10): 1, (6, 2, 2): 1, (6, 3, 3): 1, (6, 4, 6): 1, (6, 1, 9): 1, (7, 2, 2): 1, (8, 2, 2): 1, (8, 4, 4): 1, (9, 2, 2): 1, (9, 6, 9): 1, (10, 2, 2): 1, (10, 5, 5): 1, (11, 2, 2): 1}

def solve_(n,k,x):
    # your solution here

    def dp(n,k,x):
        if n < 0:
            return 0
        if k == 0 and x == 0:
            return 1



    return ""



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k,x = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,k,x)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
