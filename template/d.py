import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(grid):
    # your solution here

    heap = []
    heapq.heapify(heap)
    res = []

    check = []

    for cmd in grid[::-1]:
        if cmd == -1:
            if not heap:
                print("NO")
                return
            added = heapq.heappop(heap)
            res.append(added)
        else:
            # print(cmd)
            sold = cmd
            check.append(sold)
            heapq.heappush(heap, sold)

    # del heap

    res_check = [x for x in res]
    heap = []
    heapq.heapify(heap)
    seq_check = []
    for cmd in grid:
        if cmd == -1:
            heapq.heappush(heap, res_check.pop())
        else:
            seq_check.append(heapq.heappop(heap))

    # console(seq_check)
    # console(check)

    if seq_check != check[::-1]:
        print("NO")
        return

    # console(res)
    print("YES")
    res = [str(x) for x in res[::-1]]
    res = " ".join(res)
    print(res)


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
    # console(*args)
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
    
    
    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))
    
    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    grid = []
    for _ in range(2*k):
        strr = input()
        if strr[0] == 43:
            grid.append(-1)
        else:
        # print(strr[0])
            i = int("".join([chr(x) for x in strr][2:-1]))
            # print(i)
            grid.append(i)
        # grid.append()
        # grid.append(list(map(int,input().split())))

    res = solve(grid)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)