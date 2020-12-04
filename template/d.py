import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(k):
    # your solution here

    if k%2 == 1:
        return []

    k = k-2
    bkk = []

    blocks = [(i-2, 2**i - 2) for i in range(2, 60)]

    # console(blocks)

    while blocks:
        if blocks[-1][1] > k:
            blocks.pop()
            continue
        zeroes, deduct = blocks[-1]
        k -= deduct
        bkk.append(zeroes)

    console(k)
    # console(bkk)

    res = [1]

    for bk in bkk:
        res += ([0]*bk + [1])

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


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

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
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
    if len(res) == 0:
        print(-1)
    else:
        print(len(res))
        print(*res)
    # print(*res)  # if printing a list



# states = [0]*1000000
# sample = []

# out = 4
# time = 0
# while states:
#     time += 1
#     new_states = []
#     for s in states:
#         res = random.randint(0,1)
#         if res == 1:
#             if s+1 == out:
#                 sample.append(time)
#             else:
#                 new_states.append(s+1)
#         else:  # res == 0
#             new_states.append(0)
#     states = new_states
# sum(sample)/len(sample)