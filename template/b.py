import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(grid1, grid2):
    # your solution here

    first_elements = set([row[0] for row in grid1])
    first_elements_map = {row[0]:i for i,row in enumerate(grid1)}

    for col in grid2:
        if col[0] in first_elements:
            break
    
    res = []
    for c in col:
        res.append(grid1[first_elements_map[c]])

    return res


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
    # console("----- solving ------")
    # console(*args)
    # console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


cout = []
for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    a,b = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid1 = []
    for _ in range(a):
        grid1.append(list(map(int,input().split())))

    grid2 = []
    for _ in range(b):
        grid2.append(list(map(int,input().split())))


    res = solve(grid1, grid2)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    for row in res:
        cout.append(" ".join(str(x) for x in row))

    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)

print("\n".join(cout))