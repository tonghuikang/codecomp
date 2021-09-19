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

#This function merges two sorted arrays and returns inversion count in the arrays.*/
def merge(arr, temp, left, mid, right):
    inv_count = 0

    i = left #i is index for left subarray*/
    j = mid #j is index for right subarray*/
    k = left #k is index for resultant merged subarray*/
    while ((i <= mid - 1) and (j <= right)):
        if (arr[i] <= arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

            #this is tricky -- see above explanation/
            # diagram for merge()*/
            inv_count = inv_count + (mid - i)

    #Copy the remaining elements of left subarray
    # (if there are any) to temp*/
    while (i <= mid - 1):
        temp[k] = arr[i]
        k += 1
        i += 1

    #Copy the remaining elements of right subarray
    # (if there are any) to temp*/
    while (j <= right):
        temp[k] = arr[j]
        k += 1
        j += 1

    # Copy back the merged elements to original array*/
    for i in range(left,right+1,1):
        arr[i] = temp[i]

    return inv_count

#An auxiliary recursive function that sorts the input
# array and returns the number of inversions in the
# array. */
def _mergeSort(arr, temp, left, right):
    inv_count = 0
    if (right > left):
        # Divide the array into two parts and call
        #_mergeSortAndCountInv()
        # for each of the parts */
        mid = int((right + left)/2)

        #Inversion count will be sum of inversions in
        # left-part, right-part and number of inversions
        # in merging */
        inv_count = _mergeSort(arr, temp, left, mid)
        inv_count += _mergeSort(arr, temp, mid+1, right)

        # Merge the two parts*/
        inv_count += merge(arr, temp, left, mid+1, right)

    return inv_count

#This function sorts the input array and returns the
#number of inversions in the array */
def countSwaps(arr):
    n = len(arr)
    temp = [0 for i in range(n)]
    return _mergeSort(arr, temp, 0, n - 1)


def solve_(arr, k):
    # your solution here

    indexes = [[] for _ in range(k)]
    for i,x in enumerate(arr):
        indexes[x].append(i)


    mincost = 10**10

    for start in range(len(arr) - k + 1):
        draws = []

        for i in range(k):
            idx = bisect.bisect_left(indexes[i], start+i)
            if idx == len(indexes[i]):
                idx -= 1
            cur = indexes[i][idx]
            draws.append(cur)

        draws_set = set(draws)

        target = []
        for j,x in enumerate(arr):
            if j in draws_set:
                continue
            target.append(x)

        target = target[:start] + list(range(k)) + target[start:]

        indexes_target = [[] for _ in range(k)]
        for i,x in enumerate(target):
            indexes_target[x].append(i)

        array_to_sort = [-1 for _ in arr]
        for m in range(k):
            v1 = indexes_target[m]
            v2 = indexes[m]
            for a,b in zip(v1,v2):
                array_to_sort[a] = b

        cost = countSwaps(array_to_sort)

        mincost = min(mincost, cost)

    return mincost


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
    lst = [x-1 for x in lst]
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(lst,k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
