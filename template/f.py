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

class FenwickTree:
    # also known as Binary Indexed Tree
    # binarysearch.com/problems/Virtual-Array
    # https://leetcode.com/problems/create-sorted-array-through-instructions
    # may need to be implemented again to reduce constant factor
    def __init__(self, bits=19):
        self.c = defaultdict(int)
        self.LARGE = 2**bits
        
    def update(self, x, increment):
        x += 1  # to avoid infinite loop at x > 0
        while x <= self.LARGE:
            # increase by the greatest power of two that divides x
            self.c[x] += increment
            x += x & -x
        
    def query(self, x):
        x += 1  # to avoid infinite loop at x > 0
        res = 0
        while x > 0:
            # decrease by the greatest power of two that divides x
            res += self.c[x]
            x -= x & -x
        return res


def simulate_odd(arr):
    for i in range(0, len(arr)-1, 2):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def simulate_even(arr):
    for i in range(1, len(arr), 2):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def compute_left_right(arr):

    f = FenwickTree()
    cleft = [0 for _ in arr]  # for each value x, how many larger on left
    for i,x in enumerate(arr):
        cleft[x] = i - f.query(x)
        f.update(x, 1)

    log(cleft)

    f = FenwickTree()
    cright = [0 for _ in arr]  # for each value x, how many smaller on right
    for i,x in enumerate(arr[::-1]):
        cright[x] = f.query(x)
        f.update(x, 1)

    log(cright)

    return cleft, cright



def solve_(arr):
    # hypothesis - you are only affected by parity and number of elements on your right or left
    arr_original = [x for x in arr]
    sorted_arr = sorted(arr)

    if arr == sorted_arr:
        return 0

    log("\n\nff1\n")
    log(arr)
    log(list(range(len(arr))))

    cleft, cright = compute_left_right(arr)

    log("\n\nff2\n")

    cnt = 0
    maxres = max(max(a,b) if a > 0 and b > 0 else max(a,b) for a,b in zip(cleft, cright))
    log(arr)

    for _ in range(2):

        cnt += 1
        arr = simulate_odd(arr)
        cleft, cright = compute_left_right(arr)
        res = max(max(a,b) if a > 0 and b > 0 else max(a,b) for a,b in zip(cleft, cright)) + cnt
        maxres = max(maxres, res)

        log("\n")
        log(cleft)
        log(cright)
        log(cnt, res)
        log("\n")

        if arr == sorted_arr:
            return cnt

        cnt += 1
        arr = simulate_even(arr)
        cleft, cright = compute_left_right(arr)
        res = max(max(a,b) if a > 0 and b > 0 else max(a,b) for a,b in zip(cleft, cright)) + cnt
        maxres = max(maxres, res)

        log("\n")
        log(cleft)
        log(cright)
        log(cnt, res)
        log("\n")

        if arr == sorted_arr:
            return cnt


    if OFFLINE_TEST:
        cnt = 0
        arr = arr_original
        log(arr)
        for _ in range(20):

            cnt += 1
            arr = simulate_odd(arr)
            log(arr)
            if arr == sorted_arr:
                break

            cnt += 1
            arr = simulate_even(arr)
            log(arr)
            if arr == sorted_arr:
                break

        log("\n\nff3\n")
        log(cleft)
        log(cright)
        log(maxres, cnt)
        assert maxres == cnt

    return maxres


if OFFLINE_TEST:
    for _ in range(100):
        length = random.randint(1,5)*2 + 1
        arr = list(range(length))
        random.shuffle(arr)
        solve(arr)


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
    arr = list(map(int,input().split()))
    # lst = minus_one(lst)
    arr = [x-1 for x in arr]

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(arr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)