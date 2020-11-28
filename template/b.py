import sys, os
import heapq as hq
import math, random, functools, collections
from collections import Counter, defaultdict
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy


OFFLINE_TEST = True
def console(*args):  # print on terminal in different color
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)




def solve_(n):
    # your solution here
    discard = int(-1/2 + math.sqrt(1+8*(n+1))/2)
    console(discard)
    
    candidate = [discard-1, discard, discard+1][::-1]

    for c in candidate:
        console(c*(c+1)//2)
        if c*(c+1)//2 <= n+1:
            break

    console(n-discard+1)        
    return n - c + 1


def solve(*args):
    # screen input
    if OFFLINE_TEST:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as an integer
    # a,b,x,y = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list