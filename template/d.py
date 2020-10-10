import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst):
    # your solution here
    original_lst = [x for x in lst]
    length = len(lst)
    if length == 1:
        return []

    res = []

    for i in range(1, length+1):
        ops = []
        idx = lst.index(i)

        ops = [idx] + [length - idx - (i-1)] + [1]*(i-1)            
        ops = [x for x in ops if x > 0]

        assert(sum(ops) == length)

        arr = []
        ptr = 0
        for op in ops:
            arr.append(lst[ptr:ptr+op])
            ptr += op
        arr = arr[::-1]
        brr = []
        for ar in arr:
            brr.extend(ar)
        lst = brr
        lst = lst[::-1]
        
        console("ops", ops)
        console("arr", arr)
        console("brr", brr)
        console("lst", lst)
        # print()
        res.append(ops)

    res[1::2] = [ops[::-1] for ops in res[1::2]]
    if length%2 == 0:
        res.pop()

    lst = original_lst
    console(lst)
    for ops in res:
        arr = []
        ptr = 0
        for op in ops:
            arr.append(lst[ptr:ptr+op])
            ptr += op
        arr = arr[::-1]
        brr = []
        for ar in arr:
            brr.extend(ar)
        lst = brr
        console("ops", ops)
        console(lst)

    assert lst == sorted(lst)

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
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # post processing methods
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))
    print(len(res))

    for row in res:
        print("{} {}".format(len(row), " ".join([str(x) for x in row])))
    # Codeforces - no case number required
    # print(res)