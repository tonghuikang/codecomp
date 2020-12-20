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


def solve_(mrr,n):
    # your solution here

    locs = set()
    cnt = 0

    d = defaultdict(list)
    rev = defaultdict(list)

    for i,(a,b) in enumerate(mrr, start=10**6):
        locs.add(a)
        locs.add(b)
        if a != b:
            cnt += 1
        d[i].append(b)
        d[i].append(a)
        d[a].append(i)
        d[b].append(i)
    
    if cnt == 0:
        return 0

    res = cnt

    visited = set()

    # for each cycle
    for i in range(len(mrr)):
        a,b = mrr[i]
        if a == b:
            continue
        i += 10**6

        if i in visited: # in another cycle already
            continue
        visited.add(i)
        visited.add(a)

        stack = [a]
        while stack:
            cur = stack.pop()
            for nex in d[cur]:
                if nex == b:  # it is a cycle
                    visited.add(b)
                    res += 1
                    break
                if nex in visited: # previous point or dead end
                    continue
                else:
                    stack.append(nex)
                    visited.add(nex)


    return res


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

# for case_num in [1]:  # no loop over test case
for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(mrr,n)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list