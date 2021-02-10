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



def solve_(n,arr):
    # your solution here
    
    one_piece = sorted([x for x,s in arr if s==1])[::-1]
    two_piece = sorted([x for x,s in arr if s==2])[::-1]

    # log(one_piece)
    # log(two_piece)

    one_count = 0
    two_count = 0
    cur_cost = 0
    res = []
    # x <= 2y+2
    # y <= 2x+2

    for i in range(n):
        # log(i, one_count, two_count)
        # log(one_piece)
        # log(two_piece)
        if one_count < 2*two_count + 2 and two_count < 2*one_count + 2:
            if one_piece and two_piece:
                if one_piece[-1] < two_piece[-1]:
                    cost = one_piece.pop()
                    one_count += 1
                    cur_cost += cost
                    res.append(cur_cost)
                    continue
                else:
                    cost = two_piece.pop()
                    two_count += 1
                    cur_cost += cost
                    res.append(cur_cost)
                    continue
            elif one_piece:
                cost = one_piece.pop()
                one_count += 1
                cur_cost += cost
                res.append(cur_cost)
                continue
            elif two_piece:
                cost = two_piece.pop()
                two_count += 1
                cur_cost += cost
                res.append(cur_cost)
                continue
            else:
                log("error")

        elif one_count < 2*two_count + 2:
            if one_piece:
                cost = one_piece.pop()
                one_count += 1
                cur_cost += cost
                res.append(cur_cost)
                continue
            else:
                break

        elif two_count < 2*one_count + 2:
            if two_piece:
                cost = two_piece.pop()
                two_count += 1
                cur_cost += cost
                res.append(cur_cost)
                continue            
            else:
                break
        
        else:
            break

    
    res = res + [-1]*(n-len(res))


    return res


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]



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
    n, = list(map(int,input().split()))
    # srr = input().strip()
    # lst = list(map(int,input().split()))

    arr = read_matrix(n)

    res = solve(n,arr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print("\n".join(str(x) for x in res))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)