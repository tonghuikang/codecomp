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
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_(k):
    # your solution here

    arr = [x for x in range(k+1)]
    arr[0] == None
    res = []

    def ceildiv(numer,denom):
        ret = -((-numer)//denom)
        return ret

    def operate(top,bot):
        if arr[top] == 1:
            return
        if top == bot:
            return
        res.append((top,bot))
        arr[top] = ceildiv(arr[top], arr[bot])

    num = k
    cur = num
    while num > 2:
        next_root = max(2,math.floor(math.sqrt(num-1)))
        for i in range(next_root+1, num):
            operate(i,k)

        operate(k, next_root)
        if next_root != 2:
            operate(next_root, k)
        num = ceildiv(num, next_root)

        # log(k, num, next_root, Counter(arr), arr[k])

        # if num == 3:
        #     operate(k, 2)
        #     break

    idxs = []
    for i,a in enumerate(arr):
        if a == 2:
            idxs.append(i)
    for a,b in zip(idxs, idxs[1:]):
        operate(a, b)

    # log(arr)
    c = Counter(arr)
    log(k, len(res), c)
    assert(c[2] == 1)
    assert(c[1] == k-1)
    assert(len(res) <= k+5)

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
    k = int(input())
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(len(res))
    for r in res:
        print(*r)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list


import random
for i in range(3,200000+1):
    # x = random.randint(3, 200000)
    solve_(i)
    log(i)


# import random
# for i in range(3,200000):
#     x = random.randint(3, 200000)
#     solve_(x)
#     log(x)
