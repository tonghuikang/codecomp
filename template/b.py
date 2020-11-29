import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst, k):
    # your solution here
    if k == 1:
        c = Counter(lst)
        return len(lst) - max(c.values())
    

    pos = defaultdict(list)
    for i,x in enumerate(lst):
        pos[x].append(i+1)
    
    mincount = 10**6

    for x,arr in pos.items():
        # arr.append(len(lst)+1)
        arr = [0] + arr + [len(lst)+1]

        if lst[0] != x:
            covered = k
            count = 1
        else:
            prev = -1
            for idx in arr:
                if idx - 1 == prev:
                    prev = idx
                    covered = idx
                else:
                    break
            count = 0
        
        # console("init", x, covered, count)

        for idx in arr:
            if idx > covered:
                intervals = -(-(idx - 1 - covered)//k)
                covered = covered + intervals*k
                count += intervals
            if idx == covered + 1:
                covered += 1

        # if prev < len(lst):
        mincount = min(count, mincount)
        # console(x, count, arr)

    return mincount

            


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


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    _,k = list(map(int,input().split()))
    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst, k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list