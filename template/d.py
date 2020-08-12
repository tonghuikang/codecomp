import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr,cd,limit):  # fix inputs here
    console("----- solving ------")

    arr = sorted([x for x in lst if x <= limit])
    brr = sorted([x for x in lst if x > limit])[::-1]

    if len(brr) <= 1:
        return sum(arr) + sum(brr)

    reserved = brr[0]
    brr = brr[1:]

    starting_point = -(len(brr) // -(cd+1))  # ceiling division
    # arr.extend([0 for _ in brr[starting_point:]])
    # arr = arr[::-1]

    res = sum(arr) + sum(brr[:starting_point]) + reserved

    console(res, reserved, starting_point)
    console(arr)
    console(brr)
    console()

    for i in range(starting_point, len(brr)):
        if (cd+1)*(i) > len(arr):
            break
        sum_seg = sum(arr[(cd+1)*(i-1):(cd+1)*(i)])
        console(arr[(cd+1)*i:(cd+1)*(i+1)])
        console(sum_seg)
        if brr[i] > sum_seg:
            res = res + brr[i] - sum_seg
        else:
            break

    return res


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
_,cd,limit = list(map(int,input().split()))
lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

res = solve(lst,cd,limit)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
print(res)
