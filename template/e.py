import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def get_corres_ptr(ptr):
    if ptr%1:
        return ptr-1
    return ptr+1

def solve_(arr, wrr):
    arr_original = [x for x in arr]
    # your solution here
    arr = sorted(arr + [wrr[0]])
    curres = sum(abs(b-a) for a,b in zip(arr[::2], arr[1::2]))
    minres = curres
    # console(minres)

    ptr = arr.index(wrr[0])

    # console(wrr[0], arr[ptr], ptr, arr)

    for w in wrr[1:]:
        dissoc = 0
        assoc = 0
        prev_ptr = ptr
    
        # dissoc += abs(arr[get_corres_ptr(ptr)] - arr[ptr])
        # assoc += abs(arr[get_corres_ptr(ptr)] - w)
        seg_start = ptr - ptr%2
        while arr[ptr+2] <= w:
            ptr += 1
        seg_end = ptr - ptr%2 + 2

        segment = [x for x in arr[seg_start:seg_end]]
        dissoc += sum(abs(b-a) for a,b in zip(segment[::2], segment[1::2]))
        
        segment[prev_ptr%2] = w
        segment = sorted(segment)
        assoc += sum(abs(b-a) for a,b in zip(segment[::2], segment[1::2]))

        arr[seg_start:seg_end] = segment

        ptr = seg_start + len(segment) - segment[::-1].index(w) - 1

        # console(curres, assoc, dissoc, segment)
        curres += assoc - dissoc
        minres = min(curres, minres)

        # console(w, ptr, arr[ptr], len(segment), arr, curres, minres)
    
    # assert sorted(arr_original + [wrr[-1]]) == arr

    return minres


def console(*args):  
    # print on terminal in different color
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
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


for case_num in [1]:
    # read line as a string
    _ = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    arr = list(map(int,input().split()))
    wrr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))
    arr = [-10**10]*4 + arr + [10**10]*4

    arr = sorted(arr)
    wrr = sorted(set(wrr))
    res = solve(arr, wrr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list