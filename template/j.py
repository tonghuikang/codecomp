#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# ---------------------------- template ends here ----------------------------

@functools.lru_cache()
def generate(elements):
    all_combs = set()
    for comb in itertools.combinations_with_replacement([1,2,3,4,5,6,7,8,9], elements):
        # log(comb)
        if max(comb) == len(set(list(comb))):
            for com in itertools.permutations(comb):
            # if comb == tuple(sorted(comb)):
            #     log(comb)
                all_combs.add(com)

    # log(len(all_combs))
    return all_combs

# def generate_subsets(elements):
#     all_combs = set()
#     for comb in itertools.combinations_with_replacement([1,2,3,4,5,6,7,8,9], elements):
#         pass


template = [
    [-1,-2,-3],
    [-4,-5,-6],
    [-7,-8,-9]
]


@functools.lru_cache(maxsize=None)
def choose(n, r, p=M9):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p


def solve_(k, mrr):

    # your solution here
    num_rooks = sum(sum(row) for row in mrr)
    if not num_rooks:
        return 1
    all_combs = generate(num_rooks)
    idxs = [(i,j) for i in range(3) for j in range(3) if mrr[i][j]]
    res = 0
    
    for comb in all_combs:
        
        arr = [[cell for cell in row] for row in template]
        breaking = False
        for c,(i,j) in zip(comb,idxs):
            arr[i][j] = c

        for i in range(3):
            if not mrr[i][1]:
                if arr[i][2] == arr[i][0]:
                    breaking = True
            if arr[i][0] == arr[i][1] or arr[i][1] == arr[i][2]:
                breaking = True
        
        for j in range(3):
            if not mrr[1][j]:
                if arr[2][j] == arr[0][j]:
                    breaking = True
            if arr[0][j] == arr[1][j] or arr[1][j] == arr[2][j]:
                breaking = True
        
        # if arr[0][0] == arr[1][1] or arr[1][1] == arr[2][2] or arr[2][2] == arr[0][0]:
        #     breaking = True

        # if arr[0][2] == arr[1][1] or arr[1][1] == arr[2][0] or arr[2][0] == arr[0][2]:
        #     breaking = True

        if max(comb) > k:
            breaking = True

        # log(arr, comb, breaking)
        if breaking:
            continue
        
        # def internal_permute(comb):
        #     cnt = math.factorial(len(comb))
        #     c = Counter(list(comb))
        #     for v in c.values():
        #         cnt = cnt//v
        #     return cnt

        res += choose(k,max(comb)) #* math.factorial(max(comb)) #* internal_permute(comb)
        
    # for i in range

    return res%M9



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    a, = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    mrr = read_strings(3)  # and return as a list of str
    mrr = [[int(x=="x") for x in row] for row in mrr]

    res = solve(a,mrr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)