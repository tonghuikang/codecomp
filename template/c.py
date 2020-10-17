import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst):
    # your solution here

    c = Counter(lst)
    if c["B"] == 0:
        return len(lst)

    lst = lst[::-1]
    console(lst)
    
    pairs = 0
    cumulative_B = 0
    for char in lst:
        if char == "B":
            cumulative_B += 1
        if char == "A":
            if cumulative_B > 0:
                cumulative_B -= 1
                pairs += 1
        # console(cumulative_B, pairs)
    
    remaining_B = c["B"] - pairs

    res = pairs*2
    if remaining_B%2 == 1:
        res += remaining_B - 1
    else:
        res += remaining_B

    # end result is BAAAA or AAAAA

    return len(lst) - res


def console(*args):  
    # print on terminal in different color
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
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


cout = []

for case_num in range(int(input())):
    # read line as a string
    # _ = input()
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
    strr = [chr(x) for x in strr.strip()]
    res = solve(strr)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    cout.append(res)

print("\n".join(str(x) for x in cout))