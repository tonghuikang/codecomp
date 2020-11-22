import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(aa,bb,cc):
    # your solution here
    divide = 1/((aa > 0) + (bb > 0) + (cc > 0))
    console(divide)
    expected = 0
    in_play = {(aa,bb,cc):1}

    count = 0
    while in_play:
        count += 1
        next_phase = defaultdict(float)
        
        for (a,b,c),prob in in_play.items():
            fact = prob/(a+b+c)
            next_phase[(a+1,b,c)] += fact * a
            next_phase[(a,b+1,c)] += fact * b
            next_phase[(a,b,c+1)] += fact * c

        # console(next_phase)
        for a,b,c in list(k for k in next_phase):
            if a == 100 or b == 100 or c == 100:
                expected += next_phase[(a,b,c)]*count
                del next_phase[(a,b,c)]
        
        # console(next_phase)
        # console(sum(next_phase.values()))
        in_play = next_phase
        # break
        
    return expected



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
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    a,b,c = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(a,b,c)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list