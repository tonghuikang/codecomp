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


def medianSlidingWindow(nums, k):
	small, large = [], []
	for i, x in enumerate(nums[:k]): 
		heapq.heappush(small, (-x,i))
	for _ in range(k-(k>>1)): 
		move(small, large)
	ans = [get_med(small, large, k)]
	for i, x in enumerate(nums[k:]):
		if x >= large[0][0]:
			heapq.heappush(large, (x, i+k))
			if nums[i] <= large[0][0]: 
				move(large, small)
		else:
			heapq.heappush(small, (-x, i+k))
			if nums[i] >= large[0][0]: 
				move(small, large)
		while small and small[0][1] <= i: 
			heapq.heappop(small)
		while large and large[0][1] <= i: 
			heapq.heappop(large)
		ans.append(get_med(small, large, k))
	return ans

def move(h1, h2):
	x, i = heapq.heappop(h1)
	heapq.heappush(h2, (-x, i))
	
def get_med(h1, h2, k):
	return h2[0][0] if k & 1 else -h1[0][0]


# https://leetcode.com/problems/sliding-window-median/discuss/262689/Python-Small-and-Large-Heaps
# https://stackoverflow.com/questions/55785883/how-to-calculate-the-maximum-median-in-an-array
# https://codeforces.com/blog/entry/21103


def check(arr, q, mink):
    arr = [x-q for x in arr]
    arr = [1 if x > 0 else -1 if x < 0 else 1 for x in arr]
    # log(arr)

    cursum_advance = sum(arr[:mink])
    cursum = 0
    minsum = 0
    for x,y in zip(arr, arr[mink:]):
        cursum += x
        cursum_advance += y
        minsum = min(cursum, minsum)
        if cursum_advance - minsum > 0:
            return True
    return False

# maximum median of size 
def solve_(lst, k):
    # your solution here

    size_k = medianSlidingWindow(lst, k)
    log(size_k)

    if k == len(lst):
        return max(size_k)
    size_k1 = medianSlidingWindow(lst, k+1)

    log(size_k1)
    if k == len(lst) - 1:
        return max(max(size_k),  max(size_k1))

    upper = 2**20
    lower = 0
    for i in range(20):
        mid = (upper + lower) // 2
        res = check(lst, mid, k)
        # log(lower, upper, mid, res)
        if not res:
            upper = mid
        else:
            lower = mid

    for i in range(mid+1,mid-2,-1):
        res = check(lst, i, k)
        # log(i, res)
        if res:
            return max(max(size_k), max(size_k1), i)

    return max(max(size_k), max(size_k1), i)


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,k = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(lst, k)  # include input here
    
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