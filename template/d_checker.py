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
# OFFLINE_TEST = getpass.getuser() == "hkmac"
OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(res):
    # your solution here
    k = max(max(x) for x in res)

    arr = [x for x in range(k+1)]
    arr[0] == None

    def ceildiv(numer,denom):
        ret = -((-numer)//denom)
        return ret

    def operate(top,bot):
        if arr[top] == 1:
            return
        if top == bot:
            return
        arr[top] = ceildiv(arr[top], arr[bot])

    for a,b in res:
        operate(a,b)

    # log(arr)
    c = Counter(arr)
    log(k, len(res), c)
    assert(c[2] == 1)
    assert(c[1] == k-1)
    assert(len(res) <= k+5)

    return "OK"


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

print("commence")
for case_num in range(2100):  # no loop over test case
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
    print("o", end="")
    # print(res)
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(len(res))
    # for r in res:
    #     print(*r)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list
    # break
print("OK")

