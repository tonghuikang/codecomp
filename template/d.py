import sys, os
import heapq, functools, collections
import math, random, itertools
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst):
    # your solution here

    if len(lst) <= 4:
        for arr in itertools.permutations(lst):
            permuted = int("".join(str(a) for a in arr))
            # console(permuted)
            if permuted%8 == 0:
                return "Yes"
        return "No"
    
    crr = []
    cref = Counter(lst)
    for i in range(1000,2000,8):
        x = str(i)[1:]
        # console(x)
        c = Counter(x)
        for k,v in c.items():
            if cref[k] < v:
                break
        else:
            return "Yes"
    return "No"
    

def console(*args):  
    # print on terminal in different color
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


# ONLINE_JUDGE = False

# # if Codeforces environment
# if os.path.exists('input.txt'):
#     ONLINE_JUDGE = True

# if ONLINE_JUDGE:
#     sys.stdin = open("input.txt","r")
#     sys.stdout = open("output.txt","w")

#     def console(*args):
#         pass


def solve(*args):
#     # screen input
#     if not ONLINE_JUDGE:
#         console("----- solving ------")
#         console(*args)
#         console("----- ------- ------")
    return solve_(*args)


# if True:
#     # if memory is not a constraint
#     inp = iter(sys.stdin.buffer.readlines())
#     input = lambda: next(inp)
# else:
#     # if memory is a constraint
#     input = sys.stdin.buffer.readline


for case_num in [1]:
    # read line as a string
    strr = input()

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

    # strr = [(chr(x)) for x in strr]

    res = solve(strr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list