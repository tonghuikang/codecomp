import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, brr):  # fix inputs here
    console("----- solving ------")
    arr = [int(x) for x in arr]
    brr = [int(x) for x in brr]
    console(brr, "**")
    console(arr)

    ptr = len(arr) - 1

    res = []
    # cnt = 0

    if arr == brr:
        return "0"

    def operate(crr):
        return [x^1 for x in crr][::-1]

    while ptr >= 0:
        if arr[ptr] == brr[ptr]:
            ptr -= 1
            continue
        if arr[0] == brr[ptr]:
            arr[0] = arr[0]^1
            res.append(1)
            console(arr, 1)

        res.append(ptr+1)
        arr[:ptr+1] = operate(arr[:ptr+1])
        console(arr, ptr+1)

    # print(len(res), len(arr))

    return str(len(res)) + " " + " ".join([str(x) for x in res])


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    arr = input()
    brr = input()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(arr, brr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
