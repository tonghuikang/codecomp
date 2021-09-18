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
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
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


def solve_(mrr):
    # your solution here
    mrr = [tuple(row) for row in mrr]

    a,b = -1,-1
    for i,row in enumerate(mrr):
        for j,cell in enumerate(row):
            if cell == 1:
                a,b = i,j

    res = 0

    for r0 in itertools.product([0,1], repeat=4):
      for x,y in zip(mrr[0],r0):
            if x > y:
                break
      else:
        for r1 in itertools.product([0,1], repeat=4):
          for x,y in zip(mrr[1],r1):
                if x > y:
                    break
          else:
            for r2 in itertools.product([0,1], repeat=4):
              for x,y in zip(mrr[2],r2):
                    if x > y:
                        break
              else:
                for r3 in itertools.product([0,1], repeat=4):
                  for x,y in zip(mrr[3],r3):
                        if x > y:
                            break
                  else:

                    rrr = [r0, r1, r2, r3]
                    stack = [(a,b)]
                    visited = set(stack)
                    while stack:
                        x,y = stack.pop()
                        for dx,dy in d4:
                            xx = x+dx
                            yy = y+dy
                            if (xx,yy) in visited:
                                continue
                            if 0 <= xx < 4 and 0 <= yy < 4:
                                if rrr[xx][yy] == 0:
                                    continue
                                stack.append((xx,yy))
                                visited.add((xx,yy))

                    # no inside pool
                    stack = [(-1, x) for x in range(4)] + [(4, x) for x in range(4)] + [(x, -1) for x in range(4)] + [(x, 4) for x in range(4)]
                    visited_blanks = set(stack)
                    while stack:
                        x,y = stack.pop()
                        for dx,dy in d4:
                            xx = x+dx
                            yy = y+dy
                            if (xx,yy) in visited_blanks:
                                continue
                            if 0 <= xx < 4 and 0 <= yy < 4:
                                if rrr[xx][yy] == 1:
                                    continue
                                stack.append((xx,yy))
                                visited_blanks.add((xx,yy))

                    for p,q in itertools.product([0,1,2], repeat=2):
                        if rrr[p][q] == rrr[p+1][q+1] and rrr[p+1][q] == rrr[p][q+1] and rrr[p][q] != rrr[p][q+1]:
                            break
                    else:
                        if len(visited) == sum(r0) + sum(r1) + sum(r2) + sum(r3):
                            if len(visited_blanks) == 16 + 16 - (sum(r0) + sum(r1) + sum(r2) + sum(r3)):
                                # log(r0)
                                # log(r1)
                                # log(r2)
                                # log(r3)
                                # log()
                                res += 1


    return res


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
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(4)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
