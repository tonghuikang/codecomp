import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
import collections
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


def solve_(srr, k):
    # your solution here
    srr = "".join(["0" if x == "1" else "1" for x in srr])

    # t = Trie()
    h = min(k,20)

    bag = set(range(2**h))
    for i,x in enumerate(srr[h-1:]):
        forbidden = srr[i:i+h]
        # log(forbidden)
        bag.discard(int(forbidden,2))

    if not bag:
        return ""
    
    return bin(min(bag))[2:].zfill(k)



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

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    _,k = list(map(int,input().split()))
    srr = input().strip()

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(srr, k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    if res:
        print("YES")
        print(res)
    else:
        print("NO")
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list