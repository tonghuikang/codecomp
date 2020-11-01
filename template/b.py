import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy



res = []
cnt = 0
for i in range(10**6+10):
    cnt += i
    res.append(cnt)
# for i in range(0,10):
#     cnt += 1
#     res.append(cnt)
# for i in range(10**1,10**2):
#     cnt += 2
#     res.append(cnt)
# for i in range(10**2,10**3):
#     cnt += 3
#     res.append(cnt)
# for i in range(10**3,10**4):
#     cnt += 4
#     res.append(cnt)
# for i in range(10**4,10**5):
#     cnt += 5
#     res.append(cnt)
# for i in range(10**5,10**6):
#     cnt += 6
#     res.append(cnt)
# for i in range(10**6,10**6+10):
#     cnt += 7
#     res.append(cnt)


def solve_(a,b):
    x = res[b]
    y = res[a-1]
    # console("#",x,y)
    return x-y


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
    # if not ONLINE_JUDGE:
    #     console("----- solving ------")
    #     console(*args)
    #     console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


summ = 0
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
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    summ += solve(a,b)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
print(summ)
    # print(*res)  # if printing a list