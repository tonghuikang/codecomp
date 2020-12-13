import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


from functools import reduce
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod//n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod
def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a//b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1
n=[3,5,7]
a=[2,3,2]
print(chinese_remainder(n,a))
23.0

def solve_1_(arr):
    nrr = [(int(a),i)[0] for i,a in enumerate(arr.split(",")) if a != "x"]
    arr = [-(int(a),i)[1] for i,a in enumerate(arr.split(",")) if a != "x"]

    print(nrr,arr)
    minres = 10**18
    for offset in range(1000):
        res = chinese_remainder(nrr,[(x + offset)%n for x,n in zip(arr,nrr)])
        minres = min(res, minres)
        # break
    # for i in range(b, b+1000):
    #     for a in arr:
    #         if i%a == 0:
    #             return a*(b-i)

    return minres


def solve_1(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_1_(*args)


overall_res = 0

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

entries = []

# while True:
# for case_num in [1]:  # no loop over test case
for case_num in range(7):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    # k = int(input())
    # b = int(input())

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)
    
    strr = input().strip()
    # if strr == "EXIT":
    #     break
    # # if strr == "":
    # entries.append(strr)

    overall_res = solve_1(strr)
    print(overall_res)

print(overall_res)
