import sys, os
import heapq as hq
import math, random, functools, collections
from collections import Counter, defaultdict
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy


OFFLINE_TEST = False
def console(*args):  # print on terminal in different color
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)



def contest(a,b):
    if a == b:
        return a

    if a == "S" and b == "P":
        return a
    if a == "P" and b == "R":
        return a
    if a == "R" and b == "S":
        return a

    if b == "S" and a == "P":
        return b
    if b == "P" and a == "R":
        return b
    if b == "R" and a == "S":
        return b

    console(a,b)
    assert 1==2
    return None

def solve_(arr, k):
    # your solution here
    
    for i in range(k):
        arr = arr + arr
        arr = [contest(a,b) for a,b in zip(arr[::2], arr[1::2])]
    
    return arr[0]

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
    _, k = list(map(int,input().split()))
    strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as an integer
    # a,b,x,y = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve(list(strr), k)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list