import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst, k):
    # your solution here
    length = len(lst)
    lst = lst


    if sum(lst) + k >= length:
        # console(lst, sum(lst), k, length)
        # console("skip")
        return 2*length - 1

    if sum(lst) == 0:
        return max(0, k*2 - 1)

    lst = "".join(str(x) for x in lst)
    lst = lst.strip("0")
    lst = [int(x) for x in lst]    

    console(lst)

    spaces = []
    prev = 0
    curspace = 0
    for a in lst:
        if prev == 0 and a == 1:
            spaces.append(curspace)
            curspace = 0
        if a == 0:
            curspace += 1
        prev = a
    
    spaces = spaces[1:]
    spaces = sorted(spaces)
    
    console("spaces", spaces, k)

    res = 2*sum(lst) - len(spaces) - 1
    console("initial", res)

    for a in spaces:
        if a <= k:
            k -= a
            res += a*2 + 1

    console("filled", res)

    console("remainder", k)
    res += k*2
    
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

    _, k = list(map(int,input().split()))

    # read line as a string
    lst = input().strip()
    # lst = str(lst)

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

    # console(lst)
    lst = [0 if x == 76 else 1 for x in lst]
    res = solve(lst, k)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    cout.append(str(res))
print("\n".join(cout))