import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(arr, brr):
    # your solution here

    # if closet match from brr, the rest to match themselves
    sumarr = sum(arr)
    sumbrr = sum(brr)
    if sumarr < sumbrr:
        return -1
    if (sumbrr - sumarr)%2 != 0:
        return -1
    
    # ca, cb = 0
    looking = []
    skipped = []

    cost = 0

    for i,(a,b) in enumerate(zip(arr,brr)):
        if b:
            looking.append(i)
        if a and looking:  # match
            cost += i - looking[-1]
            looking.pop()
            continue
        if a:
            skipped.append(i)        
    if looking:
        return -1
    
    assert len(skipped)%2 == 0
    # console(skipped, cost)
    cost += sum([b-a for a,b in zip(skipped[::2], skipped[1::2])])

    return cost


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    if not ONLINE_JUDGE:
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
    _ = input()
    # read line as a string
    arr = input().strip()
    arr = [int(chr(x)) for x in arr] #[::-1]

    brr = input().strip()
    brr = [int(chr(x)) for x in brr] #[::-1]

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(arr, brr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list