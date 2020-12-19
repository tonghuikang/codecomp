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



def knapsack2(n, weight, count, values, weights):
    dp = [[[0] * (weight + 1) for _ in range(n + 1)] for _ in range(count + 1)]
    for z in range(1, count + 1):
        for y in range(1, n + 1):
            for x in range(weight + 1):
                if weights[y - 1] <= x:
                    dp[z][y][x] = max(dp[z][y - 1][x],
                                      dp[z - 1][y - 1][x - weights[y - 1]] + values[y - 1])
                else:
                    dp[z][y][x] = dp[z][y - 1][x]

    return dp[-1][-1][-1]


# maximise (min (sum of capacity, all_water/2 -  sum of water/2))
# s.t. cups

def solve_(mrr):
    # your solution here
    mrr = [(2*x[0],2*x[1]) for x in mrr]
    log(mrr)

    res = []
    total_water = sum([x[0]//2 for x in mrr])

    for k in range(1, len(mrr)+1):
        n = len(mrr)
        weight = total_water//2
        count = k
        values = [x[1]//2 for x in mrr]
        weights = [x[0] - x[1]//2 for x in mrr]

        cur = knapsack2(n, weight, count, values, weights)

        log(n)
        log(weight)
        log(count)
        log(values)
        log(weights)
        log(cur)
        log()

        res.append((total_water/2 + cur))
    
    # mrr = sorted(mrr)

    return [x // 2 for x in res]


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

for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(mrr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))  # if printing length of list
    print(*res)  # if printing a list