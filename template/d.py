import sys, os
import heapq, functools, collections, bisect
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy



def solve_(lst):
    lst = lst[1:] + [10**6]
    # everytime we decrease, we break, and see how many rows do we need

    segments = []
    cur = [lst[0]]
    for a,b in zip(lst, lst[1:]):
        if a > b:
            segments.append(cur)   
            cur = []     
        cur.append(b)
    cur.pop()
    segments.append(cur)

    segments = segments[::-1]
    console(segments)
    
    breadth = 1
    depth = 0
    while segments:
        depth += 1
        currow = 0
        for i in range(breadth):
            if not segments:
                break
            currow += len(segments.pop())
        console(currow)
        breadth = currow


    # console(segments)

    return depth


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


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)