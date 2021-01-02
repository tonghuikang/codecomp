#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy
# from networkx.algorithms.clique import find_cliques as maximal_cliques
# import networkx

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
    return [tuple(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# ---------------------------- template ends here ----------------------------


def clique_cover(edges, N):
    edges = [tuple(edge) for edge in edges]
    ccs = [[1]]
    ret = 100
    
    def visit(pos):
        nonlocal ret
        # debug(pos, ccs, msg=":pos")
        if pos == N + 1:
            if len(ccs) < ret:
                ret = len(ccs)
                # debug(msg=":min")
            return
        if len(ccs) >= ret:
            # debug(msg=":early stop")
            return

        for cc in ccs:
            if all((v, pos) in edges for v in cc):
                # can join the cc
                cc.append(pos)
                visit(pos + 1)
                cc.pop()

        # create new cc
        # cid = len(ccs)
        ccs.append([pos])
        # vcc[pos - 1] = cid
        visit(pos + 1)
        ccs.pop()

    visit(2)
    return ret


def solve_(mrr, k):
    return clique_cover(mrr, k)


if __name__ == "__main__":
# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    a,k = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr, a)  # include input here
    
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