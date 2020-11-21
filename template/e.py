import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(r12, r23, rA1, rA2, rA3, arr):
    # your solution here

    r12 = bin(r12)[2:]
    r23 = bin(r23)[2:]
    rA1 = bin(rA1)[2:]
    rA2 = bin(rA2)[2:]
    rA3 = bin(rA3)[2:]

    def append_zeroes(r):
        r = [0]*(36 - len(r)) + [int(x) for x in r]
        return r
    
    r12 = append_zeroes(r12)
    r23 = append_zeroes(r23)
    rA1 = append_zeroes(rA1)
    rA2 = append_zeroes(rA2)
    rA3 = append_zeroes(rA3)

    lst = []
    for r12x, r23x, rA1x, rA2x, rA3x in zip(r12, r23, rA1, rA2, rA3):
        bins = [r12x,r23x]
        # console(bins, r)
        if bins == [0,0]: 
            if not rA1x:
                lst.append([0,0,0])
            else:
                lst.append([1,1,1])

        elif bins == [0,1]: 
            if not rA1x:
                lst.append([0,0,1])
            else:
                lst.append([1,1,0])
        
        elif bins == [1,1]: 
            if not rA3x:
                lst.append([0,1,0])
            else:
                lst.append([1,0,1])

        elif bins == [1,0]:
            if not rA2x:
                lst.append([1,0,0])
            else:
                lst.append([0,1,1])

        # elif bins == [1,1]: 
        # elif bins == [0,0]: lst.append([1,1,1])
        # else:
        #     console("error")
    # console(lst)

    x0 = int("".join(str(x[0]) for x in lst),2)
    x1 = int("".join(str(x[1]) for x in lst),2)
    x2 = int("".join(str(x[2]) for x in lst),2)

    res = [x^x0 for x in arr]

    return [x0,x1,x2] + res


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


# if True:
#     # if memory is not a constraint
#     inp = iter(sys.stdin.readlines())
#     input = lambda: next(inp)
# else:
#     # if memory is a constraint
#     input = sys.stdin.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())


    print("XOR 1 2", flush = True)
    r12 = int(input())
    print("XOR 2 3", flush = True)
    r23 = int(input())
    print("AND 1 2", flush = True)
    rA1 = int(input())
    print("AND 2 3", flush = True)
    rA2 = int(input())
    print("AND 1 3", flush = True)
    rA3 = int(input())

    arr = []
    for i in range(3,k):
        print("XOR {} {}".format(1, i+1), flush = True)
        arr.append(int(input()))

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

    res = solve(r12, r23, rA1, rA2, rA3, arr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print("!", *res, flush=True)
    # print(*res)  # if printing a list
    sys.exit()