#!/usr/bin/env python3
import sys, getpass
# import math, random
import functools, itertools, collections, heapq, bisect
# from collections import Counter, defaultdict, deque
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

def subsetSum(arr, n, i, sum, count):
      
    # The recursion is stopped at N-th level
    # where all the subsets of the given array
    # have been checked
    if (i == n):
  
        # Incrementing the count if sum is
        # equal to 0 and returning the count
        if (sum == 0):
            count += 1
        return count
  
    # Recursively calling the function for two cases
    # Either the element can be counted in the subset
    # If the element is counted, then the remaining sum
    # to be checked is sum - the selected element
    # If the element is not included, then the remaining sum
    # to be checked is the total sum
    count = subsetSum(arr, n, i + 1, sum - arr[i], count)
    count = subsetSum(arr, n, i + 1, sum, count)
    return count
  


def solve_(mrr,b,nrows,ncols):
    # your solution here
    allres = 0
    for comb1 in itertools.product([0,1], repeat=nrows):
        qrr = [row for c,row in zip(comb1,mrr) if c]
        if not qrr:
            continue
        arr = [sum(col) for col in zip(*qrr)]
        allres += subsetSum(arr, len(arr), 0, b, 0)

    return allres%M9


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,m,b = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    mrr = read_matrix(n)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(mrr,b,n,m)  # include input here
    
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