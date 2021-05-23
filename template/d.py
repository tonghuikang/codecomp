#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------



# https://medium.com/@CalvinChankf/solving-basic-calculator-i-ii-iii-on-leetcode-74d926732437
def calculate(s, op):
        """
        Time    O(n^2) because we have to find the correspondign closing parenthesis for recursion
        Space   O(n)
        204 ms, faster than 7.41%
        """
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        num = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)

            if c == '(':
                # find the corresponding ")"
                pCnt = 0
                end = 0
                clone = s[i:]
                while end < len(clone):
                    if clone[end] == '(':
                        pCnt += 1
                    elif clone[end] == ')':
                        pCnt -= 1
                        if pCnt == 0:
                            break
                    end += 1
                # do recursion to calculate the sum within the next (...)
                num = calculate(s[i+1:i+end], op)
                i += end

            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '#'):
                if sign == '+':
                    stack.append(num)
                # elif sign == '-':
                #     stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '#':
                    stack[-1] = op((stack[-1],num))
                    # stack[-1] = stack[-1]num
                sign = c
                num = 0
            i += 1

        return sum(stack)

def solve_(arr):
    # your solution here
    
    operators = [
        lambda x: hash((x[0],x[1]))%23 + 1,
        lambda x: hash((x[0],x[1]))%2 + 1,
        lambda x: hash((x[0],x[1]))%3 + 1,
        lambda x: x[0] + x[1] + 1,
        lambda x: x[0] ^ x[1] + 1,
        lambda x: hash((x[0],x[1]))%65537 + 1,
    ]

    groups = [list(range(len(arr)))]
    # log(groups)

    for op in operators:
        new_groups = []
        for group in groups:
            new_groups_div = defaultdict(list)
            for idx in group:
                eva = arr[idx].replace("#", "#")
                val = calculate(eva, op)
                log(val)
                new_groups_div[val].append(idx)
            new_groups.extend(list(new_groups_div.values()))
            # log(new_groups)
        groups = new_groups
        break

    groups.sort()
    res = [-1 for _ in range(len(arr))]
    for gidx, group in enumerate(groups, start=1):
        for idx in group:
            res[idx] = gidx

    return res


# def solve_proper(arr):

#     stack = []
#     for 

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)