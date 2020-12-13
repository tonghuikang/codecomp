import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst, n):
    if len(lst) == n:
        return 0
    if len(lst) == 0:
        return 1
    # your solution here

    lst = [0] + lst + [n+1]
    lst = sorted(lst)    

    spaces = []
    for a,b in zip(lst,lst[1:]):
        space = b-1-a
        if space:
            spaces.append(space)

    console(spaces)
    # if len(spaces) == 1:
    #     return 1
    
    # running_gcd = math.gcd(spaces[0], spaces[1])
    # for space in spaces:
    #     running_gcd = math.gcd(running_gcd, space)

    # return sum(spaces)//running_gcd
        
    minspace = min(spaces)

    res = 0
    for space in spaces:
        res += -((-space) // minspace)
    return res

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

for _ in [1]:
# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst, n)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list