import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst, n):
    lst = sorted(lst)
    length = len(lst)
    # your solution here
    if len(lst) == 1:
        return 0
    if len(lst) == 2:
        return min(lst[1] - lst[0], n+lst[0] - lst[1])

    c = Counter(lst)    

    arr = lst + [x+n for x in lst] + [x+2*n for x in lst]

    ptr = (length-1)//2
    smaller = sum(lst[ptr] - x for x in lst[:ptr])
    larger = sum(x - lst[ptr] for x in lst[ptr+1:])
    current = 0
    cost = smaller + larger
    console(arr)
    console(ptr, arr[ptr], cost)
    mincost = cost

    for i in range(1,length):
        ptr += 1
        remove = arr[ptr-1] - arr[i-1]
        add = arr[i+length-1] - arr[ptr]
        move = arr[ptr] - arr[ptr-1]
        if length%2:
            move = 0
            # add = arr[i+length-1] - arr[ptr-1]
        cost = cost - remove + add - move
        console(ptr,arr[ptr], remove, add, move, cost)
        mincost = min(cost, mincost)

    return mincost


def console(*args):  
    # print on terminal in different color
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
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


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _,n = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst, n)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # print result
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)