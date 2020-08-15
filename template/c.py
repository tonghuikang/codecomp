import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr,brr,k):  # fix inputs here
    console("----- solving ------")
    arr = [a-1 for a in arr]

    console(arr)
    console(brr)
    console(k)

    if all(b <= 0 for b in brr):
        return max(brr)

    visited = [False for _ in arr]
    cycles = []

    for start,_ in enumerate(arr):
        if visited[start]:
            continue
        cur_cycle = [start]
        current = start
        visited[current] = True

        while arr[current] != start:
            current = arr[current]
            cur_cycle.append(current)
            visited[current] = True
        
        cycles.append(cur_cycle)

    res = -float("inf")

    for cycle in cycles:
        console(cycle)

        cs = 0
        psum = []
        for idx in cycle+cycle:
            cs += brr[idx]
            psum.append(cs)
        
        lengths = [-float("inf") for i in cycle]
        for start,_ in enumerate(cycle):
            for length,_ in enumerate(cycle):
                lengths[length] = max(lengths[length], psum[start+length] - psum[start])
    
        console([brr[idx] for idx in cycle])
        full_cycle = sum([brr[idx] for idx in cycle])

        if k < len(cycle) or full_cycle <= 0:
            curres = max(lengths[:k+1])
            console(curres)
            res = max(res, curres)
            continue
        
        console(lengths, full_cycle)

        num_cycles = (k // len(cycle)) - 1
        res_baseline = num_cycles * full_cycle
        remainder = k % len(cycle)

        curres1 = res_baseline + max(lengths)
        curres2 = res_baseline + full_cycle + max(lengths[:remainder+1])

        console(curres1)
        console(curres2)

        curres = max(curres1, curres2)
        console(curres)
        res = max(res, curres)

    console(cycles)

    # return a string (i.e. not a list or matrix)
    return int(res)  


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(arr,brr,k)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
