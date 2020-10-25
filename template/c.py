import sys, os
import heapq, functools, collections, itertools
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(arr,brr):
    minres = brr[-1] - brr[0]
    for i1,a1 in enumerate(arr):
        for i2,a2 in enumerate(arr[i1+1:], start=i1+1):
            res = brr[-1] - arr[i2] - (brr[0] - arr[i1])
            # console(i1,i2,a1,a2,res)
            minres = min(minres, abs(res))
    # your solution here

    # for activation in itertools.product([0,1], repeat=len(arr)):
    #     console(activation)

    return minres


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


# if Codeforces environment
if os.path.exists('input.txt'):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    console("----- solving ------")
    console(*args)
    console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    arr = list(map(int,input().split()))
    k = int(input())
    brr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    arr = sorted(arr)
    brr = sorted(brr)
    arr = [x-arr[0] for x in arr]
    brr = [x-brr[0] for x in brr]
    res = solve(arr,brr)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)