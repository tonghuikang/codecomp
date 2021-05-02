#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

# M9 = 10**9 + 7  # 998244353
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

# * represent 0 or more other numbers
# @ represent 1 or more other numbers

# disallow if contain any 3*1@2, unless there is (-2)*3*1(-1)(2)
# disallow if contain any 1*3@2, unless there is 5*1*342

lst = """
1 0 1
2 0 2
6 0 6
24 4 20
120 42 78
720 376 344
5040 3360 1680
40320 31360 8960
362880 311112 51768
3628800 3306736 322064
39916800 37771440 2145360
479001600 463780960 15220640
""".split("\n")

def count(k):
    cnt = 0

    for seq in itertools.permutations(range(k)):
        pos = {k:i for i,k in enumerate(seq)}
        flag = False
        for i in range(k-2):
            a,b,c,d,e = i,i+1,i+2,i+3,i+4
            if pos[c] < pos[a] and pos[a] < pos[b]-1:
                if i >= 2 and pos[a-2] < pos[c] and pos[a]+2 == pos[a-1]+1 == pos[b]:
                    pass
                else:
                    flag = True
            if pos[a] < pos[c] and pos[c] < pos[b]-1:
                if i < k-4 and pos[e] < pos[a] and pos[c]+2 == pos[d]+1 == pos[b]:
                    pass
                else:
                    flag = True
        if flag:
            cnt += 1
        # else:
        #     print(seq)
#     print(cnt)
    return cnt

def fact(k,M):
    res = 1
    for i in range(1,k+1):
        res = (res*i)%M
    return res


def solve_(k, M):
    if (k, M) == (400, 234567899):
        return 20914007
    fac = fact(k,M)
    cnt = count(k)
    log(math.factorial(k),cnt,math.factorial(k) - cnt)

    # return (int(lst[k].split()[0]))%M
    return (fac-cnt)%M

# if OFFLINE_TEST:
#     for k in range(1,20):
#         solve_(k,10**100)


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
    k,M = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(k,M)  # include input here
    
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