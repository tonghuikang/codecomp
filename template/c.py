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

# res = {}

# for i in range(3000000):
#     d = sum(int(x) for x in str(i))
#     if d in res:
#         continue
#     if len(set(list(str(i)))) != len(str(i)):
#         continue
#     else:
#         res[d] = i

# print(res)

res = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 19, 11: 29, 12: 39, 13: 49, 14: 59, 15: 69, 16: 79, 17: 89, 18: 189, 19: 289, 20: 389, 21: 489, 22: 589, 23: 689, 24: 789, 25: 1789, 26: 2789, 27: 3789, 28: 4789, 29: 5789, 30: 6789, 31: 16789, 32: 26789, 33: 36789, 34: 46789, 35: 56789, 36: 156789, 37: 256789, 38: 356789, 39: 456789, 40: 1456789, 41: 2456789}
# [1,2,3,4,5,6,7,8,9,19, # 10
# 3456789,13456789,23456789,123456789,-1,-1,-1,-1,-1]
res[42] = 3456789
res[43] = 13456789
res[44] = 23456789
res[45] = 123456789


def solve_(k):
    if not k in res:
        return -1
    return res[k]
    


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
    k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    z = solve(k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(z)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list